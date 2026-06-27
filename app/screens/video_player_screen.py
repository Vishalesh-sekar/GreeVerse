from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.label import Label

from app.media_store import get_videos

from app.widgets.option_popup import show_message
from app.widgets.rename_popup import show_rename_popup
from app.widgets.copy_popup import show_copy_popup
from app.widgets.move_popup import show_move_popup

from core.media_controller.media_actions import (
    rename_media,
    copy_media,
    move_media,
    delete_media_to_trash,
    toggle_favorite,
    toggle_private,
    get_media_details
)


class VideoPlayerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None
        self.playlist = []
        self.index = 0

        root = BoxLayout(orientation="vertical")

        self.title = Label(
            text="Video Player",
            size_hint_y=None,
            height=45,
            color=(0, 0, 0, 1)
        )

        self.video = Video(state="stop", options={"eos": "stop"})

        controls = BoxLayout(size_hint_y=None, height=55)

        player_buttons = [
            ("Back", self.go_back),
            ("Prev", self.previous_video),
            ("Play", self.play),
            ("Pause", self.pause),
            ("Stop", self.stop),
            ("Next", self.next_video),
        ]

        for text, callback in player_buttons:
            btn = Button(text=text)
            btn.bind(on_release=lambda instance, cb=callback: cb())
            controls.add_widget(btn)

        actions = BoxLayout(size_hint_y=None, height=55)

        action_buttons = [
            ("Rename", self.rename_current),
            ("Copy", self.copy_current),
            ("Move", self.move_current),
            ("Delete", self.delete_current),
            ("Favorite", self.favorite_current),
            ("Private", self.private_current),
            ("Details", self.show_details),
        ]

        for text, callback in action_buttons:
            btn = Button(text=text)
            btn.bind(on_release=lambda instance, cb=callback: cb())
            actions.add_widget(btn)

        root.add_widget(self.title)
        root.add_widget(self.video)
        root.add_widget(controls)
        root.add_widget(actions)

        self.add_widget(root)

    def set_video(self, media):
        self.playlist = get_videos()
        self.media = media

        if media in self.playlist:
            self.index = self.playlist.index(media)

        self.load_current()

    def load_current(self):
        if not self.playlist:
            return

        self.media = self.playlist[self.index]
        self.title.text = self.media.name
        self.video.source = self.media.path
        self.video.state = "play"

    def play(self):
        self.video.state = "play"

    def pause(self):
        self.video.state = "pause"

    def stop(self):
        self.video.state = "stop"

    def next_video(self):
        if not self.playlist:
            return

        self.stop()
        self.index = (self.index + 1) % len(self.playlist)
        self.load_current()

    def previous_video(self):
        if not self.playlist:
            return

        self.stop()
        self.index = (self.index - 1) % len(self.playlist)
        self.load_current()

    def rename_current(self):
        if self.media:
            self.stop()
            show_rename_popup(self.media, self.do_rename)

    def do_rename(self, media, new_name):
        updated_media = rename_media(media, new_name)

        if updated_media:
            self.media = updated_media
            self.title.text = updated_media.name
            self.video.source = updated_media.path
            show_message("Renamed", "Video renamed successfully")
        else:
            show_message("Rename Failed", "Could not rename video")

    def copy_current(self):
        if self.media:
            show_copy_popup(self.media, self.do_copy)

    def do_copy(self, media, destination_folder):
        copied_path = copy_media(media, destination_folder)

        if copied_path:
            show_message("Copied", f"Copied to:\n{copied_path}")
        else:
            show_message("Copy Failed", "Could not copy video")

    def move_current(self):
        if self.media:
            self.stop()
            show_move_popup(self.media, self.do_move)

    def do_move(self, media, destination_folder):
        moved_media = move_media(media, destination_folder)

        if moved_media:
            self.media = moved_media
            self.title.text = moved_media.name
            self.video.source = moved_media.path
            show_message("Moved", "Video moved successfully")
        else:
            show_message("Move Failed", "Could not move video")

    def delete_current(self):
        if not self.media:
            return

        self.stop()
        deleted_media = delete_media_to_trash(self.media)

        if deleted_media:
            show_message("Moved to Trash", "Video moved to GreeVerse trash")
            self.manager.current = "videos"
        else:
            show_message("Delete Failed", "Could not move video to trash")

    def favorite_current(self):
        if not self.media:
            return

        added = toggle_favorite(self.media)

        if added:
            show_message("Favorite", "Added to favorites")
        else:
            show_message("Favorite", "Removed from favorites")

    def private_current(self):
        if not self.media:
            return

        marked = toggle_private(self.media)

        if marked:
            show_message("Private", "Marked as private")
        else:
            show_message("Private", "Removed from private files")

    def show_details(self):
        if self.media:
            show_message("Video Details", get_media_details(self.media))

    def go_back(self):
        self.stop()
        self.manager.current = "videos"