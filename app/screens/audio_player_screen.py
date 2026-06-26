from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.audio import SoundLoader


class AudioPlayerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None
        self.sound = None

        root = BoxLayout(orientation="vertical")

        self.title = Label(
            text="No Audio",
            color=(0, 0, 0, 1),
            font_size=22
        )

        controls = BoxLayout(size_hint_y=None, height=60)

        back_btn = Button(text="Back")
        play_btn = Button(text="Play")
        pause_btn = Button(text="Pause")
        stop_btn = Button(text="Stop")

        back_btn.bind(on_release=lambda x: self.go_back())
        play_btn.bind(on_release=lambda x: self.play())
        pause_btn.bind(on_release=lambda x: self.pause())
        stop_btn.bind(on_release=lambda x: self.stop())

        controls.add_widget(back_btn)
        controls.add_widget(play_btn)
        controls.add_widget(pause_btn)
        controls.add_widget(stop_btn)

        root.add_widget(self.title)
        root.add_widget(controls)

        self.add_widget(root)

    def set_audio(self, media):
        self.stop()
        self.media = media
        self.title.text = media.name
        self.sound = SoundLoader.load(media.path)

        if self.sound:
            self.sound.play()

    def play(self):
        if self.sound:
            self.sound.play()

    def pause(self):
        if self.sound:
            self.sound.stop()

    def stop(self):
        if self.sound:
            self.sound.stop()

    def go_back(self):
        self.stop()
        self.manager.current = "audio"