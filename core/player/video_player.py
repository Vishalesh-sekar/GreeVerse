import cv2


class VideoPlayer:
    def __init__(self):
        self.video_list = []
        self.current_index = 0

    def load_playlist(self, video_list):
        self.video_list = video_list
        self.current_index = 0

    def play(self, index=0):
        if not self.video_list:
            print("No video files found")
            return False

        if index < 0 or index >= len(self.video_list):
            print("Invalid video index")
            return False

        self.current_index = index
        video = self.video_list[self.current_index]

        cap = cv2.VideoCapture(video.path)

        if not cap.isOpened():
            print(f"Cannot open video: {video.name}")
            return False

        print(f"Playing: {video.name}")
        print("Press Q to quit video")

        while True:
            success, frame = cap.read()

            if not success:
                break

            cv2.imshow("GreeVerse Video Player", frame)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        return True

    def next_video(self):
        if not self.video_list:
            return False

        self.current_index = (self.current_index + 1) % len(self.video_list)
        return self.play(self.current_index)

    def previous_video(self):
        if not self.video_list:
            return False

        self.current_index = (self.current_index - 1) % len(self.video_list)
        return self.play(self.current_index)