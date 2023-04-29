import sys
from PyQt6.QtWidgets import *
from Add_contact import AddContact
from db_handler import DBHandler
from contact_info import Contact_info
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__db = DBHandler()
    
        self.setWindowTitle("Contacts")
        self.setWindowIcon(QIcon('contact.png'))
        self.h_box = QHBoxLayout()
        self.add_contact = QPushButton("Add Contact")
        self.add_contact.setStyleSheet('background-color: lightgreen')
        self.h_box.addWidget(self.add_contact)
        self.v_box = QVBoxLayout()
        self.user = QLineEdit()
        self.user.setPlaceholderText("Enter name...")
        self.user.setStyleSheet("background-color: lightgreen")
        self.v_box.addWidget(self.user)
        self.contact_list = QListWidget()
        self.v_box.addWidget(self.contact_list)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        self.add_contact.clicked.connect(self.add)
        self.user.textChanged.connect(self.search)
        self.set_typeText(self.contact_list,10)
        self.update_content(self.__db.get_name())
        self.contact_list.itemClicked.connect(self.info)
    
    def set_typeText(self,obj,s):
        #obj.setFond(QFont("Italic",s))
        obj.setStyleSheet("QListWidget"
                                  "{"
                                  "border : 2px solid black;"
                                  "background : lightblue;"
                                  "}"
                                  "QListWidget QScrollBar"
                                  "{"
                                  "background : green;"
                                  "}"
                                  "QListView::item:selected"
                                  "{"
                                  "border : 2px solid black;"
                                  "background : green;"
                                  "}"
                                  )
    def add(self):
        self.c = AddContact()
        self.c.show()
        self.update_content(self.__db.get_name())
    
    def update_content(self,name):
        self.contact_list.clear()
        for i in name:
            self.contact_list.addItem(f"{i[0]} {i[1]}")

    def search(self):
        self.contact_list.clear()
        name = self.user.text()
        search = self.__db.search(name)
        self.update_content(search)
    
    def info(self):
        name = self.contact_list.currentItem().text()
        self.i = Contact_info(name)
        self.i.show()
        

app = QApplication(sys.argv)
win = MainWindow()
win.show()
exit(app.exec())