from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from app.media_store import all_media
from core.search.search_engine import search_media


class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical")

        top = BoxLayout(size_hint_y=None, height=55)

        self.search_input = TextInput(
            hint_text="Search media...",
            multiline=False
        )

        search_btn = Button(text="Search", size_hint_x=0.25)
        back_btn = Button(text="Back", size_hint_x=0.2)

        search_btn.bind(on_release=lambda x: self.search())
        back_btn.bind(on_release=lambda x: self.go_back())

        top.add_widget(self.search_input)
        top.add_widget(search_btn)
        top.add_widget(back_btn)

        self.results_box = GridLayout(cols=1, spacing=8, padding=8, size_hint_y=None)
        self.results_box.bind(minimum_height=self.results_box.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.results_box)

        root.add_widget(top)
        root.add_widget(scroll)

        self.add_widget(root)

    def search(self):
        self.results_box.clear_widgets()

        query = self.search_input.text
        results = search_media(all_media, query)

        for media in results:
            btn = Button(
                text=f"{media.media_type.upper()} | {media.name}",
                size_hint_y=None,
                height=60
            )
            self.results_box.add_widget(btn)

    def go_back(self):
        self.manager.current = "photos"