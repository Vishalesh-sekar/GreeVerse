from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

from app.media_store import get_audio

from core.media_manager.media_manager import (
    rename_file,
    copy_file,
    move_file,
    safe_delete_file
)

from core.favorites.favorites_manager import (
    add_favorite,
    remove_favorite,
    is_favorite
)

from core.privacy.private_access import (
    is_private,
    mark_as_private,
    remove_from_private
)

from app.widgets.option_popup import show_message
from app.widgets.rename_popup import show_rename_popup
from app.widgets.copy_popup import show_copy_popup
from app.widgets.move_popup import show_move_popup

from utils.file_utils import format_size


class AudioPlayerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None
        self.sound = None
        self.playlist = []
        self.index = 0

        root = BoxLayout(orientation="vertical", padding=15, spacing=10)

        self.icon = Label(text="🎵", font_size=80, color=(0, 0, 0, 1))
        self.title = Label(text="No Audio", color=(0, 0, 0, 1), font_size=20)
        self.status = Label(text="Stopped", color=(0.3, 0.3, 0.3, 1))

        controls = BoxLayout(size_hint_y=None, height=55)

        back_btn = Button(text="Back")
        prev_btn = Button(text="Prev")
        play_btn = Button(text="Play")
        pause_btn = Button(text="Pause")
        stop_btn = Button(text="Stop")
        next_btn = Button(text="Next")

        back_btn.bind(on_release=lambda x: self.go_back())
        prev_btn.bind(on_release=lambda x: self.previous_audio())
        play_btn.bind(on_release=lambda x: self.play())
        pause_btn.bind(on_release=lambda x: self.pause())
        stop_btn.bind(on_release=lambda x: self.stop())
        next_btn.bind(on_release=lambda x: self.next_audio())

        for btn in [back_btn, prev_btn, play_btn, pause_btn, stop_btn, next_btn]:
            controls.add_widget(btn)

        actions = BoxLayout(size_hint_y=None, height=55)

        rename_btn = Button(text="Rename")
        copy_btn = Button(text="Copy")
        move_btn = Button(text="Move")
        fav_btn = Button(text="Favorite")
        private_btn = Button(text="Private")
        delete_btn = Button(text="Delete")
        details_btn = Button(text="Details")

        rename_btn.bind(on_release=lambda x: self.rename_current())
        copy_btn.bind(on_release=lambda x: self.copy_current())
        move_btn.bind(on_release=lambda x: self.move_current())
        fav_btn.bind(on_release=lambda x: self.favorite_current())
        private_btn.bind(on_release=lambda x: self.private_current())
        delete_btn.bind(on_release=lambda x: self.delete_current())
        details_btn.bind(on_release=lambda x: self.show_details())

        for btn in [
            rename_btn,
            copy_btn,
            move_btn,
            fav_btn,
            private_btn,
            delete_btn,
            details_btn
        ]:
            actions.add_widget(btn)

        root.add_widget(self.icon)
        root.add_widget(self.title)
        root.add_widget(self.status)
        root.add_widget(controls)
        root.add_widget(actions)

        self.add_widget(root)

    def set_audio(self, media):
        self.stop()

        self.playlist = get_audio()
        self.media = media

        if media in self.playlist:
            self.index = self.playlist.index(media)

        self.load_current()
        self.play()

    def load_current(self):
        if not self.playlist:
            return

        self.media = self.playlist[self.index]
        self.title.text = self.media.name
        self.sound = SoundLoader.load(self.media.path)

    def play(self):
        if self.sound:
            self.sound.play()
            self.status.text = "Playing"

    def pause(self):
        if self.sound:
            self.sound.stop()
            self.status.text = "Paused"

    def stop(self):
        if self.sound:
            self.sound.stop()
            self.status.text = "Stopped"

    def next_audio(self):
        if not self.playlist:
            return

        self.stop()
        self.index = (self.index + 1) % len(self.playlist)
        self.load_current()
        self.play()

    def previous_audio(self):
        if not self.playlist:
            return

        self.stop()
        self.index = (self.index - 1) % len(self.playlist)
        self.load_current()
        self.play()

    def rename_current(self):
        if self.media:
            show_rename_popup(self.media, self.do_rename)

    def do_rename(self, media, new_name):
        self.stop()
        updated_media = rename_file(media, new_name)

        if updated_media:
            self.media = updated_media
            self.title.text = updated_media.name
            self.sound = SoundLoader.load(updated_media.path)
            show_message("Renamed", "Audio renamed successfully")
        else:
            show_message("Rename Failed", "Could not rename audio")

    def copy_current(self):
        if self.media:
            show_copy_popup(self.media, self.do_copy)

    def do_copy(self, media, destination_folder):
        copied_path = copy_file(media, destination_folder)

        if copied_path:
            show_message("Copied", f"Copied to:\n{copied_path}")
        else:
            show_message("Copy Failed", "Could not copy audio")

    def move_current(self):
        if self.media:
            show_move_popup(self.media, self.do_move)

    def do_move(self, media, destination_folder):
        self.stop()
        moved_media = move_file(media, destination_folder)

        if moved_media:
            self.media = moved_media
            self.title.text = moved_media.name
            self.sound = SoundLoader.load(moved_media.path)
            show_message("Moved", "Audio moved successfully")
        else:
            show_message("Move Failed", "Could not move audio")

    def favorite_current(self):
        if not self.media:
            return

        if is_favorite(self.media):
            remove_favorite(self.media)
            show_message("Favorite", "Removed from favorites")
        else:
            add_favorite(self.media)
            show_message("Favorite", "Added to favorites")

    def private_current(self):
        if not self.media:
            return

        if is_private(self.media):
            remove_from_private(self.media)
            show_message("Private", "Removed from private files")
        else:
            mark_as_private(self.media)
            show_message("Private", "Marked as private")

    def delete_current(self):
        if not self.media:
            return

        self.stop()
        deleted_media = safe_delete_file(self.media)

        if deleted_media:
            show_message("Moved to Trash", "Audio moved to GreeVerse trash")
            self.manager.current = "audio"
        else:
            show_message("Delete Failed", "Could not move audio to trash")

    def show_details(self):
        if self.media:
            message = (
                f"Name: {self.media.name}\n"
                f"Type: {self.media.media_type}\n"
                f"Extension: {self.media.extension}\n"
                f"Size: {format_size(self.media.size)}\n"
                f"Path: {self.media.path}"
            )

            show_message("Audio Details", message)

    def go_back(self):
        self.stop()
        self.manager.current = "audio"