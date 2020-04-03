import sys, random
from PySide2.QtWidgets import QDialog, QApplication
from game import *

class Board:

    def __init__(self,places):
        self.tiles = []
        self.generateTiles(places)
    
    def generateTiles(self,places):
        for place in places:
            self.tiles.append(Tile(place))

class Tile:
    options = [
            {"name":"aura","path":"img/aura.svg","used":0},
            {"name":"gas","path":"img/gas.svg","used":0},
            {"name":"nova","path":"img/nova.svg","used":0},
            {"name":"fire","path":"img/fire.svg","used":0},
            {"name":"steel","path":"img/steel.svg","used":0},
            {"name":"asteroids","path":"img/asteroids.svg","used":0}
        ]

    def __init__(self, ui):
        self.ui = ui
        self.name = None
        self.type = None
        self.value = 0
        if ui.objectName() == "tile_10":
            self.setDesert()
        else:
            self.differentiate()

    def differentiate(self):
        choice = random.randrange(5)
        if self.options[choice]['used'] < 4:
            decision = self.options[choice]
            self.type = decision['name']
            self.name = self.ui.objectName()
            self.ui.setPixmap(QPixmap(decision['path']))
            self.options[choice]['used'] += 1
        else:
            self.differentiate()

    def setDesert(self):
        decision = self.options[5]
        self.type = decision['name']
        self.ui.setPixmap(QPixmap(decision['path']))

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.gameStatus = "playing"
        self.ui.places = [
            self.ui.tile_01,
            self.ui.tile_02,
            self.ui.tile_03,
            self.ui.tile_04,
            self.ui.tile_05,
            self.ui.tile_06,
            self.ui.tile_07,
            self.ui.tile_08,
            self.ui.tile_09,
            self.ui.tile_10,
            self.ui.tile_11,
            self.ui.tile_12,
            self.ui.tile_13,
            self.ui.tile_14,
            self.ui.tile_15,
            self.ui.tile_16,
            self.ui.tile_17,
            self.ui.tile_18,
            self.ui.tile_19,
        ]
        self.ui.startGameButton.clicked.connect(self.new_game)
        self.show()
    
    def new_game(self):
        self.ui.startGameButton.setHidden(True)
        self.board = Board(self.ui.places)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())