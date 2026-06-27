from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


def show_rename_popup(media, on_rename):
    layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

    name_input = TextInput(
        text=media.name,
        multiline=False
    )

    message = Label(text="Enter new file name", color=(0, 0, 0, 1))

    rename_btn = Button(text="Rename")
    cancel_btn = Button(text="Cancel")

    layout.add_widget(message)
    layout.add_widget(name_input)
    layout.add_widget(rename_btn)
    layout.add_widget(cancel_btn)

    popup = Popup(
        title="Rename File",
        content=layout,
        size_hint=(0.8, 0.45)
    )

    def rename_action(instance):
        new_name = name_input.text.strip()

        if new_name:
            on_rename(media, new_name)
            popup.dismiss()
        else:
            message.text = "Name cannot be empty"

    rename_btn.bind(on_release=rename_action)
    cancel_btn.bind(on_release=lambda x: popup.dismiss())

    popup.open()