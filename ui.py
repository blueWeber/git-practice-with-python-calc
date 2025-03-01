<<<<<<< HEAD
# ch 6.3.1 ui.py
=======
# ch 6.3.2 ui.py
>>>>>>> 26f4b9a (Modify activateMessage function to add an argument)

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox) # QLineEdit, QComboBox 추가
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.te1 = QPlainTextEdit()
    self.te1.setReadOnly(True)

    self.btn1 = QPushButton('Calc', self) # 버튼 이름 변경
    self.btn2 = QPushButton('Clear', self)

    self.le1 = QLineEdit('0', self) # 라인 에디트1 추가
    self.le1.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트1 오른쪽 정렬
    self.le1.setFocus(true) # 포커스 설정
    self.le1.selectAll() # 텍스트 전체 선택

    self.le2 = QLineEdit('0', self) # 라인 에디트2 추가
    self.le2.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트2 오른쪽 정렬

    self.cb = QComboBox(self) # 콤보 박스 추가
    self.cb.addItems(['+', '-', '*', '/']) # 콤보 박스 항목 추가(연산자로 사용)

    hox_formular = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
    hox_formular.addWidget(self.le1)
    hox_formular.addWidget(self.cb)
    hox_formular.addWidget(self.le2)

    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(self.btn1)
    hbox.addWidget(self.btn2)

    vbox = QVBoxLayout()
    vbox.addWidget(self.te1)
    vbox.addLayout(hox_formular) # hbox_formular 추가
    vbox.addLayout(hbox)
    vbox.addStretch(1)

    self.setLayout(vbox)

    self.setWindowTitle('Calculator')
    self.setWindowIcon(QIcon('icon.png'))
    self.resize(256, 256)
    self.show()

  def setDisplay(self, text):
    self.te1.appendPlainText(text)

  def clearMessage(self):
    self.te1.clear()