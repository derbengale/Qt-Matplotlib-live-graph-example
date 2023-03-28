# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

from components.mplwidget import MplWidget

class Ui_Fogster2000(object):
    def setupUi(self, Fogster2000):
        if not Fogster2000.objectName():
            Fogster2000.setObjectName(u"Fogster2000")
        Fogster2000.resize(1640, 937)
        self.centralwidget = QWidget(Fogster2000)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Harlow Solid Italic"])
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.selector = QComboBox(self.centralwidget)
        self.selector.addItem("")
        self.selector.addItem("")
        self.selector.addItem("")
        self.selector.setObjectName(u"selector")
        self.selector.setFont(font)

        self.verticalLayout_6.addWidget(self.selector)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Harlow Solid Italic"])
        font1.setPointSize(45)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.s_temp = QSlider(self.frame)
        self.s_temp.setObjectName(u"s_temp")
        self.s_temp.setMinimumSize(QSize(198, 30))
        self.s_temp.setCursor(QCursor(Qt.CrossCursor))
        self.s_temp.setMaximum(235)
        self.s_temp.setPageStep(20)
        self.s_temp.setOrientation(Qt.Horizontal)
        self.s_temp.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout.addWidget(self.s_temp)

        self.v_temp = QLabel(self.frame)
        self.v_temp.setObjectName(u"v_temp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.v_temp.sizePolicy().hasHeightForWidth())
        self.v_temp.setSizePolicy(sizePolicy1)
        self.v_temp.setMinimumSize(QSize(100, 0))
        self.v_temp.setMaximumSize(QSize(260, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Harlow Solid Italic"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.v_temp.setFont(font2)
        self.v_temp.setFrameShape(QFrame.Box)
        self.v_temp.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.v_temp)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.s_dur = QSlider(self.frame_2)
        self.s_dur.setObjectName(u"s_dur")
        self.s_dur.setMinimumSize(QSize(198, 30))
        self.s_dur.setCursor(QCursor(Qt.CrossCursor))
        self.s_dur.setMinimum(1)
        self.s_dur.setMaximum(200)
        self.s_dur.setPageStep(20)
        self.s_dur.setOrientation(Qt.Horizontal)
        self.s_dur.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_2.addWidget(self.s_dur)

        self.v_dur = QLabel(self.frame_2)
        self.v_dur.setObjectName(u"v_dur")
        sizePolicy1.setHeightForWidth(self.v_dur.sizePolicy().hasHeightForWidth())
        self.v_dur.setSizePolicy(sizePolicy1)
        self.v_dur.setMinimumSize(QSize(100, 0))
        self.v_dur.setMaximumSize(QSize(260, 16777215))
        self.v_dur.setFont(font2)
        self.v_dur.setFrameShape(QFrame.Box)
        self.v_dur.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.v_dur)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.s_pow = QSlider(self.frame_4)
        self.s_pow.setObjectName(u"s_pow")
        self.s_pow.setMinimumSize(QSize(198, 30))
        self.s_pow.setCursor(QCursor(Qt.CrossCursor))
        self.s_pow.setMinimum(10)
        self.s_pow.setMaximum(100)
        self.s_pow.setPageStep(20)
        self.s_pow.setTracking(True)
        self.s_pow.setOrientation(Qt.Horizontal)
        self.s_pow.setInvertedAppearance(False)
        self.s_pow.setInvertedControls(False)
        self.s_pow.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_4.addWidget(self.s_pow)

        self.v_pow = QLabel(self.frame_4)
        self.v_pow.setObjectName(u"v_pow")
        sizePolicy1.setHeightForWidth(self.v_pow.sizePolicy().hasHeightForWidth())
        self.v_pow.setSizePolicy(sizePolicy1)
        self.v_pow.setMinimumSize(QSize(100, 0))
        self.v_pow.setMaximumSize(QSize(260, 16777215))
        self.v_pow.setFont(font2)
        self.v_pow.setFrameShape(QFrame.Box)
        self.v_pow.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.v_pow)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.s_interv = QSlider(self.frame_3)
        self.s_interv.setObjectName(u"s_interv")
        self.s_interv.setMinimumSize(QSize(198, 30))
        self.s_interv.setCursor(QCursor(Qt.CrossCursor))
        self.s_interv.setAutoFillBackground(False)
        self.s_interv.setMinimum(1)
        self.s_interv.setMaximum(200)
        self.s_interv.setPageStep(20)
        self.s_interv.setOrientation(Qt.Horizontal)
        self.s_interv.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_3.addWidget(self.s_interv)

        self.v_interv = QLabel(self.frame_3)
        self.v_interv.setObjectName(u"v_interv")
        sizePolicy1.setHeightForWidth(self.v_interv.sizePolicy().hasHeightForWidth())
        self.v_interv.setSizePolicy(sizePolicy1)
        self.v_interv.setMinimumSize(QSize(100, 0))
        self.v_interv.setMaximumSize(QSize(260, 16777215))
        self.v_interv.setFont(font2)
        self.v_interv.setFrameShape(QFrame.Box)
        self.v_interv.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.v_interv)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.plot = MplWidget(self.centralwidget)
        self.plot.setObjectName(u"plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy2)
        self.plot.setMinimumSize(QSize(800, 0))
        self.plot.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.plot)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.b_shoot = QPushButton(self.centralwidget)
        self.b_shoot.setObjectName(u"b_shoot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.b_shoot.sizePolicy().hasHeightForWidth())
        self.b_shoot.setSizePolicy(sizePolicy3)
        self.b_shoot.setMinimumSize(QSize(0, 123))
        font3 = QFont()
        font3.setFamilies([u"Harlow Solid Italic"])
        font3.setPointSize(35)
        self.b_shoot.setFont(font3)
        self.b_shoot.setStyleSheet(u"QPushButton#b_shoot{\n"
"    background-color: lime;\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton#b_shoot:hover {\n"
"    background-color: springgreen;\n"
"}\n"
"\n"
"QPushButton#b_shoot:pressed {\n"
"    background-color: cyan;     \n"
"}\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.b_shoot)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        Fogster2000.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Fogster2000)
        self.statusbar.setObjectName(u"statusbar")
        Fogster2000.setStatusBar(self.statusbar)

        self.retranslateUi(Fogster2000)

        QMetaObject.connectSlotsByName(Fogster2000)
    # setupUi

    def retranslateUi(self, Fogster2000):
        Fogster2000.setWindowTitle(QCoreApplication.translate("Fogster2000", u"Fogster2000", None))
        self.label_2.setText(QCoreApplication.translate("Fogster2000", u"Select Behaviour", None))
        self.selector.setItemText(0, QCoreApplication.translate("Fogster2000", u"Manual Control", None))
        self.selector.setItemText(1, QCoreApplication.translate("Fogster2000", u"Shoot in Intervals", None))
        self.selector.setItemText(2, QCoreApplication.translate("Fogster2000", u"Shoot Continuously", None))

        self.label.setText(QCoreApplication.translate("Fogster2000", u"Temperature", None))
        self.v_temp.setText(QCoreApplication.translate("Fogster2000", u"220 \u00b0C", None))
        self.label_3.setText(QCoreApplication.translate("Fogster2000", u"Shot Duration", None))
        self.v_dur.setText(QCoreApplication.translate("Fogster2000", u"10.0 sec", None))
        self.label_10.setText(QCoreApplication.translate("Fogster2000", u"Pump Power", None))
        self.v_pow.setText(QCoreApplication.translate("Fogster2000", u"100 %", None))
        self.label_4.setText(QCoreApplication.translate("Fogster2000", u"Interval", None))
        self.v_interv.setText(QCoreApplication.translate("Fogster2000", u"10 min", None))
        self.b_shoot.setText(QCoreApplication.translate("Fogster2000", u"Shoot", None))
    # retranslateUi

