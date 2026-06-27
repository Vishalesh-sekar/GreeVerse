from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from app.media_store import load_media

from app.screens.photos_screen import PhotosScreen
from app.screens.image_viewer_screen import ImageViewerScreen

from app.screens.videos_screen import VideosScreen
from app.screens.video_player_screen import VideoPlayerScreen

from app.screens.audio_screen import AudioScreen
from app.screens.audio_player_screen import AudioPlayerScreen

from app.screens.documents_screen import DocumentsScreen
from app.screens.document_details_screen import DocumentDetailsScreen

from app.screens.search_screen import SearchScreen
from app.screens.settings_screen import SettingsScreen


class GreeVerseApp(App):
    def build(self):
        load_media()

        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(PhotosScreen(name="photos"))
        sm.add_widget(ImageViewerScreen(name="image_viewer"))

        sm.add_widget(VideosScreen(name="videos"))
        sm.add_widget(VideoPlayerScreen(name="video_player"))

        sm.add_widget(AudioScreen(name="audio"))
        sm.add_widget(AudioPlayerScreen(name="audio_player"))

        sm.add_widget(DocumentsScreen(name="documents"))
        sm.add_widget(DocumentDetailsScreen(name="document_details"))

        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(SettingsScreen(name="settings"))

        sm.current = "photos"
        return sm