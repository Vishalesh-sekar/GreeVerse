from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


def show_move_popup(media, on_move):
    layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

    folder_input = TextInput(
        hint_text="Enter destination folder path",
        multiline=False
    )

    message = Label(text="Move file to folder", color=(0, 0, 0, 1))

    move_btn = Button(text="Move")
    cancel_btn = Button(text="Cancel")

    layout.add_widget(message)
    layout.add_widget(folder_input)
    layout.add_widget(move_btn)
    layout.add_widget(cancel_btn)

    popup = Popup(
        title="Move File",
        content=layout,
        size_hint=(0.85, 0.45)
    )

    def move_action(instance):
        destination = folder_input.text.strip()

        if destination:
            on_move(media, destination)
            popup.dismiss()
        else:
            message.text = "Destination folder cannot be empty"

    move_btn.bind(on_release=move_action)
    cancel_btn.bind(on_release=lambda x: popup.dismiss())

    popup.open()