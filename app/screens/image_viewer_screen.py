from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

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


class ImageViewerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None

        root = BoxLayout(orientation="vertical")

        self.title = Label(
            text="Image Viewer",
            size_hint_y=None,
            height=45,
            color=(0, 0, 0, 1)
        )

        self.image = Image(fit_mode="contain")

        controls = BoxLayout(size_hint_y=None, height=60)

        buttons = [
            ("Back", self.go_back),
            ("Rename", self.rename_current),
            ("Copy", self.copy_current),
            ("Move", self.move_current),
            ("Delete", self.delete_current),
            ("Favorite", self.favorite_current),
            ("Private", self.private_current),
            ("Details", self.show_details),
        ]

        for text, callback in buttons:
            btn = Button(text=text)
            btn.bind(on_release=lambda instance, cb=callback: cb())
            controls.add_widget(btn)

        root.add_widget(self.title)
        root.add_widget(self.image)
        root.add_widget(controls)

        self.add_widget(root)

    def set_image(self, media):
        self.media = media
        self.title.text = media.name
        self.image.source = media.path
        self.image.reload()

    def rename_current(self):
        if self.media:
            show_rename_popup(self.media, self.do_rename)

    def do_rename(self, media, new_name):
        updated_media = rename_media(media, new_name)

        if updated_media:
            self.set_image(updated_media)
            show_message("Renamed", "Image renamed successfully")
        else:
            show_message("Rename Failed", "Could not rename image")

    def copy_current(self):
        if self.media:
            show_copy_popup(self.media, self.do_copy)

    def do_copy(self, media, destination_folder):
        copied_path = copy_media(media, destination_folder)

        if copied_path:
            show_message("Copied", f"Copied to:\n{copied_path}")
        else:
            show_message("Copy Failed", "Could not copy image")

    def move_current(self):
        if self.media:
            show_move_popup(self.media, self.do_move)

    def do_move(self, media, destination_folder):
        moved_media = move_media(media, destination_folder)

        if moved_media:
            self.set_image(moved_media)
            show_message("Moved", "Image moved successfully")
        else:
            show_message("Move Failed", "Could not move image")

    def delete_current(self):
        if not self.media:
            return

        deleted_media = delete_media_to_trash(self.media)

        if deleted_media:
            show_message("Moved to Trash", "Image moved to GreeVerse trash")
            self.manager.current = "photos"
        else:
            show_message("Delete Failed", "Could not move image to trash")

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
            show_message("Image Details", get_media_details(self.media))

    def go_back(self):
        self.manager.current = "photos"