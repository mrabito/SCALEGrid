#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

version = 0.1


class DrawGrid(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowOpacity(0.5)
        self.setWindowTitle('SCALEGrid ver.' + str(version))
        self.ctrl_grids()
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def ctrl_grids(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setGeometry(5, 5, 25, 20)
        sld.setRange(5,100)
        sld.valueChanged[int].connect(self.change_opacity)

    def change_opacity(self, value):
        self.setWindowOpacity(value/100)

    # paintEvent で呼ばれる
    def draw_lines(self, qp):
        # 画面サイズを取得
        size = self.size()
        x = size.width()

        # ラインを定義
        line_solid = QPen(Qt.black, 1, Qt.SolidLine)
        line_dot = QPen(Qt.black, 1, Qt.DotLine)

        # 描画
        for i in range(17):
            pos_x = x / 16 * i
            if i % 4 == 0:
                qp.setPen(line_solid)
            else:
                qp.setPen(line_dot)
            # 縦線
            qp.drawLine(pos_x, 0, pos_x, x)
            # 横線
            qp.drawLine(0, pos_x, x, pos_x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dg = DrawGrid()
    sys.exit(app.exec_())
