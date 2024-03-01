from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
        
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('credentials_db.db')
        
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click Cancel to exit", QtWidgets.QMessageBox.Cancel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS credentials (ID integer primary key AUTOINCREMENT, Service VARCHAR(40), Login VARCHAR(40), Password VARCHAR(40))")
        return True
    
    def execute_query_with_params(self, sql_query, query_values = None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
           for query_value in query_values:
               query.addBindValue(query_value)
        query.exec()
        return query
        
    def add_new_credential_query(self, service, login, password):
        sql_query = "INSERT INTO credentials (Service, Login, Password) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [service, login, password])
    
    def edit_new_credential_query(self, service, login, password, id):
        sql_query = "UPDATE credentials SET Service=?, Login=?, Password=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [service, login, password, id])
        
    def delete_new_credential_query(self, id):
        sql_query = "DELETE FROM credentials WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])