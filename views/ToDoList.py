from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow
from database import firebase
from PyQt5 import uic


class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("views/resources/todo-list.ui", self)
        self.show()

        self.ref = firebase.ref

        self.update_list_item()
        
        self.add_todo.clicked.connect(self.add)
        self.edit_todo.clicked.connect(self.edit)
        self.delete_todo.clicked.connect(self.delete)

    def add(self):
        value = self.todo_text.text()

        if value:
            self.ref.push().set(value)

            self.todo_text.clear()
            self.update_list_item()

    def delete(self):
        selected_row = self.get_selected_row()

        if selected_row != -1:
            self.ref.child(list(self.ref.get().keys())[selected_row]).delete()
            self.update_list_item()

    def edit(self):
        selected_row = self.get_selected_row()

        if selected_row != -1:
            value = self.get_selected_value()
            ref_keys = list(self.ref.get().keys())

            self.ref.child(ref_keys[selected_row]).set(value)
            self.update_list_item()

    def update_list_item(self):
        model = QStandardItemModel()
        ref_get = self.ref.get()

        if ref_get:
            items = ref_get.items()

            for key, value in items:
                standard_item = QStandardItem(value)
                model.appendRow(standard_item)

        self.todo_list.setModel(model)

    def get_selected_row(self):
        selection_model = self.todo_list.selectionModel()
        return selection_model.currentIndex().row()

    def get_selected_value(self):
        selected_row = self.get_selected_row()
        return self.todo_list.model().item(selected_row).text()
