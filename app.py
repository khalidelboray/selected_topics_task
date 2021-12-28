import PySide6
from PySide6.QtCore import QEasingCurve
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
from functions import Caesar_Cipher, Transposition_Cipher


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(400, 400)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.init_ui()
        self.init_events()

    def init_ui(self):
        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.move(20, 20)
        self.text_input.resize(360, 30)
        self.text_input.setStyleSheet("background-color: #f0f0f0;")

        self.algos_select = QtWidgets.QComboBox(self)
        self.algos_select.move(20, 60)
        self.algos_select.resize(360, 30)
        self.algos_select.addItem("Caesar Cipher")
        self.algos_select.addItem("Transposition Cipher")
        self.algos_select.setStyleSheet("background-color: #f0f0f0;")

        self.button = QtWidgets.QPushButton("Encode", self)
        self.button.move(20, 200)
        self.button.resize(360, 30)
        self.button.clicked.connect(self.encode)

        self.shift_label = QtWidgets.QLabel("Shift:", self)
        self.shift_label.move(20, 100)
        self.shift_label.resize(360, 30)

        self.spinbox = QtWidgets.QSpinBox(self)
        self.spinbox.move(60, 100)
        self.spinbox.resize(320, 30)
        self.spinbox.setStyleSheet("background-color: #f0f0f0;")
        self.spinbox.setRange(0, 25)
        self.spinbox.setValue(3)

        self.key_input = QtWidgets.QLineEdit(self)
        self.key_input.move(60, 100)
        self.key_input.resize(320, 30)
        self.key_input.setStyleSheet("background-color: #f0f0f0;")
        self.key_input.hide()

        self.text_output = QtWidgets.QLineEdit(self)
        self.text_output.move(20, 240)
        self.text_output.resize(360, 30)
        self.text_output.setStyleSheet("background-color: #f0f0f0;color: red;")
        self.text_output.setReadOnly(True)

        self.maintain_case = QtWidgets.QCheckBox("Maintain Case", self)
        self.maintain_case.move(20, 160)
        self.maintain_case.resize(360, 30)

        self.ignore_forigin = QtWidgets.QCheckBox("Ignore Forigin", self)
        self.ignore_forigin.move(20, 130)
        self.ignore_forigin.resize(360, 30)

        self.name_label = QtWidgets.QLabel(
            "Name: Khalid Mohamed Elborai - خالد محمد البرعي", self
        )
        # self.name_label.move(20, 280)
        self.name_label.resize(360, 50)
        self.name_label.setStyleSheet("color: black;font-size: 13px;")

        # Animate name_label QLabel with QPropertyAnimation
        self.name_animation = PySide6.QtCore.QPropertyAnimation(self.name_label, b"pos")
        self.name_animation.setDuration(1000)
        self.name_animation.setStartValue(PySide6.QtCore.QPoint(0, 280))
        self.name_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.name_animation.setEndValue(PySide6.QtCore.QPoint(20, 280))
        self.name_animation.setLoopCount(-1)
        self.name_animation.start()

        self.section_label = QtWidgets.QLabel("Section: 3", self)
        self.section_label.move(20, 340)
        self.section_label.resize(360, 30)
        self.section_label.setStyleSheet("color: black;font-size: 15px;")

    def init_events(self):
        self.button.clicked.connect(self.encode)
        self.text_input.textChanged.connect(self.encode)
        self.spinbox.valueChanged.connect(self.encode)
        self.key_input.textChanged.connect(self.encode)
        self.maintain_case.stateChanged.connect(self.encode)
        self.ignore_forigin.stateChanged.connect(self.encode)
        self.algos_select.currentTextChanged.connect(self.toggle_checkboxs)

    def toggle_checkboxs(self, algo):
        if algo == "Caesar Cipher":
            self.maintain_case.setEnabled(True)
            self.ignore_forigin.setEnabled(True)
            self.shift_label.setText("Shift:")
            self.key_input.hide()
            self.spinbox.show()
            self.spinbox.setReadOnly(False)
            self.spinbox.setRange(0, 25)

        elif algo == "Transposition Cipher":
            self.maintain_case.setEnabled(False)
            self.ignore_forigin.setEnabled(False)
            self.shift_label.setText("Key:")
            self.spinbox.hide()
            self.key_input.show()
        self.encode()

    def encode(self):

        text = self.text_input.text()

        if self.algos_select.currentText() == "Caesar Cipher":
            maintain_case = self.maintain_case.isChecked()
            ignore_forigin = self.ignore_forigin.isChecked()
            shift = self.spinbox.value()
            self.text_output.setText(
                Caesar_Cipher(text, shift, maintain_case, ignore_forigin)
            )
        elif self.algos_select.currentText() == "Transposition Cipher":
            shift = self.key_input.text()
            self.text_output.setText(Transposition_Cipher(text, shift))


# Start the app
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
