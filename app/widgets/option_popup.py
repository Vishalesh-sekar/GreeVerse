from kivy.uix.popup import Popup
from kivy.uix.label import Label


def show_message(title, message):
    popup = Popup(
        title=title,
        content=Label(text=message),
        size_hint=(0.8, 0.45)
    )
    popup.open()