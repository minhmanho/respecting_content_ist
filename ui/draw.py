# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import glob
import os
import sys

class ui_edit_widget(object):
    def setupUi(self, edit_widget, image_file, artist, out_dir, auto_update=False):
        self.win_size = 512
        # self.palette = palette
        self.result = None
        self.gray_win = None
        edit_widget.setObjectName("edit_widget")
        edit_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_widget.resize(1024, 600)

        self.groupBox_2 = QtWidgets.QGroupBox(edit_widget)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 160, 331, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.level_1 = QtWidgets.QSlider(self.groupBox_2)
        self.level_1.setGeometry(QtCore.QRect(10, 40, 311, 16))
        self.level_1.setMinimum(0)
        self.level_1.setMaximum(100)
        self.level_1.setOrientation(QtCore.Qt.Horizontal)
        self.level_1.setObjectName("level_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 311, 16))
        self.label_2.setObjectName("label_2")
        self.level_2 = QtWidgets.QSlider(self.groupBox_2)
        self.level_2.setGeometry(QtCore.QRect(10, 90, 311, 16))
        self.level_2.setMinimum(0)
        self.level_2.setMaximum(100)
        self.level_2.setOrientation(QtCore.Qt.Horizontal)
        self.level_2.setObjectName("level_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 311, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 311, 16))
        self.label_5.setObjectName("label_5")
        self.label_1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_1.setGeometry(QtCore.QRect(10, 20, 311, 16))
        self.label_1.setObjectName("label_1")
        self.level_5 = QtWidgets.QSlider(self.groupBox_2)
        self.level_5.setGeometry(QtCore.QRect(10, 240, 311, 16))
        self.level_5.setMinimum(0)
        self.level_5.setMaximum(100)
        self.level_5.setOrientation(QtCore.Qt.Horizontal)
        self.level_5.setObjectName("level_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 311, 16))
        self.label_4.setObjectName("label_4")
        self.level_3 = QtWidgets.QSlider(self.groupBox_2)
        self.level_3.setGeometry(QtCore.QRect(10, 140, 311, 16))
        self.level_3.setMinimum(0)
        self.level_3.setMaximum(100)
        self.level_3.setOrientation(QtCore.Qt.Horizontal)
        self.level_3.setObjectName("level_3")
        self.level_4 = QtWidgets.QSlider(self.groupBox_2)
        self.level_4.setGeometry(QtCore.QRect(10, 190, 311, 16))
        self.level_4.setMinimum(0)
        self.level_4.setMaximum(100)
        self.level_4.setOrientation(QtCore.Qt.Horizontal)
        self.level_4.setObjectName("level_4")
        self.save_button = QtWidgets.QPushButton(edit_widget)
        self.save_button.setGeometry(QtCore.QRect(560, 450, 75, 23))
        self.save_button.setObjectName("save_button")
        self.load_button = QtWidgets.QPushButton(edit_widget)
        self.load_button.setGeometry(QtCore.QRect(640, 450, 75, 23))
        self.load_button.setObjectName("load_button")
        self.update_button = QtWidgets.QPushButton(edit_widget)
        self.update_button.setEnabled(False)
        self.update_button.setGeometry(QtCore.QRect(720, 450, 75, 23))
        self.update_button.setObjectName("update_button")
        self.tabWidget = QtWidgets.QTabWidget(edit_widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 520, 520))
        self.tabWidget.setObjectName("tabWidget")

        self.drawWidget = GUIDraw(artist, out_dir=out_dir)
        self.drawWidget.setObjectName("drawWidget")
        self.tabWidget.addTab(self.drawWidget, "")

        # self.visWidget = GUI_VIS()
        # self.visWidget.setObjectName("visWidget")
        # self.tabWidget.addTab(self.visWidget, "")

        self.save_button.clicked.connect(self.save_clicked)
        self.load_button.clicked.connect(self.load_clicked)
        self.update_button.clicked.connect(self.update_clicked)
        self.level_1.valueChanged[int].connect(self.changeValue_1)
        self.level_2.valueChanged[int].connect(self.changeValue_2)
        self.level_3.valueChanged[int].connect(self.changeValue_3)
        self.level_4.valueChanged[int].connect(self.changeValue_4)
        self.level_5.valueChanged[int].connect(self.changeValue_5)

        self.retranslateUi(edit_widget)
        QtCore.QMetaObject.connectSlotsByName(edit_widget)

        self.drawWidget.init_result(image_file)


        self.handle_update = self.drawWidget.compute_result if auto_update else self.setEnabled_update
        self.auto_update = auto_update
    
    def setEnabled_update(self):
        self.update_button.setEnabled(True)

    # def update_handler(status):
    #     return {
    #         self.drawWidget.compute_result
    #     }

    def changeValue_1(self, value):
        print('Level 1: ' + str(value))
        self.handle_update()
        self.drawWidget.artist.network.connect_weights[0] = value/100

    def changeValue_2(self, value):
        print('Level 2: ' + str(value))
        self.handle_update()
        self.drawWidget.artist.network.connect_weights[1] = value/100
    
    def changeValue_3(self, value):
        print('Level 3: ' + str(value))
        self.handle_update()
        self.drawWidget.artist.network.connect_weights[2] = value/100
    
    def changeValue_4(self, value):
        print('Level 4: ' + str(value))
        self.handle_update()
        self.drawWidget.artist.network.connect_weights[3] = value/100

    def changeValue_5(self, value):
        print('Level 5: ' + str(value))
        self.handle_update()
        self.drawWidget.artist.network.connect_weights[4] = value/100

    def update_clicked(self):
        self.drawWidget.compute_result()
        self.update_button.setEnabled(False)

    def retranslateUi(self, edit_widget):
        _translate = QtCore.QCoreApplication.translate
        edit_widget.setWindowTitle(_translate("edit_widget", "Form"))
        self.groupBox_2.setTitle(_translate("edit_widget", "Features Control Panel"))
        self.label_2.setText(_translate("edit_widget", "Level 2:"))
        self.label_3.setText(_translate("edit_widget", "Level 3:"))
        self.label_5.setText(_translate("edit_widget", "Level 5:"))
        self.label_1.setText(_translate("edit_widget", "Level 1:"))
        self.label_4.setText(_translate("edit_widget", "Level 4:"))
        self.save_button.setText(_translate("edit_widget", "Save"))
        self.load_button.setText(_translate("edit_widget", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drawWidget), _translate("edit_widget", "Interesting Widget"))
        self.update_button.setText(_translate("edit_widget", "Update"))

    def save_clicked(self):
        print('Save Image')
        self.drawWidget.save_result()

    def load_clicked(self):
        print('Load Image')
        self.drawWidget.load_image()

    def done_clicked(self):
        print('Done')
        self.drawWidget.nextImage()

    def skip_clicked(self):
        print('Skip')
        self.drawWidget.nextImage(does_save_result=False)

    def load(self):
        self.drawWidget.load_image()

class GUIDraw(QtWidgets.QWidget):
    def __init__(self, artist, out_dir='images', load_size=512, win_size=512):
        QtWidgets.QWidget.__init__(self)
        self.image_file = None
        self.pos = None
        self.artist = artist
        self.win_size = win_size
        self.load_size = load_size
        self.setFixedSize(win_size, win_size)
        self.move(win_size, win_size)
        self.total_images = 0
        self.image_id = 0
        self.setMouseTracking(True)
        self.out_dir = out_dir

    def init_result(self, image_file):
        self.read_image(image_file)  # read an image .encode('utf-8')
        self.reset()

    def get_batches(self, img_dir):
        self.img_list = glob.glob(os.path.join(img_dir, '*.png'))
        self.total_images = len(self.img_list)
        img_first = self.img_list[0]
        self.init_result(img_first)

    def nextImage(self, does_save_result=True):
        if does_save_result:
            self.save_result()
        self.image_id += 1
        if self.image_id == self.total_images:
            print('you have finished all the results')
            sys.exit()
        img_current = self.img_list[self.image_id]
        # self.reset()
        self.init_result(img_current)

    def save_result(self):
        path = os.path.abspath(self.image_file)
        path, ext = os.path.splitext(path)
        _name = os.path.basename(self.image_file).split('.')[0]

        connect_weights_str = '-'.join([str(int(k*100)) for k in self.artist.network.connect_weights])
        save_path = os.path.join(self.out_dir, _name + '_' + connect_weights_str)

        print('Saving result to <%s>\n' % save_path)
        result_bgr = cv2.cvtColor(self.result, cv2.COLOR_RGB2BGR)
        cv2.imwrite(save_path + '.png', result_bgr)

    def read_image(self, image_file):
        self.image_file = image_file
        print(image_file)
        im_bgr = cv2.resize(cv2.imread(image_file), (512, 512))
        self.im_full = im_bgr.copy()
        # get image for display
        h, w, c = self.im_full.shape
        max_width = max(h, w)
        r = self.win_size / float(max_width)
        self.scale = int(float(self.win_size) / self.load_size)
        print('scale = %f' % self.scale)
        self.rw = int(round(r * w / 4.0) * 4)
        self.rh = int(round(r * h / 4.0) * 4)

        self.im_win = cv2.resize(self.im_full, (self.rw, self.rh), interpolation=cv2.INTER_CUBIC)

        self.dw = int((self.win_size - self.rw) // 2)
        self.dh = int((self.win_size - self.rh) // 2)
        self.win_w = self.rw
        self.win_h = self.rh

        self.im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

    def reset(self):
        print('reset')
        self.pos = None
        self.result = None
        self.compute_result()
        self.update()

    def scale_point(self, pnt):
        x = int((pnt.x() - self.dw) / float(self.win_w) * self.load_size)
        y = int((pnt.y() - self.dh) / float(self.win_h) * self.load_size)
        return x, y

    def valid_point(self, pnt):
        if pnt is None:
            print('WARNING: no point\n')
            return None
        else:
            if pnt.x() >= self.dw and pnt.y() >= self.dh and pnt.x() < self.win_size - self.dw and pnt.y() < self.win_size - self.dh:
                x = int(np.round(pnt.x()))
                y = int(np.round(pnt.y()))
                return QtCore.QPoint(x, y)
            else:
                print('WARNING: invalid point (%d, %d)\n' % (pnt.x(), pnt.y()))
                return None

    def erase(self):
        self.eraseMode = not self.eraseMode

    def load_image(self):
        img_path = QtWidgets.QFileDialog.getOpenFileName(self, 'load an input image')[0]
        self.init_result(img_path)

    def compute_result(self):
        stylized_image = self.artist.stylize(self.im_rgb)
        self.result = stylized_image
        self.update()
    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        im = self.result

        if im is not None:
            qImg = QtGui.QImage(im.tostring(), im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888)
            painter.drawImage(0, 0, qImg)

        painter.end()

class GUI_VIS(QtWidgets.QWidget):
    def __init__(self, win_size=512, scale=4.0):
        QtWidgets.QWidget.__init__(self)
        self.result = None
        self.win_width = win_size
        self.win_height = win_size
        self.scale = scale
        self.setFixedSize(self.win_width, self.win_height)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # painter.fillRect(event.rect(), QColor(49, 54, 49))
        if self.result is not None:
            h, w, c = self.result.shape
            qImg = QtGui.QImage(self.result.tostring(), w, h, QtGui.QImage.Format_RGB888)
            painter.drawImage(0, 0, qImg)

        painter.end()

    def update_result(self, result):
        self.result = result
        self.update()

    def reset(self):
        self.update()
        self.result = None

    def is_valid_point(self, pos):
        if pos is None:
            return False
        else:
            x = pos.x()
            y = pos.y()
            return x >= 0 and y >= 0 and x < self.win_width and y < self.win_height

    def scale_point(self, pnt):
        x = int(pnt.x() / self.scale)
        y = int(pnt.y() / self.scale)
        return x, y

    def mousePressEvent(self, event):
        pos = event.pos()
        x, y = self.scale_point(pos)
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

