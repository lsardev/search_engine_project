from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import QIcon
import os
import sys

# main window
class MainWindow(QMainWindow):

	# constructor
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		# creating a tab widget
		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
		self.tabs.currentChanged.connect(self.current_tab_changed)
		self.tabs.setTabsClosable(True)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.setCentralWidget(self.tabs)

		# creating a status bar
		self.status = QStatusBar()
		self.setStatusBar(self.status)
		navtb = QToolBar("Navigation")
		self.addToolBar(navtb)

		# creating back action
		back_btn = QAction(QIcon("icons/back.png") ,"Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.text("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		navtb.addAction(back_btn)

		# similarly adding next button
		next_btn = QAction(QIcon("icons/forward.png") ,"Forward", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navtb.addAction(next_btn)

		# similarly adding reload button
		reload_btn = QAction(QIcon("icons/reload.png"),"Reload", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navtb.addAction(reload_btn)

		# creating home action
		home_btn = QAction(QIcon("icons/home.png") ,"Home", self)
		home_btn.setStatusTip("Go home")

		# adding action to home button
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		# adding a separator
		navtb.addSeparator()

		# creating a line edit widget for URL
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		navtb.addWidget(self.urlbar)

		# similarly adding stop action
		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		navtb.addAction(stop_btn)

		# creating first tab
		self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

	
		self.showMaximized()
		self.setWindowTitle("new window")
		
        

	# method for adding new tab
	def add_new_tab(self, qurl = None, label ="Blank"):

		if qurl is None:
			qurl = QUrl('http://www.google.com')

		# creating a QWebEngineView object
		browser = QWebEngineView()

		# setting url to browser
		browser.setUrl(qurl)

		# setting tab index
		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)

		# adding action to the browser when url is changed
		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		# adding action to the browser when loading is finished
		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

	# when double clicked is pressed on tabs
	def tab_open_doubleclick(self, i):

		if i == -1:
			self.add_new_tab()

	# when tab is changed
	def current_tab_changed(self, i):

		# get the curl
		qurl = self.tabs.currentWidget().url()
		self.update_urlbar(qurl, self.tabs.currentWidget())
		self.update_title(self.tabs.currentWidget())

	# when tab is closed
	def close_current_tab(self, i):

		if self.tabs.count() < 2:
			return

		self.tabs.removeTab(i)

	# method for updating the title
	def update_title(self, browser):

		if browser != self.tabs.currentWidget():
			return

		# get the page title
		title = self.tabs.currentWidget().page().title()
		self.setWindowTitle("% s - tab" % title)

	# action to go to home
	def navigate_home(self):

		# go to google
		self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

	# method for navigate to url
	def navigate_to_url(self):

		q = QUrl(self.urlbar.text())

		if q.scheme() == "":
			q.setScheme("http")

		self.tabs.currentWidget().setUrl(q)

	# method to update the url
	def update_urlbar(self, q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())
		self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
app.setApplicationName("My Browser")
window = MainWindow()
app.exec_()
