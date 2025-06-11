import sys
from PyQt5.QtWidgets import *

_nim = 'SD', 'SMP'
_nama = 'Alfiana Ayuan Sari'


class inputDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(inputDialogDemo, self).__init__(parent)

        layout = QFormLayout()
        self.btn = QPushButton("Graduate")

        # trigger get item
        self.btn.clicked.connect(self.getItem)

        self.le = QLineEdit()
        layout.addRow(self.btn, self.le)
        self.btn1 = QPushButton("Ambil Nama")

        # trigger get text
        self.btn1.clicked.connect(self.getText)

        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)
        self.btn2 = QPushButton("Masukan Interger")

        # trigger get int
        self.btn2.clicked.connect(self.getInt)

        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)
        self.setLayout(layout)
        self.setWindowTitle("Input Dialog demo")

    def getItem(self):
        # load NIM
        items = []
        items.extend(list(_nim))

        item, ok = QInputDialog.getItem(
            self, "Pilih Input Dialog", "Daftar Bahasa", items, 0, False)

        if ok and item:
            self.le.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, 'Input Teks', 'Masukan Nama: ')

        # check name _name
        if ok and text in _nama:
            self.le1.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "Input Integer", "Masukan Nomor")

        # check if number > maks _nim
        if ok and num <= int(max(list(_nim)[3:])):
            self.le2.setText(str(num))


def main():
    app = QApplication(sys.argv)
    ex = inputDialogDemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
