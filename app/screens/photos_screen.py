from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from app.screens.base_screen import BaseScreen
from app.media_store import get_images


class PhotosScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Photos"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=3, spacing=8, padding=8, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_images():
            btn = Button(
                text=media.name,
                size_hint_y=None,
                height=120
            )
            btn.bind(on_release=lambda instance, m=media: self.open_image(m))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_image(self, media):
        viewer = self.manager.get_screen("image_viewer")
        viewer.set_image(media)
        self.manager.current = "image_viewer"