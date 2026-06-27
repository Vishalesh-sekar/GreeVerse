from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from app.screens.base_screen import BaseScreen
from app.media_store import get_documents
from app.widgets.media_card import MediaCard


class DocumentsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Documents"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, padding=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_documents():
            card = MediaCard(media, on_open=self.open_document_details)
            grid.add_widget(card)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_document_details(self, media):
        details = self.manager.get_screen("document_details")
        details.set_document(media)
        self.manager.current = "document_details"