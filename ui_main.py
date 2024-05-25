# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(542, 447)
        icon = QIcon()
        icon.addFile(u":/icons/icons/ava.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower,\n"
"#btn_upper,\n"
"#btn_digits,\n"
"#btn_special {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: crimson;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid crimson;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: brown;\n"
"    border-color: crimson;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_lock.sizePolicy().hasHeightForWidth())
        self.icon_lock.setSizePolicy(sizePolicy)
        self.icon_lock.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/lock.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(90, 90))

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy1)
        self.frame_password.setTabletTracking(False)
        self.frame_password.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_password.setStyleSheet(u"QFrame {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color:crimson;\n"
"}")
        self.frame_password.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}")

        self.horizontalLayout_2.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        sizePolicy.setHeightForWidth(self.btn_visibility.sizePolicy().hasHeightForWidth())
        self.btn_visibility.setSizePolicy(sizePolicy)
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton{\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/visibility_off.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/visibility on.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(False)

        self.horizontalLayout_2.addWidget(self.btn_visibility)

        self.btn_refresh = QPushButton(self.frame_password)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"    margin-right:0;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.horizontalLayout_2.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.frame_password)
        self.btn_copy.setObjectName(u"btn_copy")
        sizePolicy.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy)
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton{\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.horizontalLayout_2.addWidget(self.btn_copy)


        self.layout_password.addWidget(self.frame_password)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_stenght = QLabel(self.centralwidget)
        self.label_stenght.setObjectName(u"label_stenght")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_stenght.sizePolicy().hasHeightForWidth())
        self.label_stenght.setSizePolicy(sizePolicy2)
        self.label_stenght.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_info.addWidget(self.label_stenght)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy2.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy2)
        self.label_entropy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_lenght = QSlider(self.centralwidget)
        self.slider_lenght.setObjectName(u"slider_lenght")
        self.slider_lenght.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_lenght.setStyleSheet(u"QSlider::groove:horizontal{\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"    background-color: crimson;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background-color: white;\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}")
        self.slider_lenght.setMaximum(100)
        self.slider_lenght.setValue(0)
        self.slider_lenght.setOrientation(Qt.Orientation.Horizontal)

        self.layout_lenght.addWidget(self.slider_lenght)

        self.spinbox_lenght = QSpinBox(self.centralwidget)
        self.spinbox_lenght.setObjectName(u"spinbox_lenght")
        self.spinbox_lenght.setStyleSheet(u"QSpinBox{\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"    border-color: crimson;\n"
"}")
        self.spinbox_lenght.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinbox_lenght.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_lenght.setMaximum(100)

        self.layout_lenght.addWidget(self.spinbox_lenght)


        self.verticalLayout.addLayout(self.layout_lenght)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setCheckable(True)

        self.layout_characters.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
        self.label_stenght.setText("")
        self.label_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"@#!", None))
    # retranslateUi

