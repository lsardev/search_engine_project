from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
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

		#tab widget
		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
		self.tabs.currentChanged.connect(self.current_tab_changed)

		self.tabs.setTabsClosable(True)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.tabs.setMovable(False)
		self.tabs.setIconSize(QtCore.QSize(220,250))

		#creating sidebar
		toolbarBox = QToolBar(self)
		toolbarBox.setFixedHeight(1000)
		toolbarBox.setFixedWidth(100)
		toolbarBox.setIconSize(QSize(100, 100))
		toolbarBox.setMovable(False)
		self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)

	
		self.setCentralWidget(self.tabs)

		self.showMaximized()
		self.setWindowTitle("new window")

		#status bar
		self.status = QStatusBar()
		self.setStatusBar(self.status)

		#shotcurt

		#principals
		self.home_shortcut = QShortcut(QKeySequence("Alt+Home"), self)
		self.home_shortcut.activated.connect(self.navigate_home)

		self.back_shortcut = QShortcut(QKeySequence("Shift+Home"), self)
		self.back_shortcut.activated.connect(lambda: self.tabs.currentWidget().back())

		self.next_shortcut = QShortcut(QKeySequence("Ctrl+Home"), self)
		self.next_shortcut.activated.connect(lambda: self.tabs.currentWidget().forward())

		self.reload_shortcut = QShortcut(QKeySequence("F5"), self)
		self.reload_shortcut.activated.connect(lambda: self.tabs.currentWidget().reload())

		self.newtab_shortcut = QShortcut(QKeySequence("Ctrl+T"), self)
		self.newtab_shortcut.activated.connect(self.add_new_tab)

		self.newtab_shortcut = QShortcut(QKeySequence("Ctrl+F7"), self)
		self.newtab_shortcut.activated.connect(self.close_current_tab)


		#seconds
		self.yt_shortcut = QShortcut(QKeySequence("Ctrl+Y"), self)
		self.yt_shortcut.activated.connect(self.navigate_youtube)

		self.gm_shortcut = QShortcut(QKeySequence("Ctrl+G"), self)
		self.gm_shortcut.activated.connect(self.navigate_gmail)

		self.gh_shortcut = QShortcut(QKeySequence("Ctrl+H"), self)
		self.gh_shortcut.activated.connect(self.navigate_github)

		self.stk_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
		self.stk_shortcut.activated.connect(self.navigate_stackoverflow)

		self.insta_shortcut = QShortcut(QKeySequence("Ctrl+I"), self)
		self.insta_shortcut.activated.connect(self.navigate_instagram)

		self.face_shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
		self.face_shortcut.activated.connect(self.navigate_facebook)

		self.tw_shortcut = QShortcut(QKeySequence("Ctrl+X"), self)
		self.tw_shortcut.activated.connect(self.navigate_twitter)

		#creating navigation
		navb = QToolBar("Navigation")
		navb.setFixedWidth(1620)
		self.addToolBar(navb)

		# creating back action
		back_btn = QAction(QIcon("icons/back.png") ,"Back", self)
		back_btn.setStatusTip("Back to previous page (Shift + Home)")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		navb.addAction(back_btn)

		# similarly adding next button
		next_btn = QAction(QIcon("icons/forward.png") ,"Forward", self)
		next_btn.setStatusTip("Forward to next page (Ctrl + Home)")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navb.addAction(next_btn)

		# similarly adding reload button
		reload_btn = QAction(QIcon("icons/reload.png"),"Reload", self)
		reload_btn.setStatusTip("Reload page (F5)")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navb.addAction(reload_btn)

		# creating home action
		home_btn = QAction(QIcon("icons/home.png") ,"Home", self)
		home_btn.setStatusTip("Go home (Alt + Home)")

		# adding action to home button
		home_btn.triggered.connect(self.navigate_home)
		navb.addAction(home_btn)

		# adding a separator
		navb.addSeparator()

		# creating a line edit widget for URL
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		navb.addWidget(self.urlbar)

		# similarly adding stop action
		stop_btn = QAction(QIcon("icons/stop.png"),"Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		navb.addAction(stop_btn)

		navb2 = QToolBar("Navigation 2")
		navb2.setFixedWidth(300)
		self.addToolBar(navb2)

		# creating youtube
		yt_btn = QAction(QIcon("icons/youtube.png") ,"Youtube", self)
		yt_btn.setStatusTip("Go to Youtube")
		yt_btn.triggered.connect(self.navigate_youtube)
		toolbarBox.addAction(yt_btn)


		#creating gmail
		gm_btn = QAction(QIcon("icons/gmail.png") ,"Gmail", self)
		gm_btn.setStatusTip("Go to Gmail")
		gm_btn.triggered.connect(self.navigate_gmail)
		toolbarBox.addAction(gm_btn)

		# creating github
		gith_btn = QAction(QIcon("icons/github.png") ,"Github", self)
		gith_btn.setStatusTip("Go to GitHub")
		gith_btn.triggered.connect(self.navigate_github)
		toolbarBox.addAction(gith_btn)

		#creating stackoverflow
		stk_btn = QAction(QIcon("icons/stackoverflow.png") ,"Stack Overflow", self)
		stk_btn.setStatusTip("Go to Stack Overflow")
		stk_btn.triggered.connect(self.navigate_stackoverflow)
		toolbarBox.addAction(stk_btn)

		#creating instagram
		insta_btn = QAction(QIcon("icons/instagram.png") ,"Instagram", self)
		insta_btn.setStatusTip("Go to Instagram")
		insta_btn.triggered.connect(self.navigate_instagram)
		toolbarBox.addAction(insta_btn)

		#creating facebook
		face_btn = QAction(QIcon("icons/facebook.png") ,"Facebook", self)
		face_btn.setStatusTip("Go to Facebook")
		face_btn.triggered.connect(self.navigate_facebook)
		toolbarBox.addAction(face_btn)

		#creating twitter
		tw_btn = QAction(QIcon("icons/twitter.png") ,"Twitter", self)
		tw_btn.setStatusTip("Go to Twitter")
		tw_btn.triggered.connect(self.navigate_twitter)
		toolbarBox.addAction(tw_btn)

		# creating first tab
		self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')


	#navigates
	# action to go to home
	def navigate_home(self):
		self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

	def navigate_youtube(self):
		self.tabs.currentWidget().setUrl(QUrl("http://www.youtube.com"))

	def navigate_gmail(self):
		self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/gmail/about/"))

	def navigate_github(self):
		self.tabs.currentWidget().setUrl(QUrl("https://github.com/"))

	def navigate_stackoverflow(self):
		self.tabs.currentWidget().setUrl(QUrl("https://stackoverflow.com/"))

	def navigate_instagram(self):
		self.tabs.currentWidget().setUrl(QUrl("https://www.instagram.com/"))
	
	def navigate_facebook(self):
		self.tabs.currentWidget().setUrl(QUrl("https://www.facebook.com/"))

	def navigate_twitter(self):
		self.tabs.currentWidget().setUrl(QUrl("https://twitter.com/"))
        

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
