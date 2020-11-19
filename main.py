import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signUpButton.clicked.connect(self.goToCreate)

    def loginFunction(self):
        email = self.email.text()
        password = self.password.text()
        print("Logged in with email/password: " + email + " / " + password)

    def goToCreate(self):
        create_account = CreateAccount()
        widget.addWidget(create_account)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("createAccount.ui", self)
        self.createAccountButton.clicked.connect(self.createAccountFunction)

    def createAccountFunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmPassword.text():
            password = self.password.text()
            print("Account created with email/password: " + email + " / " + password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(447)
widget.setFixedHeight(357)
widget.show()
app.exec_()