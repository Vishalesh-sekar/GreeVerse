from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from app.widgets.top_bar import TopBar
from app.widgets.bottom_nav import BottomNav


class BaseScreen(Screen):
    section_order = ["photos", "videos", "audio", "documents"]

    def build_root(self, title):
        root = BoxLayout(orientation="vertical")

        top_bar = TopBar(
            title=f"GreeVerse - {title}",
            on_search=lambda: self.go_to("search"),
            on_settings=lambda: self.go_to("settings")
        )

        self.content = BoxLayout(orientation="vertical")

        bottom_nav = BottomNav(on_navigate=self.go_to)

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