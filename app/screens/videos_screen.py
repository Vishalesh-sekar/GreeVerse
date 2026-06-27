from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from app.screens.base_screen import BaseScreen
from app.media_store import get_videos
from app.widgets.media_card import MediaCard


class VideosScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Videos"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_videos():
            card = MediaCard(media, on_open=self.open_video)
            grid.add_widget(card)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_video(self, media):
        player = self.manager.get_screen("video_player")
        player.set_video(media)
        self.manager.current = "video_player"