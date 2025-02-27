# ch 4.2.1 main.py

# 애플리케이션 구현에 필요한 라이브러리 추가
import sys
from ui import View # ui.py에서 View 클래스를 가져옴
from ctrl import Control # ctrl.py에서 Control 클래스를 가져옴
from PyQt5.QtWidgets import QApplication

def main(): # 프로그램 실행(Application) 함수
  calc = QApplication(sys.argv) # QApplication 객체 생성
  app = QApplication(sys.argv) # QApplication 객체 생성
  view = View() # View 클래스 인스턴스화
  Control(view = view) # Control 클래스 인스턴스화
  sys.exit(app.exec_()) # 프로그램 종료

if __name__ == "__main__": # main.py를 main() 함수 실행
  main()