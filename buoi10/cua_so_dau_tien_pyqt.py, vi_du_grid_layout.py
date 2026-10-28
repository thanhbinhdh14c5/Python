#Hoatdong 1
#bai1.1
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
class CuaSoDauTien(QWidget):
 def __init__(self):
   super().__init__()
   self.setWindowTitle("Cua so PyQt dau tien")
   self.resize(300, 200)
   layout = QVBoxLayout()
   nhan = QLabel("Xin chao PyQt!")
   layout.addWidget(nhan)
   self.setLayout(layout)
app = QApplication(sys.argv)
cua_so = CuaSoDauTien()
cua_so.show()
sys.exit(app.exec_())


#Bài tập 1.2 – QHBoxLayout và QGridLayout:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
class ViDuGridLayout(QWidget):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("Vi du QGridLayout")
  self.resize(300, 200)
  layout = QGridLayout()
  layout.addWidget(QLabel("Ho ten:"), 0, 0)
  layout.addWidget(QLabel("Tuoi:"), 1, 0)
  layout.addWidget(QPushButton("Dong y"), 2, 0)
  layout.addWidget(QPushButton("Huy"), 2, 1)
  self.setLayout(layout)
app = QApplication(sys.argv)
cua_so = ViDuGridLayout()
cua_so.show()
sys.exit(app.exec_())