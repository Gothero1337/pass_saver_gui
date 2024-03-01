import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtSql import QSqlTableModel

from auth import Ui_Dialog as Ui_2
from dialog import Ui_Dialog
from design import Ui_MainWindow
from connection import Data

class AuthWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.ui = Ui_2()
        self.ui.setupUi(self)
        self.ui.btn_signin.clicked.connect(self.signing)
    
    def signing(self):
        if self.ui.le_login.text() == "Gothero" and self.ui.le_password.text() == "Gothero2000":
            self.accept()
        else:
          QtWidgets.QMessageBox.warning(self, "Error", "Invalid credentials!")  
        

class CredentialsSaver(QMainWindow):
    def __init__(self):
        super(CredentialsSaver, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        
        self.ui.btn_add.clicked.connect(self.open_dialog_window)
        self.ui.btn_edit.clicked.connect(self.open_dialog_window)
        self.ui.btn_del.clicked.connect(self.delete_current_credential)
        
    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('credentials')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.verticalHeader().setVisible(False)
        
        
    def open_dialog_window(self):
        self.dialog_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.dialog_window)
        self.dialog_window.show()
        sender = self.sender()
        if sender.text() == "Add credentials":
           self.ui_window.btn_ok.clicked.connect(self.add_new_credential)
        else:
           self.ui_window.btn_ok.clicked.connect(self.edit_current_credential)
        
    def add_new_credential(self):
        service = self.ui_window.le_service.text()
        login = self.ui_window.le_login.text()
        password = self.ui_window.le_password.text()
        
        self.conn.add_new_credential_query(service, login, password)
        self.view_data()
        self.dialog_window.close()
        
    def edit_current_credential(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))   
         
        service = self.ui_window.le_service.text()
        login = self.ui_window.le_login.text()
        password = self.ui_window.le_password.text()
        
        self.conn.edit_new_credential_query(service, login, password, id)
        self.view_data()
        self.dialog_window.close()
        
    def delete_current_credential(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        
        self.conn.delete_new_credential_query(id)
        self.view_data()       
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    auth_window = AuthWindow()
    window = CredentialsSaver()
    auth_window.show()
    if auth_window.exec() == QDialog.Accepted:
        window.show()
        sys.exit(app.exec())