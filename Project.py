import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout, QListWidget
import pygame
import glob

pygame.init()


class Interface(QWidget):

    def __init__(self):
        super().__init__()
        self.playsound = None
        self.pause = None

        self.init_ui()

    def init_ui(self):
        self.song_1 = QPushButton("Загрузить 1 песню")
        self.pause = QPushButton("Пауза")
        self.play_it = QPushButton("Воспроизвести текущую")
        self.openf = QPushButton("Открыть папку с музыкой")
        self.resize(350, 500)
        h_box = QVBoxLayout()
        h_box.addWidget(self.song_1)
        h_box.addWidget(self.play_it)
        h_box.addWidget(self.pause)
        h_box.addWidget(self.openf)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("mp3")

        self.song_1.clicked.connect(self.song_1_open)
        self.pause.clicked.connect(self.pause_songs)
        self.play_it.clicked.connect(self.play_songs)
        self.openf.clicked.connect(self.open_folder)
        self.listWidget = QListWidget()
        self.listWidget.clicked.connect(self.change)
        self.listWidget.setObjectName("listWidget")
        h_box.addWidget(self.listWidget)

        self.show()

    def open_folder(self):
        self.listWidget.clear()
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory",
                                                      '/home', QFileDialog.ShowDirsOnly))

        songs = glob.glob(os.path.join(folder, '*.mp3'))
        for file_1 in songs:
            self.listWidget.addItem(file_1)

    def change(self):
        self.data_1 = self.listWidget.currentItem().text()

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

        self.listWidget.addItem(self.data_1)

    def play_songs(self):
        self.playsound = pygame.mixer.init()
        pygame.mixer.music.load(self.data_1)
        pygame.mixer.music.play()


app = QApplication(sys.argv)
pencere = Interface()
sys.exit(app.exec_())
