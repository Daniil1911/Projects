import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout
import pygame

pygame.init()


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.playsound = None
        self.pause = None

        self.init_ui()

    def init_ui(self):
        self.song_1 = QPushButton("Загрузить")
        self.pause = QPushButton("пауза")
        self.play_it = QPushButton("Воспроизвести")
        h_box = QHBoxLayout()
        h_box.addWidget(self.song_1)
        h_box.addWidget(self.play_it)
        h_box.addWidget(self.pause)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("mp3")

        self.song_1.clicked.connect(self.song_1_open)
        self.pause.clicked.connect(self.pause_songs)
        self.play_it.clicked.connect(self.play_songs)

        self.show()

    def pause_songs(self):
        if self.playsound is None:
            self.pause.setText("_пауза_")
            self.playsound = "пауза"
            pygame.mixer.music.pause()
        else:
            self.pause.setText("Пауза")
            self.playsound = None
            pygame.mixer.music.unpause()

    def song_1_open(self):
        file = QFileDialog.getOpenFileName(self, "Open", os.getenv("HOME"))
        print(file)
        self.data_1 = file[0]

    def play_songs(self):
        self.playsound = pygame.mixer.init()
        pygame.mixer.music.load(self.data_1)
        pygame.mixer.music.play()


app = QApplication(sys.argv)
pencere = Interface()
sys.exit(app.exec_())
