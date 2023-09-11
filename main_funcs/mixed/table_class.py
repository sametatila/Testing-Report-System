from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd

from main_funcs.mixed.gui_classes import ExtendedComboBox
    
class PandasModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()
        self.bolds = dict()
        
    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                try:
                    label = self._df.columns.tolist()[section].replace('_',' ').title()
                    return label
                except (IndexError,):
                    return QVariant()
            elif role == Qt.FontRole:
                return self.bolds.get(section, QVariant())
        return QVariant()
    
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self._df.iloc[row][column]
            return value


    def setData(self, index, value, role = Qt.EditRole):
        return False


    def rowCount(self, parent=QModelIndex()):
        return len(self._df.index)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(
            colname, ascending=order == Qt.AscendingOrder, inplace=True
        )
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()
        

class CheckablePandasModel(PandasModel):
    checklist_sig = pyqtSignal(object)
    def __init__(self, df=pd.DataFrame(), parent=None):
        super().__init__(df, parent)
        self.checkable_values = set()
        self._checkable_column = -1

    @property
    def checkable_column(self):
        return self._checkable_column

    @checkable_column.setter
    def checkable_column(self, column):
        if self.checkable_column == column:
            return
        last_column = self.checkable_column
        self._checkable_column = column

        if last_column == -1:
            self.beginInsertColumns(
                QModelIndex(), self.checkable_column, self.checkable_column
            )
            self.endInsertColumns()

        elif self.checkable_column == -1:
            self.beginRemoveColumns(QModelIndex(), last_column, last_column)
            self.endRemoveColumns()
        for c in (last_column, column):
            if c > 0:
                self.dataChanged.emit(
                    self.index(0, c), self.index(self.columnCount() - 1, c)
                )

    def columnCount(self, parent=QModelIndex()):
        return super().columnCount(parent) + (1 if self.checkable_column != -1 else 0)

    def data(self, index, role=Qt.DisplayRole):
        if self.checkable_column != -1:
            row, col = index.row(), index.column()
            if col == self.checkable_column:
                if role == Qt.CheckStateRole:
                    return (
                        Qt.Checked
                        if row in self.checkable_values
                        else Qt.Unchecked
                    )
                return QVariant()
            if col > self.checkable_column:
                index = index.sibling(index.row(), col - 1)
        
        return super().data(index, role)

    def setData(self, index, value, role):
        if self.checkable_column != -1:
            row, col = index.row(), index.column()
            if col == self.checkable_column:
                if role == Qt.CheckStateRole:
                    if row in self.checkable_values:
                        self.checkable_values.discard(row)
                    else:
                        self.checkable_values.add(row)
                    self.checklist_sig.emit(self.checkable_values)
                    self.dataChanged.emit(index, index, (role,))
                    return True
                return False
            if col > self.checkable_column:
                index = index.sibling(index.row(), col - 1)
        return super().setData(index, value, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if self.checkable_column != -1:
            if section == self.checkable_column and orientation == Qt.Horizontal:
                return QVariant()
            if section > self.checkable_column and orientation == Qt.Horizontal:
                section -= 1
        return super().headerData(section, orientation, role)

    def flags(self, index):
        if self.checkable_column != -1:
            col = index.column()
            if col == self.checkable_column:
                return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled 
            if col > self.checkable_column:
                index = index.sibling(index.row(), col - 1)
        return super().flags(index) | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

class Delegate(QItemDelegate):
    def __init__(self, owner, choices):
        super().__init__(owner)
        self.items = choices
    def createEditor(self, parent, option, index):
        self.editor = ExtendedComboBox(parent)
        self.editor.addItems(self.items)
        return self.editor
    def paint(self, painter, option, index):
        value = index.data(Qt.DisplayRole)
        style = QApplication.style()
        opt = QStyleOptionComboBox()
        opt.text = str(value)
        opt.rect = option.rect
        style.drawComplexControl(QStyle.CC_ComboBox, opt, painter)
        QItemDelegate.paint(self, painter, option, index)
    def setEditorData(self, editor, index):
        value = index.data(Qt.DisplayRole)
        num = self.items.index(value)
        editor.setCurrentIndex(num)
    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, Qt.DisplayRole, QVariant(value))
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)