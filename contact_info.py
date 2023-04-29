from PyQt6.QtWidgets import *
from db_handler import DBHandler
from PyQt6.QtGui import *

class Contact_info(QWidget):
    
    def __init__(self,first) -> None:
        super().__init__()

        self.setWindowTitle("Contacts Info")
        self.setWindowIcon(QIcon('contact.png'))
        self.__db = DBHandler()
        self.v_box = QVBoxLayout()
        self.list = QListWidget()
        self.v_box.addWidget(self.list)
        self.setLayout(self.v_box)
        self.first = first
        self.get_one(self.first)
        self.set_typeText(self.list,10)
    
    def set_typeText(self,obj,s):
        #obj.setFond(QFont("Italic",s))
        obj.setStyleSheet("QListWidget"
                                  "{"
                                  "border : 2px solid black;"
                                  "background : lightblue;"
                                  "}"
                                  "QListWidget QScrollBar"
                                  "{"
                                  "background : blue;"
                                  "}"
                                  "QListView::item:selected"
                                  "{"
                                  "border : 2px solid black;"
                                  "background : green;"
                                  "}"
                                  )
    def get_one(self,first):
        for k,v in self.__db.get_all().items():
                if first in str(v):
                    self.list.addItem(f"{k} | {v}")
 