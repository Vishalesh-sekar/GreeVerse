from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from app.screens.base_screen import BaseScreen
from app.media_store import get_documents
from core.documents.document_opener import open_document
from core.privacy.private_access import is_private
from core.privacy.password_manager import verify_password


class DocumentsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Documents"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=8, padding=8, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_documents():
            btn = Button(
                text=f"📄 {media.name}",
                size_hint_y=None,
                height=65
            )
            btn.bind(on_release=lambda instance, m=media: self.open_doc(m))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_doc(self, media):
        if is_private(media):
            password = input("Enter password: ")

            if verify_password(password):
                open_document(media)
            else:
                print("Wrong password")
        else:
            open_document(media)