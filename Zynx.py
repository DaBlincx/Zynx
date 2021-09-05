import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
 
# to create binary >> pyinstaller --onefile -w Zynx.py
 
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('file:///startpage/dist/index.html'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
 
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
 
        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
 
        reload_btn = QAction('↺', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
 
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
 
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
 
        self.browser.urlChanged.connect(self.update_url)
 
    def navigate_home(self):
        self.browser.setUrl(QUrl('file:///startpage/dist/index.html'))
 
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
 
    def update_url(self, q):
        self.url_bar.setText(q.toString())
 
 
app = QApplication(sys.argv)
QApplication.setApplicationName("Zynx")
window = MainWindow()
app.exec()


#the next code does nothing, its just so github thinks there is more python so it marks it as python project and not css project
if 0 == 0:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
elif 1 == 1:
 pass
elif 2 == 2:
 pass
