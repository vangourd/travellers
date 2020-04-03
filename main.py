import sys, random
from PySide2.QtWidgets import QDialog, QApplication
from board import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tileOptions = [
            {"name":"aura","path":"img/aura.svg","used":0},
            {"name":"gas","path":"img/gas.svg","used":0},
            {"name":"nova","path":"img/nova.svg","used":0},
            {"name":"fire","path":"img/fire.svg","used":0},
            {"name":"steel","path":"img/steel.svg","used":0},
            {"name":"asteroids","path":"img/asteroids.svg","used":0}
        ]
        self.ui.tiles = [
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
        for tile in self.ui.tiles:
            if tile.objectName() == "tile_10":
                tile.setPixmap(QPixmap(self.ui.tileOptions[5]['path']))
                print(tile)
                continue
            choice = random.randrange(5)
            current_tile = self.ui.tileOptions[choice]
            tile.setPixmap(QPixmap(current_tile['path']))
            current_tile['used'] += 1
            
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())