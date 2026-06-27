from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

from utils.file_utils import format_size
from app.theme.colors import PEACH, LAGOON


class MediaCard(BoxLayout):
    def __init__(self, media, on_open=None, thumbnail=None, **kwargs):
        super().__init__(orientation="vertical", padding=8, spacing=5, **kwargs)

        self.media = media
        self.size_hint_y = None
        self.height = 180

        with self.canvas.before:
            Color(*PEACH)
            self.bg = RoundedRectangle(radius=[18], pos=self.pos, size=self.size)

        self.bind(pos=self.update_bg, size=self.update_bg)

        if thumbnail:
            preview = Image(source=thumbnail, fit_mode="cover", size_hint_y=0.58)
        else:
            preview = Label(text=self.get_icon(), font_size=42, color=(0, 0, 0, 1))

        title = Label(
            text=media.name[:28],
            color=(0, 0, 0, 1),
            font_size=13,
            size_hint_y=0.18
        )

        size = Label(
            text=format_size(media.size),
            color=(0.25, 0.25, 0.25, 1),
            font_size=11,
            size_hint_y=0.14
        )

        open_btn = Button(
            text="Open",
            size_hint_y=0.22,
            background_normal="",
            background_color=LAGOON
        )

        if on_open:
            open_btn.bind(on_release=lambda x: on_open(media))

        self.add_widget(preview)
        self.add_widget(title)
        self.add_widget(size)
        self.add_widget(open_btn)

    def get_icon(self):
        if self.media.media_type == "video":
            return "▶"
        if self.media.media_type == "audio":
            return "🎵"
        if self.media.media_type == "document":
            return "📄"
        return "🖼"

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size