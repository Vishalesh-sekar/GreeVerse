from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from app.screens.base_screen import BaseScreen
from app.media_store import get_images
from app.widgets.media_card import MediaCard


class PhotosScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Photos"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=3, spacing=10, padding=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_images():
            card = MediaCard(media, on_open=self.open_image, thumbnail=media.path)
            grid.add_widget(card)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_image(self, media):
        viewer = self.manager.get_screen("image_viewer")
        viewer.set_image(media)
        self.manager.current = "image_viewer"