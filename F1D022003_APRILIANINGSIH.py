import sys
from PyQt5.QtWidgets import *

graduates = 'SD', 'SMP', 'SMA', 'Mahasiswa', 'S1', 'S2', 'S3'
religi = 'Islam', 'Hindu', 'Budha', 'kristen', 'Konghucu'


class tabdemo(QTabWidget):
    def __init__(self, parent=None):
        super(tabdemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.setWindowTitle("Lamaran Pekerjaan")

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        layout.addRow("Date of Birth", QLineEdit())

        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)

        self.btngraduate = QPushButton("Graduate")

        # trigger get item
        self.btngraduate.clicked.connect(self.getItem)

        self.legraduate = QLineEdit()
        layout.addRow(self.btngraduate, self.legraduate)

        self.setTabText(0, "Profile")
        self.tab1.setLayout(layout)

    def getItem(self):

        items = []
        items.extend(list(graduates))

        item, ok = QInputDialog.getItem(
            self, "Pilih Input Dialog", "Daftar Bahasa", items, 0, False)

        if ok and item:
            self.legraduate.setText(item)

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                # Memunculkan `data` pada `contents` QTextEdit
                self.contents.setText(data)

    def tab2UI(self):
        layout = QVBoxLayout()

        self.le = QLabel("Masukkan Berkas lamaran Pekerjaan")

        layout.addWidget(self.le)
        self.btn1 = QPushButton("Upload di sini")

        # trigger get files
        self.btn1.clicked.connect(self.getfiles)

        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setTabText(1, "Berkas")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Kemampuan Bahasa"))
        layout.addWidget(QCheckBox("Bahasa Korea"))
        layout.addWidget(QCheckBox("Bahasa Inggris"))
        layout.addWidget(QCheckBox("Bahasa Jepang"))
        layout.addWidget(QLabel("Kemampuan IT"))
        layout.addWidget(QCheckBox("Jaringan"))
        layout.addWidget(QCheckBox("Kecerdasan Buatan"))
        layout.addWidget(QCheckBox("Sistem Informasi"))

        self.setTabText(2, "Skill")
        self.tab3.setLayout(layout)

    def tab4UI(self):

        layout = QVBoxLayout()
        self.btnfont = QPushButton("choose font")

        # trigger get font
        self.btnfont.clicked.connect(self.getfont)

        layout.addWidget(self.btnfont)
        self.le3 = QLabel("Tampilan font sesudah diubah")

        layout.addWidget(self.le3)
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog demo")

        self.setTabText(3, "Settings")
        self.tab4.setLayout(layout)

    def getfont(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.le3.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = tabdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
