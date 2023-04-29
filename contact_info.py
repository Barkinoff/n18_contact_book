from PyQt6.QtWidgets import *
from db_handler import DBHandler
from PyQt6.QtGui import *

class Contact_info(QWidget):
    
    def __init__(self,first,last) -> None:
        super().__init__()

        self.setWindowTitle("Contacts Info")
        self.setWindowIcon(QIcon('contact.png'))
        self.__db = DBHandler()
        self.v_box = QVBoxLayout()
        self.list = QListWidget()
        self.v_box.addWidget(self.list)
        self.setLayout(self.v_box)
        self.first = first
        self.last = last
        self.get_one(self.first,self.last)
        self.set_typeText(self.list,10)
        self.cancel = QPushButton("Cancel")
        self.cancel.setStyleSheet("background: red")
        self.v_box.addWidget(self.cancel)
        self.cancel.clicked.connect(self.close)
    
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
    def get_one(self,first,last):
        for k,v in self.__db.get_all(first,last).items():
                self.list.addItem(f"{k} | {v}")
 