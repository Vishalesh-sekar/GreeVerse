from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from app.theme.colors import BACKGROUND, NECTARINE, LAGOON


class BaseScreen(Screen):
    section_order = ["photos", "videos", "audio", "documents"]

    def build_root(self, title):
        root = BoxLayout(orientation="vertical")

        top_bar = BoxLayout(size_hint_y=None, height=55)
        title_label = Label(
            text=f"[b]GreeVerse - {title}[/b]",
            markup=True,
            color=(0, 0, 0, 1)
        )

        search_btn = Button(text="Search", size_hint_x=0.25)
        search_btn.bind(on_release=lambda x: self.go_to("search"))

        settings_btn = Button(text="⚙", size_hint_x=0.15)
        settings_btn.bind(on_release=lambda x: self.go_to("settings"))

        top_bar.add_widget(title_label)
        top_bar.add_widget(search_btn)
        top_bar.add_widget(settings_btn)

        self.content = BoxLayout(orientation="vertical")

        bottom_nav = BoxLayout(size_hint_y=None, height=55)

        for name in self.section_order:
            btn = Button(text=name.capitalize())
            btn.bind(on_release=lambda instance, screen=name: self.go_to(screen))
            bottom_nav.add_widget(btn)

        root.add_widget(top_bar)
        root.add_widget(self.content)
        root.add_widget(bottom_nav)

        return root

    def go_to(self, screen_name):
        self.manager.current = screen_name

    def on_touch_up(self, touch):
        if abs(touch.dx) > 80:
            current = self.manager.current

            if current in self.section_order:
                index = self.section_order.index(current)

                if touch.dx < 0 and index < len(self.section_order) - 1:
                    self.manager.current = self.section_order[index + 1]

                elif touch.dx > 0 and index > 0:
                    self.manager.current = self.section_order[index - 1]

        return super().on_touch_up(touch)