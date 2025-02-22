# ch 4.2.1 main.py

# 애플리케이션 구현에 필요한 라이브러리 추가
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout) # 애플리케이션 핸들러와 빈 GUI 위젯
from PyQt5.QtGui import QIcon # 아이콘 추가

class Calculator(QWidget): # QWidget 클래스를 상속받아서 클래스를 정의
    
    def __init__(self):
        super().__init__() # 부모 클래스 QWidget을 초기화
        self.initUI() # 나머지 초기화는 initUI 함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기 전용으로 설정

        self.btn1 = QPushButton('Message', self) # 버튼 추가
        self.btn1.clicked.connect(self.activeMessage) # 버튼 클릭 시 핸들러 함수 연결

        self.btn2 = QPushButton('Clear', self) # 버튼 2 추가
        self.btn2.clicked.connect(self.clearMessage) # 버튼 클릭 시 핸들러 함수 연결

        hbox = QHBoxLayout() # 수평 박스 레이아웃 생성
        hbox.addStretch(1) # 공백
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout() # 수직 박스 레이아웃 생성
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 위젯 추가
        #vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addLayout(hbox) # btn1 위치에 hbox 배치
        vbox.addStretch(1) # 빈 공간

        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정  

        self.setWindowTitle('Calculator') # 윈도우에 표시되는 타이틀
        self.setWindowIcon(QIcon('icon.png')) # 윈도우 아이콘 추가
        self.resize(256, 256) # 윈도우 사이즈
        self.show() # 윈도우 화면이 표시되도록 호출

    def activeMessage(self): # 버튼을 클릭할 때 동작하는 함수: 메세지 박스 출력
        QMessageBox.information(self, 'Information', 'You clicked the button.') # 메세지 박스 생성
        self.te1.appendPlainText('You clicked the button!')

    def clearMessage(self): # 버튼을 클릭할 때 동작하는 함수: 텍스트 에디트 초기화
        self.te1.clear() # 텍스트 에디트 초기화

if __name__ == '__main__': # pyqt는 애플리케이션 당 1개의 QApplication 객체만 생성 가능
    app = QApplication(sys.argv) # QApplication 객체 생성
    view = Calculator() # Calculator 클래스의 객체 생성
    sys.exit(app.exec_()) # 애플리케이션이 이벤트 처리를 하도록 루프 구동