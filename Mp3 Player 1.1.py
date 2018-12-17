import sys, os
import pygame
import glob
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *

pygame.init()


class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.regulPlaysound = None
        self.regulPause = None
        self.regulPlay = None
        self.interface()

    def interface(self):
        self.setWindowTitle('Mp3 Player')
        controlBar = self.addControls()
        centralWidget = QWidget()
        centralWidget.setLayout(controlBar)
        self.setCentralWidget(centralWidget)
        self.resize(370, 620)

        self.show()

    def addControls(self):
        controlArea = QVBoxLayout()
        seekSliderLayout = QHBoxLayout()
        Buttons1 = QHBoxLayout()
        Buttons2 = QHBoxLayout()
        play_list = QHBoxLayout()
        playlistCtrlLayout = QHBoxLayout()
        self.setLayout(controlArea)
        self.listWidget = QListWidget()
        self.listWidget.clicked.connect(self.change)
        self.listWidget.setObjectName("listWidget")
        play_list.addWidget(self.listWidget)

        play_button = QPushButton('Воспроизвести')
        play_button.setFixedSize(120, 31)
        pause_button = QPushButton('Пауза')
        pause_button.setFixedSize(80, 31)
        open_music_files_button = QPushButton('Открыть папку')
        stop_music_file_button = QPushButton('Остановить')
        volume_decrease_button = QPushButton('-')
        volume_decrease_button.setFixedSize(50, 31)
        volume_increase_button = QPushButton('+')
        volume_increase_button.setFixedSize(50, 31)
        open_music_file_button = QPushButton('Загрузить трек')

        play_button.clicked.connect(self.play_music)
        pause_button.clicked.connect(self.pause_music)
        volume_decrease_button.clicked.connect(self.decrease)
        volume_increase_button.clicked.connect(self.increase)
        stop_music_file_button.clicked.connect(self.stop_music)
        open_music_file_button.clicked.connect(self.open_file)
        open_music_files_button.clicked.connect(self.open_files)

        Buttons1.addWidget(play_button)
        Buttons1.addWidget(pause_button)
        Buttons1.addWidget(volume_decrease_button)
        Buttons1.addWidget(volume_increase_button)
        Buttons2.addWidget(open_music_files_button)
        Buttons2.addWidget(stop_music_file_button)
        Buttons2.addWidget(open_music_file_button)

        controlArea.addLayout(Buttons1)
        controlArea.addLayout(Buttons2)
        controlArea.addLayout(play_list)
        return controlArea

    def open_files(self):
        self.listWidget.clear()
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory",
                                                      '/home', QFileDialog.ShowDirsOnly))

        songs = glob.glob(os.path.join(folder, '*.mp3'))
        for file_1 in songs:
            self.listWidget.addItem(file_1)

    def change(self):
        self.data_1 = self.listWidget.currentItem().text()

    def pause_music(self):
        if self.regulPlaysound != None:
            self.regulPlaysound = pygame.mixer.init()
            pygame.mixer.music.pause()
        else:
            self.regulPlaysound = True
            pygame.mixer.music.unpause()

    def stop_music(self):
        if self.regulPlaysound != None:
            self.regulPlaysound = pygame.mixer.init()
            pygame.mixer.music.stop()
        else:
            pass

    def decrease(self):
        if self.regulPlaysound != None:
            self.volume = self.volume - 0.1
            pygame.mixer.music.set_volume(self.volume)
        else:
            pass

    def increase(self):
        if self.regulPlaysound != None:
            self.volume = self.volume + 0.1
            pygame.mixer.music.set_volume(self.volume)
        else:
            pass

    def regul(self):
        if data_1 == None:
            self.regulPlay = True
            return self.regulPlay

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, "Open", os.getenv("HOME"))
        print(file)
        self.data_1 = file[0]
        self.listWidget.addItem(self.data_1)

    def play_music(self):
        self.regulPlaysound = pygame.mixer.init()
        pygame.mixer.music.load(self.data_1)
        pygame.mixer.music.play()
        self.regulPlaysound = True
        self.volume = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Player()
    sys.exit(app.exec_())
