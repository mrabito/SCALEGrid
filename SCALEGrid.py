#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

version = 0.1

class drawGrid(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowOpacity(0.5)
        self.setWindowTitle('SCALEGrid ver.' + str(version))
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        # 画面サイズを取得
        size = self.size()
        x = size.width()
        y = size.height()

        # ラインを定義
        lineSolid = QPen(Qt.black, 1, Qt.SolidLine)
        lineDot = QPen(Qt.black, 1, Qt.DotLine)

        # 描画
        for i in range(17):
            posX = x / 16 * i
            if i%4 == 0 :
                qp.setPen(lineSolid)
            else:
                qp.setPen(lineDot)
            # 縦線
            qp.drawLine(posX, 0, posX, x)
            # 横線
            qp.drawLine(0, posX, x, posX)

class control(QMainWindow):

    def main(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = drawGrid()
    sys.exit(app.exec_())