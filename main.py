import sys, random
from PySide2.QtWidgets import QDialog, QApplication
from board import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.choices = [
            "img/aura.svg",
            "img/gas.svg",
            "img/nova.svg",
            "img/fire.svg",
            "img/steel.svg",
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
            choice = random.randrange(5)
            tile.setPixmap(QPixmap(self.ui.choices[choice]))
            
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())