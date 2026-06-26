import pygame


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.is_paused = False

    def load_playlist(self, audio_list):
        self.playlist = audio_list
        self.current_index = 0

    def play(self, index=0):
        if not self.playlist:
            print("No audio files found")
            return False

        if index < 0 or index >= len(self.playlist):
            print("Invalid audio index")
            return False

        self.current_index = index
        audio = self.playlist[self.current_index]

        try:
            pygame.mixer.music.load(audio.path)
            pygame.mixer.music.play()
            self.is_paused = False

            print(f"Playing: {audio.name}")
            return True

        except pygame.error as e:
            print(f"Cannot play audio: {audio.name}")
            print(f"Reason: {e}")
            return False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True

    def resume(self):
        pygame.mixer.music.unpause()
        self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_paused = False

    def next_audio(self):
        if not self.playlist:
            return False

        self.current_index = (self.current_index + 1) % len(self.playlist)
        return self.play(self.current_index)

    def previous_audio(self):
        if not self.playlist:
            return False

        self.current_index = (self.current_index - 1) % len(self.playlist)
        return self.play(self.current_index)