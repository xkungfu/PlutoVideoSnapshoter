# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QAction, QMenu)

from pluto.ui.qt.mvc.views import View


class ImageStitchingWindow(View):
    def __init__(self):
        super(ImageStitchingWindow, self).__init__(ui_file="image_stitching_window.ui")
        self.imageListWidget.setIconSize(QSize(96, 96))
        self.imageListWidget.resize(self.width() * 0.67, self.imageListWidget.height())
        self.upImageLabel.setGeometry(0, 0, 0, 0)
        self.upImageLabel.setStyleSheet("QLabel { background-color : rgba(0,0,0,.8); opacity:0.3;}")
        self.downImageLabel.setGeometry(0, 0, 0, 0)
        self.downImageLabel.setStyleSheet("QLabel { background-color : rgba(0,0,0,.8); opacity:0.3;}")
        self.__init_context_menu()

    def __init_context_menu(self):
        self.contextMenu = QMenu()
        self.previewSelectedAction = QAction("Preview selected", self)
        self.previewAllAction = QAction("Preview all", self)
        self.saveSelectedAction = QAction("Save selected", self)
        self.saveAllAction = QAction("Save all", self)
        self.contextMenu.addAction(self.previewSelectedAction)
        self.contextMenu.addAction(self.previewAllAction)
        self.contextMenu.addAction(self.saveSelectedAction)
        self.contextMenu.addAction(self.saveAllAction)
        self.imageListWidget.customContextMenuRequested.connect(self.on_open_menu)

    def on_open_menu(self, position):
        self.contextMenu.exec_(self.imageListWidget.mapToGlobal(position))