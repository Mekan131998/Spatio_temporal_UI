# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STC_measurement.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 977)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 60, 331, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(18, 18))
        self.tabWidget.setObjectName("tabWidget")
        self.camera_tab = QtWidgets.QWidget()
        self.camera_tab.setObjectName("camera_tab")
        self.widget = QtWidgets.QWidget(self.camera_tab)
        self.widget.setGeometry(QtCore.QRect(18, 18, 291, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.init_camera_button = QtWidgets.QPushButton(self.widget)
        self.init_camera_button.setObjectName("init_camera_button")
        self.gridLayout_5.addWidget(self.init_camera_button, 0, 0, 1, 1)
        self.live_button = QtWidgets.QPushButton(self.widget)
        self.live_button.setObjectName("live_button")
        self.gridLayout_5.addWidget(self.live_button, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.exposure_line_edit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exposure_line_edit.setFont(font)
        self.exposure_line_edit.setText("")
        self.exposure_line_edit.setObjectName("exposure_line_edit")
        self.gridLayout_5.addWidget(self.exposure_line_edit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.average_edit = QtWidgets.QSpinBox(self.widget)
        self.average_edit.setObjectName("average_edit")
        self.gridLayout_5.addWidget(self.average_edit, 2, 1, 1, 1)
        self.back_subtract_button = QtWidgets.QPushButton(self.widget)
        self.back_subtract_button.setObjectName("back_subtract_button")
        self.gridLayout_5.addWidget(self.back_subtract_button, 3, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.bin10_check_button = QtWidgets.QCheckBox(self.widget)
        self.bin10_check_button.setObjectName("bin10_check_button")
        self.gridLayout_6.addWidget(self.bin10_check_button, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.one_radio = QtWidgets.QRadioButton(self.groupBox)
        self.one_radio.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.one_radio.setObjectName("one_radio")
        self.one_over_2_radio = QtWidgets.QRadioButton(self.groupBox)
        self.one_over_2_radio.setGeometry(QtCore.QRect(80, 30, 51, 17))
        self.one_over_2_radio.setObjectName("one_over_2_radio")
        self.over_4_radio = QtWidgets.QRadioButton(self.groupBox)
        self.over_4_radio.setGeometry(QtCore.QRect(140, 30, 51, 17))
        self.over_4_radio.setObjectName("over_4_radio")
        self.over_8_radio = QtWidgets.QRadioButton(self.groupBox)
        self.over_8_radio.setGeometry(QtCore.QRect(200, 30, 51, 17))
        self.over_8_radio.setObjectName("over_8_radio")
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 2)
        self.bin_cam_push = QtWidgets.QPushButton(self.widget)
        self.bin_cam_push.setObjectName("bin_cam_push")
        self.gridLayout_6.addWidget(self.bin_cam_push, 2, 0, 1, 1)
        self.trigger_push = QtWidgets.QPushButton(self.widget)
        self.trigger_push.setObjectName("trigger_push")
        self.gridLayout_6.addWidget(self.trigger_push, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.camera_tab, "")
        self.stage_tab = QtWidgets.QWidget()
        self.stage_tab.setObjectName("stage_tab")
        self.widget1 = QtWidgets.QWidget(self.stage_tab)
        self.widget1.setGeometry(QtCore.QRect(18, 14, 291, 331))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.stage_init = QtWidgets.QPushButton(self.widget1, clicked=lambda: self.stage_init_fun())
        self.stage_init.setObjectName("stage_init")
        self.gridLayout.addWidget(self.stage_init, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.closed_open_combo = QtWidgets.QComboBox(self.widget1)
        self.closed_open_combo.setObjectName("closed_open_combo")
        self.closed_open_combo.addItem("")
        self.closed_open_combo.addItem("")
        self.gridLayout.addWidget(self.closed_open_combo, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.set_pos_inline = QtWidgets.QLineEdit(self.widget1)
        self.set_pos_inline.setInputMethodHints(QtCore.Qt.ImhNone)
        self.set_pos_inline.setObjectName("set_pos_inline")
        self.gridLayout.addWidget(self.set_pos_inline, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.actual_pos_inline = QtWidgets.QLineEdit(self.widget1)
        self.actual_pos_inline.setReadOnly(True)
        self.actual_pos_inline.setObjectName("actual_pos_inline")
        self.gridLayout.addWidget(self.actual_pos_inline, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget2.setGeometry(QtCore.QRect(11, 31, 131, 89))
        self.widget2.setObjectName("widget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.kp_inline = QtWidgets.QLineEdit(self.widget2)
        self.kp_inline.setObjectName("kp_inline")
        self.gridLayout_2.addWidget(self.kp_inline, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.kd_inline = QtWidgets.QLineEdit(self.widget2)
        self.kd_inline.setObjectName("kd_inline")
        self.gridLayout_2.addWidget(self.kd_inline, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.ki_inline = QtWidgets.QLineEdit(self.widget2)
        self.ki_inline.setObjectName("ki_inline")
        self.gridLayout_2.addWidget(self.ki_inline, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.stage_tab, "")
        self.scan_tab = QtWidgets.QWidget()
        self.scan_tab.setObjectName("scan_tab")
        self.widget3 = QtWidgets.QWidget(self.scan_tab)
        self.widget3.setGeometry(QtCore.QRect(21, 25, 281, 331))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.ref_pos_inline_edit = QtWidgets.QLineEdit(self.widget3)
        self.ref_pos_inline_edit.setObjectName("ref_pos_inline_edit")
        self.gridLayout_3.addWidget(self.ref_pos_inline_edit, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.span_inline_edit = QtWidgets.QLineEdit(self.widget3)
        self.span_inline_edit.setObjectName("span_inline_edit")
        self.gridLayout_3.addWidget(self.span_inline_edit, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.num_of_points_inline = QtWidgets.QLineEdit(self.widget3)
        self.num_of_points_inline.setObjectName("num_of_points_inline")
        self.gridLayout_3.addWidget(self.num_of_points_inline, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.information_label = QtWidgets.QLabel(self.groupBox_3)
        self.information_label.setGeometry(QtCore.QRect(10, 20, 261, 71))
        self.information_label.setText("")
        self.information_label.setObjectName("information_label")
        self.gridLayout_3.addWidget(self.groupBox_3, 3, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scan_stage_only_button = QtWidgets.QPushButton(self.widget3)
        self.scan_stage_only_button.setObjectName("scan_stage_only_button")
        self.gridLayout_7.addWidget(self.scan_stage_only_button, 0, 0, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.widget3)
        self.save_button.setObjectName("save_button")
        self.gridLayout_7.addWidget(self.save_button, 0, 1, 1, 1)
        self.workspace_button = QtWidgets.QPushButton(self.widget3)
        self.workspace_button.setObjectName("workspace_button")
        self.gridLayout_7.addWidget(self.workspace_button, 1, 1, 1, 1)
        self.saveH5_button = QtWidgets.QPushButton(self.widget3)
        self.saveH5_button.setObjectName("saveH5_button")
        self.gridLayout_7.addWidget(self.saveH5_button, 2, 1, 1, 1)
        self.scan_button = QtWidgets.QPushButton(self.widget3)
        self.scan_button.setObjectName("scan_button")
        self.gridLayout_7.addWidget(self.scan_button, 1, 0, 2, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.tabWidget.addTab(self.scan_tab, "")
        self.camera_image_widget = QtWidgets.QWidget(self.centralwidget)
        self.camera_image_widget.setGeometry(QtCore.QRect(441, 90, 500, 500))
        self.camera_image_widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.camera_image_widget.setObjectName("camera_image_widget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 450, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget4 = QtWidgets.QWidget(self.groupBox_4)
        self.widget4.setGeometry(QtCore.QRect(20, 20, 291, 91))
        self.widget4.setObjectName("widget4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.center_check = QtWidgets.QCheckBox(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.center_check.setFont(font)
        self.center_check.setObjectName("center_check")
        self.gridLayout_4.addWidget(self.center_check, 0, 0, 1, 1)
        self.reset_push = QtWidgets.QPushButton(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_push.setFont(font)
        self.reset_push.setObjectName("reset_push")
        self.gridLayout_4.addWidget(self.reset_push, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.x_inline_edit = QtWidgets.QLineEdit(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x_inline_edit.setFont(font)
        self.x_inline_edit.setText("")
        self.x_inline_edit.setObjectName("x_inline_edit")
        self.gridLayout_4.addWidget(self.x_inline_edit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.y_inline_edit = QtWidgets.QLineEdit(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y_inline_edit.setFont(font)
        self.y_inline_edit.setObjectName("y_inline_edit")
        self.gridLayout_4.addWidget(self.y_inline_edit, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 0, 931, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.signal_widget = QtWidgets.QWidget(self.centralwidget)
        self.signal_widget.setGeometry(QtCore.QRect(10, 623, 462, 272))
        self.signal_widget.setStyleSheet("background-color: rgb(247, 255, 216);")
        self.signal_widget.setObjectName("signal_widget")
        self.spectrum_widget = QtWidgets.QWidget(self.centralwidget)
        self.spectrum_widget.setGeometry(QtCore.QRect(480, 623, 462, 272))
        self.spectrum_widget.setStyleSheet("background-color: rgb(229, 255, 220);")
        self.spectrum_widget.setObjectName("spectrum_widget")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 600, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(480, 600, 462, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(480, 68, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # START_FUN:
    # initialize the stage function:
    def stage_init_fun(self):
        if self.stage_init.text()=='Initialize':
            self.stage_init.setText('Initialized')
            self.stage_init.setStyleSheet("background-color: #005500; color: white")
        else:
            self.stage_init.setText('Initialize')
            self.stage_init.setStyleSheet("background-color: #e1e1e1; color: black")

       


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.init_camera_button.setText(_translate("MainWindow", "Initialize"))
        self.live_button.setText(_translate("MainWindow", "Live"))
        self.label.setText(_translate("MainWindow", "Exposure (ms)"))
        self.label_2.setText(_translate("MainWindow", "Average"))
        self.back_subtract_button.setText(_translate("MainWindow", "Background subtraction"))
        self.bin10_check_button.setText(_translate("MainWindow", "Bin10"))
        self.groupBox.setTitle(_translate("MainWindow", "AOI"))
        self.one_radio.setText(_translate("MainWindow", "1"))
        self.one_over_2_radio.setText(_translate("MainWindow", "1/2"))
        self.over_4_radio.setText(_translate("MainWindow", "1/4"))
        self.over_8_radio.setText(_translate("MainWindow", "1/8"))
        self.bin_cam_push.setText(_translate("MainWindow", "Bin Cam"))
        self.trigger_push.setText(_translate("MainWindow", "Trigger"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camera_tab), _translate("MainWindow", "Camera"))
        self.stage_init.setText(_translate("MainWindow", "Initialize"))
        self.label_5.setText(_translate("MainWindow", "Loop type"))
        self.closed_open_combo.setItemText(0, _translate("MainWindow", "Closed Loop"))
        self.closed_open_combo.setItemText(1, _translate("MainWindow", "Open Loop "))
        self.label_6.setText(_translate("MainWindow", "Stage position"))
        self.label_7.setText(_translate("MainWindow", "Actual position"))
        self.groupBox_2.setTitle(_translate("MainWindow", "PID settings"))
        self.label_8.setText(_translate("MainWindow", "kp"))
        self.label_9.setText(_translate("MainWindow", "kd"))
        self.label_10.setText(_translate("MainWindow", "ki"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stage_tab), _translate("MainWindow", "Stage"))
        self.label_11.setText(_translate("MainWindow", "Ref. pos. (um)"))
        self.label_12.setText(_translate("MainWindow", "Span (fs/um)"))
        self.label_13.setText(_translate("MainWindow", "Num. of points"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Info"))
        self.scan_stage_only_button.setText(_translate("MainWindow", "Scan stage only "))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.workspace_button.setText(_translate("MainWindow", "To workspace"))
        self.saveH5_button.setText(_translate("MainWindow", "Save H5"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_tab), _translate("MainWindow", "Scan"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Pixel position"))
        self.center_check.setText(_translate("MainWindow", "Center mark"))
        self.reset_push.setText(_translate("MainWindow", "Reset Position"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_14.setText(_translate("MainWindow", "STC measurement UI"))
        self.label_15.setText(_translate("MainWindow", "Signal"))
        self.label_16.setText(_translate("MainWindow", "Spectrum"))
        self.label_17.setText(_translate("MainWindow", "Camera Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
