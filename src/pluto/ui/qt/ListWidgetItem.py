# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidgetItem


class ListWidgetItem(QListWidgetItem):
    def __init__(self, *__args):
        super(ListWidgetItem, self).__init__(*__args)
        self.storage = None

    def set_storage(self, val):
        self.storage = val

    def get_storage(self):
        return self.storage

    def refresh_ui(self):
        self.setData(0, str(self.storage))
