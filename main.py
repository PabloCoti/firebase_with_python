from PyQt5.QtWidgets import QApplication
from views import ToDoList
import sys

app = QApplication(sys.argv)
main_view = ToDoList()

sys.exit(app.exec_())
