from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TopBar(BoxLayout):
    def __init__(self, title, on_search=None, on_settings=None, **kwargs):
        super().__init__(orientation="horizontal", size_hint_y=None, height=55, **kwargs)

        self.add_widget(
            Label(
                text=f"[b]{title}[/b]",
                markup=True,
                color=(0, 0, 0, 1),
                font_size=20
            )
        )

        search_btn = Button(text="Search", size_hint_x=0.28)
        settings_btn = Button(text="⚙", size_hint_x=0.16)

        if on_search:
            search_btn.bind(on_release=lambda x: on_search())

        if on_settings:
            settings_btn.bind(on_release=lambda x: on_settings())

        self.add_widget(search_btn)
        self.add_widget(settings_btn)