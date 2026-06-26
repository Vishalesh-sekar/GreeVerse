from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.screenmanager import Screen
from core.media_manager.media_manager import delete_file


class ImageViewerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.media = None

        self.root = BoxLayout(orientation="vertical")

        self.title = Label(size_hint_y=None, height=45, color=(0, 0, 0, 1))
        self.image = Image(allow_stretch=True)

        options = BoxLayout(size_hint_y=None, height=55)

        back_btn = Button(text="Back")
        delete_btn = Button(text="Delete")
        details_btn = Button(text="Details")

        back_btn.bind(on_release=lambda x: self.go_back())
        delete_btn.bind(on_release=lambda x: self.delete_current())
        details_btn.bind(on_release=lambda x: self.show_details())

        options.add_widget(back_btn)
        options.add_widget(delete_btn)
        options.add_widget(details_btn)

        self.root.add_widget(self.title)
        self.root.add_widget(self.image)
        self.root.add_widget(options)

        self.add_widget(self.root)

    def set_image(self, media):
        self.media = media
        self.title.text = media.name
        self.image.source = media.path
        self.image.reload()

    def go_back(self):
        self.manager.current = "photos"

    def delete_current(self):
        if self.media:
            delete_file(self.media)
            self.manager.current = "photos"

    def show_details(self):
        if self.media:
            self.title.text = f"{self.media.name} | {self.media.size} bytes"