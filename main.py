import sys, random
from PySide2.QtWidgets import QDialog, QApplication, QLabel
from game import *

class Board:

    def __init__(self,uiTiles,uiEdges):
        self.tiles = []
        self.edges = []
        self.setupTiles(uiTiles)
        self.setupEdges(uiEdges)
    
    def setupTiles(self,places):
        for place in places:
            self.tiles.append(Tile(place))

    def setupEdges(self, uiEdges):
        for uiEdge in uiEdges:
            self.edges.append(Edge(uiEdge))

class Edge:
    color_opts = {
        "green": {"rightToLeft":"img/edge_rl_green.svg","leftToRight":"img/edge_lr_green.svg","straight":"img/edge_straight_green.svg"},
        "blue": {"rightToLeft":"img/edge_rl_blue.svg","leftToRight":"img/edge_lr_blue.svg","straight":"img/edge_straight_blue.svg"},
        "yellow": {"rightToLeft":"img/edge_rl_yellow.svg","leftToRight":"img/edge_lr_yellow.svg","straight":"img/edge_straight_yellow.svg"},
        "red": {"rightToLeft":"img/edge_rl_red.svg","leftToRight":"img/edge_lr_red.svg","straight":"img/edge_straight_red.svg"},
    }

    def __init__(self,ui):
        self.ui = ui
        self.type = None
        self.determineType()
        print(self.type)

    def determineType(self):

        def findLeftorRight(num):
            if x % 2:
                return "leftToRight"
            else:
                return "rightToLeft"

        x = int(self.ui.objectName().strip("edge"))
        if 1 < x <= 6:
            self.type = findLeftorRight(x)
        if 6 < x <= 10:
            self.type = "straight"
        if 11 < x <= 18:
            self.type = findLeftorRight(x)
        if 19 < x <= 23:
            self.type = "straight"
        if 23 < x <= 33:
            self.type = findLeftorRight(x)
        if 33 < x <= 39:
            self.type = "straight"
        if 39 < x <= 49:
            self.type = findLeftorRight(x)
        if 49 < x <= 54:
            self.type = "straight"
        if 54 < x <= 62:
            self.type = findLeftorRight(x)
        if 62 < x <= 66:
            self.type = "straight"
        if 66 < x <= 72:
            self.type = findLeftorRight(x)

    def setColor(self, color):
        self.ui.setPixmap(QPixmap(self.color_opts[color][self.type]))

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
        self.uiEdges = []
        self.uiTiles = []
        for i in range(1,20):
            self.uiTiles.append(self.findChild(QLabel,f"tile_{i:02d}"))
        for i in range(1,73):
            self.uiEdges.append(self.findChild(QLabel,f"edge{i:02d}"))

        self.ui.startGameButton.clicked.connect(self.new_game)
        self.show()
    
    def new_game(self):
        self.ui.startGameButton.setHidden(True)
        self.board = Board(self.uiTiles,self.uiEdges)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())