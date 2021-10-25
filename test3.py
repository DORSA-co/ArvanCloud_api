# import sys
# from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
# from PyQt5.QtGui import QIcon

# class App(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 file system view - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
    
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
        
#         self.model = QFileSystemModel()
#         self.model.setRootPath('')
#         self.tree = QTreeView()
#         self.tree.setModel(self.model)
        
#         self.tree.setAnimated(False)
#         self.tree.setIndentation(20)
#         self.tree.setSortingEnabled(True)
        
#         self.tree.setWindowTitle("Dir View")
#         self.tree.resize(640, 480)
        
#         windowLayout = QVBoxLayout()
#         windowLayout.addWidget(self.tree)
#         self.setLayout(windowLayout)
        
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

from PyQt5 import QtWidgets
import sys


class MyScrollWidget(QtWidgets.QWidget):

    def __init__(self):
        super(MyScrollWidget, self).__init__()

        scrollArea = QtWidgets.QScrollArea(self)
        top_widget = QtWidgets.QWidget()
        top_layout = QtWidgets.QVBoxLayout()
        for i in range(10):
            group_box = QtWidgets.QGroupBox()

            group_box.setTitle('GroupBox For Item {0}'.format(i))

            layout = QtWidgets.QHBoxLayout(group_box)

            label = QtWidgets.QLabel()
            label.setText('Label For Item {0}'.format(i))
            layout.addWidget(label)

            push_button = QtWidgets.QPushButton(group_box)
            push_button.setText('Run Button')
            push_button.setFixedSize(100, 32)
            layout.addWidget(push_button)

            group_box.setLayout(layout)
            top_layout.addWidget(group_box)

        top_widget.setLayout(top_layout)
        scrollArea.setWidget(top_widget)
        self.resize(200, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyScrollWidget()
    widget.show()
    sys.exit(app.exec_())