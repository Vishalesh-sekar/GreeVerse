from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from core.documents.document_opener import open_document

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

from core.privacy.password_manager import verify_password

from app.widgets.option_popup import show_message
from app.widgets.rename_popup import show_rename_popup
from app.widgets.copy_popup import show_copy_popup
from app.widgets.move_popup import show_move_popup

from utils.file_utils import format_size


class DocumentDetailsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        self.icon = Label(
            text="📄",
            font_size=80,
            color=(0, 0, 0, 1)
        )

        self.document_name = Label(
            text="",
            color=(0, 0, 0, 1),
            font_size=20
        )

        self.details = Label(
            text="",
            color=(0.2, 0.2, 0.2, 1)
        )

        open_btn = Button(text="Open Document", size_hint_y=None, height=45)
        rename_btn = Button(text="Rename", size_hint_y=None, height=45)
        copy_btn = Button(text="Copy", size_hint_y=None, height=45)
        move_btn = Button(text="Move", size_hint_y=None, height=45)
        fav_btn = Button(text="Favorite", size_hint_y=None, height=45)
        private_btn = Button(text="Private", size_hint_y=None, height=45)
        delete_btn = Button(text="Delete", size_hint_y=None, height=45)
        back_btn = Button(text="Back", size_hint_y=None, height=45)

        open_btn.bind(on_release=lambda x: self.open_current())
        rename_btn.bind(on_release=lambda x: self.rename_current())
        copy_btn.bind(on_release=lambda x: self.copy_current())
        move_btn.bind(on_release=lambda x: self.move_current())
        fav_btn.bind(on_release=lambda x: self.favorite_current())
        private_btn.bind(on_release=lambda x: self.private_current())
        delete_btn.bind(on_release=lambda x: self.delete_current())
        back_btn.bind(on_release=lambda x: self.go_back())

        root.add_widget(self.icon)
        root.add_widget(self.document_name)
        root.add_widget(self.details)

        for btn in [
            open_btn,
            rename_btn,
            copy_btn,
            move_btn,
            fav_btn,
            private_btn,
            delete_btn,
            back_btn
        ]:
            root.add_widget(btn)

        self.add_widget(root)

    def set_document(self, media):
        self.media = media

        self.document_name.text = media.name

        self.details.text = (
            f"Type: {media.extension}\n"
            f"Size: {format_size(media.size)}\n"
            f"Path: {media.path}"
        )

    def open_current(self):
        if not self.media:
            return

        if is_private(self.media):
            self.ask_password()
        else:
            open_document(self.media)

    def ask_password(self):
        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        message = Label(
            text="Private document",
            color=(0, 0, 0, 1)
        )

        password_input = TextInput(
            hint_text="Enter password",
            password=True,
            multiline=False
        )

        open_btn = Button(text="Open")
        cancel_btn = Button(text="Cancel")

        layout.add_widget(message)
        layout.add_widget(password_input)
        layout.add_widget(open_btn)
        layout.add_widget(cancel_btn)

        popup = Popup(
            title="Password Required",
            content=layout,
            size_hint=(0.8, 0.45)
        )

        def verify_and_open(instance):
            if verify_password(password_input.text):
                popup.dismiss()
                open_document(self.media)
            else:
                message.text = "Wrong password"

        open_btn.bind(on_release=verify_and_open)
        cancel_btn.bind(on_release=lambda x: popup.dismiss())

        popup.open()

    def rename_current(self):
        if self.media:
            show_rename_popup(self.media, self.do_rename)

    def do_rename(self, media, new_name):
        updated_media = rename_file(media, new_name)

        if updated_media:
            self.set_document(updated_media)
            show_message("Renamed", "Document renamed successfully")
        else:
            show_message("Rename Failed", "Could not rename document")

    def copy_current(self):
        if self.media:
            show_copy_popup(self.media, self.do_copy)

    def do_copy(self, media, destination_folder):
        copied_path = copy_file(media, destination_folder)

        if copied_path:
            show_message("Copied", f"Copied to:\n{copied_path}")
        else:
            show_message("Copy Failed", "Could not copy document")

    def move_current(self):
        if self.media:
            show_move_popup(self.media, self.do_move)

    def do_move(self, media, destination_folder):
        moved_media = move_file(media, destination_folder)

        if moved_media:
            self.set_document(moved_media)
            show_message("Moved", "Document moved successfully")
        else:
            show_message("Move Failed", "Could not move document")

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

        deleted_media = safe_delete_file(self.media)

        if deleted_media:
            show_message("Moved to Trash", "Document moved to GreeVerse trash")
            self.manager.current = "documents"
        else:
            show_message("Delete Failed", "Could not move document to trash")

    def go_back(self):
        self.manager.current = "documents"