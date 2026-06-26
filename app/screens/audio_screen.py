from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from app.screens.base_screen import BaseScreen
from app.media_store import get_audio


class AudioScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.build_root("Audio"))

    def on_pre_enter(self):
        self.content.clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=8, padding=8, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for media in get_audio():
            btn = Button(
                text=f"🎵 {media.name}",
                size_hint_y=None,
                height=65
            )
            btn.bind(on_release=lambda instance, m=media: self.open_audio(m))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        self.content.add_widget(scroll)

    def open_audio(self, media):
        player = self.manager.get_screen("audio_player")
        player.set_audio(media)
        self.manager.current = "audio_player"