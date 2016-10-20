from src.processor import *
from src.ui import *



if __name__ == "__main__":
    p = Processor()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,p)
    MainWindow.show()
    sys.exit(app.exec_())
    p.kill()

