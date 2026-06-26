from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from app.screens.base_screen import BaseScreen
from app.media_store import get_videos


class VideosScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Videos"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=8, padding=8, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_videos():
            btn = Button(
                text=f"▶ {media.name}",
                size_hint_y=None,
                height=70
            )
            btn.bind(on_release=lambda instance, m=media: self.open_video(m))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_video(self, media):
        player = self.manager.get_screen("video_player")
        player.set_video(media)
        self.manager.current = "video_player"