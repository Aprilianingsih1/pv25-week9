import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn = QPushButton("QFileDialog static method demo")

        # trigger get file
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        self.le = QLabel("Hello")

        layout.addWidget(self.le)
        self.btn1 = QPushButton("QFileDialog object")

        # trigger get files
        self.btn1.clicked.connect(self.getfiles)

        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'D:\KULIAH', "Image files (*.jpg *.gif)")
        print(fname)
        self.le.setPixmap(QPixmap(fname)) #load gambar variabel 'le'

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                #Memunculkan `data` pada `contents` QTextEdit
                self.contents.setText(data)

def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
