from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main_funcs.thread_class.delete_result_class import *
from main_funcs.thread_class.create_plan_class import *

import sys
from datetime import datetime


class SideGrip(QWidget):
    def __init__(self, parent, edge):
        QWidget.__init__(self, parent)
        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None
        
class ProgressDialogUi(QDialog):
    def __init__(self):
        super(ProgressDialogUi, self).__init__()
        uic.loadUi('./data/gui_data/progress_bar_dialog.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()
        
class PlanDeleteConfirmationDialogUi(QDialog):
    def __init__(self):
        super(PlanDeleteConfirmationDialogUi, self).__init__()
        uic.loadUi('./data/gui_data/confirmation.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.test_type.setVisible(False)
        self.btn_delete_plan.clicked.connect(self.delete_plan)
        self.btn_cancel.clicked.connect(self.close)
        
    def delete_plan(self):
        self.thread = DeletePlanClass(parent = None, index = 0)
        self.thread.plan_date = self.date.text()
        self.thread.plan_school = self.inst.text()
        self.thread.start()
        self.close()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()

class ResultDeleteConfirmationDialogUi(QDialog):
    def __init__(self):
        super(ResultDeleteConfirmationDialogUi, self).__init__()
        uic.loadUi('./data/gui_data/confirmation.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.test_type.setVisible(False)
        self.selected_list.setVisible(False)
        self.btn_delete_plan.clicked.connect(self.delete_result)
        self.btn_cancel.clicked.connect(self.close)
        
    def delete_result(self):
        self.thread = DeleteSchoolResultClass(parent = None, index = 0)
        self.thread.main_date = self.date.text()
        self.thread.institution = self.inst.text()
        self.thread.test_type = self.test_type.text()
        self.thread.start()
        self.close()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()

class SelectedResultDeleteConfirmationDialogUi(QDialog):
    def __init__(self):
        super(SelectedResultDeleteConfirmationDialogUi, self).__init__()
        uic.loadUi('./data/gui_data/confirmation.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.test_type.setVisible(False)
        self.selected_list.setVisible(False)
        self.btn_delete_plan.clicked.connect(self.delete_result)
        self.btn_cancel.clicked.connect(self.close)
        
    def delete_result(self):
        self.thread = DeleteSelectedResultClass(parent = None, index = 0)
        self.thread.main_date = self.date.text()
        self.thread.institution = self.inst.text()
        self.thread.test_type = self.test_type.text()
        self.thread.main_list = self.selected_list.text()
        self.thread.start()
        self.close()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end
    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()

class ChangeSchoolNameConfirmationDialogUi(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        uic.loadUi('./data/gui_data/confirmation_change_school_name.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_apply.clicked.connect(self.apply_process)
        self.btn_apply.clicked.connect(self.apply_process)
        self.btn_cancel.clicked.connect(self.cancel)
        
        
    def apply_process(self):
        super().accept()
        self.close()
    
    def cancel(self):
        self.close()


    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()
        
class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        self.completer.popup().setFixedHeight(150)
        self.completer.popup().setStyleSheet("""
                                            /* SCROLL BARS */
                                            QScrollBar:horizontal {
                                                border: none;
                                                background: rgb(52, 59, 72);
                                                height: 14px;
                                                margin: 0px 21px 0 21px;
                                                border-radius: 0px;
                                            }
                                            QScrollBar::handle:horizontal {
                                                background: rgb(85, 170, 255);
                                                min-width: 25px;
                                                border-radius: 7px
                                            }
                                            QScrollBar::add-line:horizontal {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                width: 20px;
                                                border-top-right-radius: 7px;
                                                border-bottom-right-radius: 7px;
                                                subcontrol-position: right;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::sub-line:horizontal {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                width: 20px;
                                                border-top-left-radius: 7px;
                                                border-bottom-left-radius: 7px;
                                                subcontrol-position: left;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
                                            {
                                                background: none;
                                            }
                                            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
                                            {
                                                background: none;
                                            }
                                            QScrollBar:vertical {
                                                border: none;
                                                background: rgb(52, 59, 72);
                                                width: 14px;
                                                margin: 21px 0 21px 0;
                                                border-radius: 0px;
                                            }
                                            QScrollBar::handle:vertical {	
                                                background: rgb(85, 170, 255);
                                                min-height: 25px;
                                                border-radius: 7px
                                            }
                                            QScrollBar::add-line:vertical {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                height: 20px;
                                                border-bottom-left-radius: 7px;
                                                border-bottom-right-radius: 7px;
                                                subcontrol-position: bottom;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::sub-line:vertical {
                                                border: none;
                                                background: rgb(55, 63, 77);
                                                height: 20px;
                                                border-top-left-radius: 7px;
                                                border-top-right-radius: 7px;
                                                subcontrol-position: top;
                                                subcontrol-origin: margin;
                                            }
                                            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                                background: none;
                                            }

                                            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                                background: none;
                                            }

                                            QAbstractScrollArea{
                                                color: rgb(85, 170, 255);	
                                                background-color: rgb(39, 44, 54);
                                                border: 1px solid rgb(27, 29, 35);
                                                padding: 10px;
                                                selection-background-color: rgb(39, 44, 54);
                                            }
                                            """)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

        self.setStyleSheet("""
                           QComboBox {
                                border: 2px solid rgb(52, 59, 72);
                                border-radius: 5px;	
                                background-color: rgb(52, 59, 72);
                            }
                            QComboBox:hover {
                                background-color: rgb(52, 59, 72);
                                border: 2px solid rgb(61, 70, 86);
                            }
                            QComboBox:pressed {	
                                background-color: rgb(35, 40, 49);
                                border: 2px solid rgb(43, 50, 61);
                            }
                            QComboBox::editable{
                                background-color: rgb(52, 59, 72);
                            }
                            """)
        self.view().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.ShortcutOverride:
            if event.key() == Qt.Key_Tab:
                self.hidePopup()
                self.setCurrentIndex(self.view().currentIndex().row())
                return True
        return QComboBox.eventFilter(self, obj, event)
    
        
    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)    


def logger():
    import logging, sys, traceback
    logger = logging.getLogger('logger')
    fh = logging.FileHandler('./gto.log')
    logger.addHandler(fh)
    def exc_handler(exctype, value, tb):
        logger.exception(''.join(traceback.format_exception(exctype, value, tb)))
    sys.excepthook = exc_handler


#################################################################################
#Title Bar START
def all_size_down(self):
    font_size = 10
    height = 30
    fi = -1
    hi = -10
    self.setStyleSheet('.QLabel { font-size: '+str(font_size+fi)+'pt;}.QPushButton { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QComboBox { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi-10)+'px}.QDateEdit { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QRadioButton { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QLineEdit { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QTableWidget { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}')

def all_size_up(self):
    font_size = 10
    height = 30
    fi = 1
    hi = 10
    self.setStyleSheet('.QLabel { font-size: '+str(font_size+fi)+'pt;}.QPushButton { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QComboBox { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi-10)+'px}.QDateEdit { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QRadioButton { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QLineEdit { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}.QTableWidget { font-size: '+str(font_size+fi)+'pt; height: '+str(height+hi)+'px}')

def all_size_normal(self):
    self.setStyleSheet("")

def mousePressEvent(self, event):
    if not self.isMaximized():
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

def mouseMoveEvent(self, event):
    if not self.isMaximized():
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end
        
def mouseReleaseEvent(self, QMouseEvent):
    self.pressing = False

def btn_close_clicked(self):
    self.close()

def btn_max_clicked(self):
    self.showMaximized()
    self.btn_max.hide()
    self.btn_maxr.show()
    
def btn_min_clicked(self):
    self.showMinimized()
    
def btn_maxr_clicked(self):
    self.showNormal()
    self.btn_maxr.hide()
    self.btn_max.show()

def windowStateChanged(self, state):
    self.btn_maxr.setVisible(state == Qt.WindowMaximized)
    self.btn_max.setVisible(state != Qt.WindowMaximized)
    self.btn_maxr.setVisible(state != Qt.WindowMinimized)
    self.btn_max.setVisible(state == Qt.WindowMinimized)
    
def changeEvent(self, event):
    if event.type() == event.WindowStateChange:
        self.windowStateChanged(self.windowState())

@property
def gripSize(self):
    return self._gripSize

def setGripSize(self, size):
    if size == self._gripSize:
        return
    self._gripSize = max(2, size)
    self.updateGrips()

def updateGrips(self):
    outRect = self.rect()
    # an "inner" rect used for reference to set the geometries of size grips
    inRect = outRect.adjusted(2, 2, -2, -2)
    # top left
    self.cornerGrips[0].setGeometry(
        QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
    # top right
    self.cornerGrips[1].setGeometry(
        QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
    # bottom right
    self.cornerGrips[2].setGeometry(
        QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
    # bottom left
    self.cornerGrips[3].setGeometry(
        QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

    # left edge
    self.sideGrips[0].setGeometry(
        0, inRect.top(), self.gripSize, inRect.height())
    # top edge
    self.sideGrips[1].setGeometry(
        inRect.left(), 0, inRect.width(), self.gripSize)
    # right edge
    self.sideGrips[2].setGeometry(
        inRect.left() + inRect.width(), 
        inRect.top(), self.gripSize, inRect.height())
    # bottom edge
    self.sideGrips[3].setGeometry(
        self.gripSize, inRect.top() + inRect.height(), 
        inRect.width(), self.gripSize)

    [grip.raise_() for grip in self.sideGrips + self.cornerGrips]

def resizeEvent(self, event):
    QMainWindow.resizeEvent(self, event)
    self.updateGrips()
#Title Bar END
#################################################################################