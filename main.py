from PyQt5.QtWidgets import QApplication
from auto_label_codes import auto_label

app = QApplication([])
window = auto_label()
window.show()
app.exec_()