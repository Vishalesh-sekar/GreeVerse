from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.label import Label


class VideoPlayerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.media = None

        root = BoxLayout(orientation="vertical")

        self.title = Label(size_hint_y=None, height=45, color=(0, 0, 0, 1))
        self.video = Video(state="stop", options={"eos": "stop"})

        controls = BoxLayout(size_hint_y=None, height=55)

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
        root.add_widget(self.video)
        root.add_widget(controls)

        self.add_widget(root)

    def set_video(self, media):
        self.media = media
        self.title.text = media.name
        self.video.source = media.path
        self.video.state = "play"

    def play(self):
        self.video.state = "play"

    def pause(self):
        self.video.state = "pause"

    def stop(self):
        self.video.state = "stop"

    def go_back(self):
        self.stop()
        self.manager.current = "videos"