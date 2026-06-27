from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BottomNav(BoxLayout):
    def __init__(self, on_navigate, **kwargs):
        super().__init__(orientation="horizontal", size_hint_y=None, height=55, **kwargs)

        items = [
            ("Photos", "photos"),
            ("Videos", "videos"),
            ("Audio", "audio"),
            ("Docs", "documents"),
        ]

        for label, screen in items:
            btn = Button(text=label)
            btn.bind(on_release=lambda instance, s=screen: on_navigate(s))
            self.add_widget(btn)