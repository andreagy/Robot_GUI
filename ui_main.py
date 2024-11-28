# Form implementation generated from reading ui file 'UI_phase1.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RobotUIApp(object):
    def setupUi(self, RobotUIApp):
        RobotUIApp.setObjectName("RobotUIApp")
        RobotUIApp.setEnabled(True)
        RobotUIApp.resize(854, 480)
        RobotUIApp.setMinimumSize(QtCore.QSize(640, 480))
        RobotUIApp.setMaximumSize(QtCore.QSize(3840, 2160))
        self.centralwidget = QtWidgets.QWidget(parent=RobotUIApp)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background-color: none;\n"
"}\n"
"\n"
"#verticalLayout {\n"
"    \n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.nav_primary_camera_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nav_primary_camera_label.setGeometry(QtCore.QRect(0, 0, 854, 480))
        self.nav_primary_camera_label.setMinimumSize(QtCore.QSize(854, 480))
        self.nav_primary_camera_label.setMaximumSize(QtCore.QSize(3840, 2160))
        self.nav_primary_camera_label.setStyleSheet("color: rgb(22, 51, 79)")
        self.nav_primary_camera_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.nav_primary_camera_label.setLineWidth(0)
        self.nav_primary_camera_label.setText("")
        self.nav_primary_camera_label.setObjectName("nav_primary_camera_label")
        self.nav_secondary_camera_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nav_secondary_camera_label.setGeometry(QtCore.QRect(30, 30, 220, 140))
        self.nav_secondary_camera_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.nav_secondary_camera_label.setText("")
        self.nav_secondary_camera_label.setObjectName("nav_secondary_camera_label")
        self.speed_display = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.speed_display.setGeometry(QtCore.QRect(270, 420, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.speed_display.setFont(font)
        self.speed_display.setAutoFillBackground(False)
        self.speed_display.setStyleSheet("QLabel {\n"
"    font-family: \'Roboto\', sans-serif;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    background-color: rgb(25, 36, 52);\n"
"    padding: 10px;\n"
"    border: 1.5px solid #e67e22; \n"
"}\n"
"\n"
"QLCDNumber {\n"
"    background-color: rgb(25, 36, 52);\n"
"    color: #ffffff; /* White text */\n"
"    border: 1.5px solid #e67e22; \n"
"    padding: 10px;\n"
"}")
        self.speed_display.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.speed_display.setObjectName("speed_display")
        self.distance_display = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.distance_display.setGeometry(QtCore.QRect(480, 420, 110, 40))
        self.distance_display.setAutoFillBackground(False)
        self.distance_display.setStyleSheet("QLabel {\n"
"    font-family: \'Roboto\', sans-serif;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    background-color: rgb(25, 36, 52);\n"
"    padding: 10px;\n"
"    border: 1.5px solid #e67e22; \n"
"}\n"
"\n"
"QLCDNumber {\n"
"    background-color: rgb(25, 36, 52);\n"
"    color: #ffffff; /* White text */\n"
"    border: 1.5px solid #e67e22; \n"
"    padding: 10px;\n"
"}")
        self.distance_display.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.distance_display.setObjectName("distance_display")
        self.speed_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(270, 390, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        self.speed_label.setFont(font)
        self.speed_label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: NONE;\n"
"}")
        self.speed_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.speed_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.speed_label.setObjectName("speed_label")
        self.distance_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.distance_label.setGeometry(QtCore.QRect(480, 390, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        self.distance_label.setFont(font)
        self.distance_label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: NONE;\n"
"}")
        self.distance_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.distance_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.distance_label.setObjectName("distance_label")
        self.work_secondary_camera_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.work_secondary_camera_label.setGeometry(QtCore.QRect(30, 30, 220, 140))
        self.work_secondary_camera_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.work_secondary_camera_label.setText("")
        self.work_secondary_camera_label.setObjectName("work_secondary_camera_label")
        self.work_primary_camera_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.work_primary_camera_label.setGeometry(QtCore.QRect(0, 0, 854, 480))
        self.work_primary_camera_label.setMinimumSize(QtCore.QSize(854, 480))
        self.work_primary_camera_label.setMaximumSize(QtCore.QSize(3840, 2160))
        self.work_primary_camera_label.setStyleSheet("color: rgb(22, 51, 79)")
        self.work_primary_camera_label.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.work_primary_camera_label.setLineWidth(0)
        self.work_primary_camera_label.setText("")
        self.work_primary_camera_label.setObjectName("work_primary_camera_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(760, 20, 71, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nav_mode_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.nav_mode_button.setStyleSheet("padding: 10px")
        self.nav_mode_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/navigation.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.nav_mode_button.setIcon(icon)
        self.nav_mode_button.setIconSize(QtCore.QSize(35, 35))
        self.nav_mode_button.setObjectName("nav_mode_button")
        self.verticalLayout.addWidget(self.nav_mode_button)
        self.work_mode_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.work_mode_button.setStyleSheet("padding: 10px;")
        self.work_mode_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/work1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.work_mode_button.setIcon(icon1)
        self.work_mode_button.setIconSize(QtCore.QSize(40, 40))
        self.work_mode_button.setObjectName("work_mode_button")
        self.verticalLayout.addWidget(self.work_mode_button)
        self.work_primary_camera_label.raise_()
        self.nav_primary_camera_label.raise_()
        self.nav_secondary_camera_label.raise_()
        self.distance_display.raise_()
        self.distance_label.raise_()
        self.speed_label.raise_()
        self.speed_display.raise_()
        self.verticalLayoutWidget.raise_()
        self.work_secondary_camera_label.raise_()
        RobotUIApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(RobotUIApp)
        QtCore.QMetaObject.connectSlotsByName(RobotUIApp)

    def retranslateUi(self, RobotUIApp):
        _translate = QtCore.QCoreApplication.translate
        RobotUIApp.setWindowTitle(_translate("RobotUIApp", "RobotUI"))
        self.speed_label.setText(_translate("RobotUIApp", "SPEED (m/s)"))
        self.distance_label.setText(_translate("RobotUIApp", "DISTANCE (m)"))
