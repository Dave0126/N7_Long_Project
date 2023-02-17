import sys
from callWindow import Window
from recvData import RcvDataThread
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = Window()
  w.show()
  # Create and start the socket thread
  recv_thread = RcvDataThread(w)
  recv_thread.start()

  sys.exit(app.exec_())