import sys, random
from PySide2.QtWidgets import QDialog, QApplication, QLabel
from game import *

class Board:

    def __init__(self,uiTiles,uiEdges,uiChits):
        self.tiles = []
        self.edges = []
        self.chits = []
        self.setupTiles(uiTiles)
        self.setupEdges(uiEdges)
        self.setupChits(uiChits)
    
    def setupTiles(self,places):
        for place in places:
            self.tiles.append(Tile(place))

    def setupEdges(self, uiEdges):
        for uiEdge in uiEdges:
            self.edges.append(Edge(uiEdge))

    def setupChits(self, uiChits):
        for uiChit in uiChits:
            self.chits.append(Chit(uiChit))

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

class Chit:
    options = [
        {"path":"img/chit02.svg","used":0},
        {"path":"img/chit03.svg","used":0},
        {"path":"img/chit04.svg","used":0},
        {"path":"img/chit05.svg","used":0},
        {"path":"img/chit06.svg","used":0},
        {"path":"img/chit08.svg","used":0},
        {"path":"img/chit09.svg","used":0},
        {"path":"img/chit10.svg","used":0},
        {"path":"img/chit11.svg","used":0},
        {"path":"img/chit12.svg","used":0},
        {"path":"img/robber.svg","used":0}
    ]

    def __init__(self,ui):
        self.ui = ui
        self.chitNo = None
        if self.ui.objectName() == "chit10":
            self.setRobber()
        else:
            self.differentiate()
    
    def differentiate(self):
        num = random.randrange(10)
        if num in [0,10]:
            max = 1
        else:
            max = 2
        if self.options[num]['used'] >= max:
            self.differentiate()
        else:
            self.ui.setPixmap(QPixmap(self.options[num]['path']).scaled(30,30,Qt.KeepAspectRatio))
            self.chitNo = num
            self.options[num]['used'] += 1
    
    def setRobber(self):
        self.ui.setPixmap(QPixmap(self.options[10]['path']).scaled(30,30,Qt.KeepAspectRatio))

    def removeRobber(self):
        self.ui.setPixmap(QPixmap(self.options[self.chitNo]['path'].scaled(30,30,Qt.KeepAspectRatio)))

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.gameStatus = "playing"
        self.uiEdges = []
        self.uiTiles = []
        self.uiChits = []
        for i in range(1,20):
            self.uiTiles.append(self.findChild(QLabel,f"tile_{i:02d}"))
        for i in range(1,73):
            self.uiEdges.append(self.findChild(QLabel,f"edge{i:02d}"))
        for i in range(1,20):
            self.uiChits.append(self.findChild(QLabel,f"chit{i:02d}"))
        self.ui.startGameButton.clicked.connect(self.new_game)
        self.show()
    
    def new_game(self):
        self.ui.startGameButton.setHidden(True)
        self.board = Board(self.uiTiles,self.uiEdges,self.uiChits)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())