# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_widget(object):
    def setupUi(self, edit_widget):
        edit_widget.setObjectName("edit_widget")
        edit_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_widget.resize(1280, 720)
        self.brush_box = QtWidgets.QSpinBox(edit_widget)
        self.brush_box.setGeometry(QtCore.QRect(10, 681, 60, 30))
        self.brush_box.setMaximum(60)
        self.brush_box.setObjectName("brush_box")
        self.brush_label = QtWidgets.QLabel(edit_widget)
        self.brush_label.setGeometry(QtCore.QRect(80, 680, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.brush_label.setFont(font)
        self.brush_label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.brush_label.setIndent(10)
        self.brush_label.setObjectName("brush_label")
        self.tab_widget = QtWidgets.QTabWidget(edit_widget)
        self.tab_widget.setGeometry(QtCore.QRect(10, 10, 630, 660))
        self.tab_widget.setObjectName("tab_widget")
        self.draw_tab = QtWidgets.QWidget()
        self.draw_tab.setObjectName("draw_tab")
        self.tab_widget.addTab(self.draw_tab, "")
        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setObjectName("info_tab")
        self.tab_widget.addTab(self.info_tab, "")
        self.widget = QtWidgets.QWidget(edit_widget)
        self.widget.setGeometry(QtCore.QRect(640, 30, 630, 640))
        self.widget.setObjectName("widget")
        self.size_box = QtWidgets.QSpinBox(edit_widget)
        self.size_box.setGeometry(QtCore.QRect(300, 680, 60, 30))
        self.size_box.setMaximum(60)
        self.size_box.setObjectName("size_box")
        self.done_button = QtWidgets.QPushButton(edit_widget)
        self.done_button.setGeometry(QtCore.QRect(1180, 680, 90, 30))
        self.done_button.setObjectName("done_button")
        self.done_button.clicked.connect(self.done_clicked)

        self.retranslateUi(edit_widget)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(edit_widget)

    def retranslateUi(self, edit_widget):
        _translate = QtCore.QCoreApplication.translate
        edit_widget.setWindowTitle(_translate("edit_widget", "Interactive Widget"))
        self.brush_label.setText(_translate("edit_widget", "Back Ground"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.draw_tab), _translate("edit_widget", "Draw Table"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.info_tab), _translate("edit_widget", "Brush Info"))
        self.done_button.setText(_translate("edit_widget", "Done"))
    
    def done_clicked(self):
        print('Done Clicked')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_widget = QtWidgets.QWidget()
    ui = Ui_edit_widget()
    ui.setupUi(edit_widget)
    edit_widget.show()
    sys.exit(app.exec_())

