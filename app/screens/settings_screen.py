from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from core.settings.settings_manager import load_settings, update_setting


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.label = Label(color=(0, 0, 0, 1))

        light_btn = Button(text="Light Theme")
        dark_btn = Button(text="Dark Theme")
        grid_3_btn = Button(text="Grid Size 3")
        back_btn = Button(text="Back")

        light_btn.bind(on_release=lambda x: self.set_theme("light"))
        dark_btn.bind(on_release=lambda x: self.set_theme("dark"))
        grid_3_btn.bind(on_release=lambda x: self.set_grid_size(3))
        back_btn.bind(on_release=lambda x: self.go_back())

        root.add_widget(Label(text="GreeVerse Settings", color=(0, 0, 0, 1)))
        root.add_widget(self.label)
        root.add_widget(light_btn)
        root.add_widget(dark_btn)
        root.add_widget(grid_3_btn)
        root.add_widget(back_btn)

        self.add_widget(root)

    def on_pre_enter(self):
        settings = load_settings()
        self.label.text = str(settings)

    def set_theme(self, theme):
        update_setting("theme", theme)
        self.on_pre_enter()

    def set_grid_size(self, size):
        update_setting("grid_size", size)
        self.on_pre_enter()

    def go_back(self):
        self.manager.current = "photos"