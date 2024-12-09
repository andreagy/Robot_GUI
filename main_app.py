import sys
from PyQt6 import QtWidgets, uic
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, Qt
import cv2
import numpy as np

from ui_main import Ui_RobotUIApp


# Class for UI management
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_RobotUIApp()
        self.ui.setupUi(self)

        # Access camera widgets
        """self.nav_primary_camera = self.ui.nav_primary_camera_label
        self.nav_secondary_camera = self.ui.nav_secondary_camera_label
        self.work_primary_camera = self.ui.work_primary_camera_label
        self.work_secondary_camera = self.ui.work_secondary_camera_label"""

        # Flag for camera feed swap
        self.swapped = False

        """
        self.nav_capture_primary = cv2.VideoCapture("http://192.168.2.2:8000/stream.mjpg")  # cv2.VideoCapture("rtsp://192.168.2.2:8554/cam1")
        self.nav_capture_secondary = cv2.VideoCapture("http://192.168.2.2:8001/stream.mjpg")  # cv2.VideoCapture("rtsp://192.168.2.2:8554/cam2")
        self.work_capture_primary = cv2.VideoCapture("http://192.168.2.2:8000/stream.mjpg")  # using this for testing, replace these with the respective camera feed
        self.work_capture_secondary = cv2.VideoCapture("http://192.168.2.2:8001/stream.mjpg")"""

        # Access camera streams
        self.stream1 = CameraStream("http://192.168.2.2:8000/stream.mjpg")
        self.stream2 = CameraStream("http://192.168.2.2:8001/stream.mjpg")
        #self.stream3 = CameraStream("http://192.168.2.2:8000/stream.mjpg")
        #self.stream4 = CameraStream("http://192.168.2.2:8001/stream.mjpg")

        # Replace QLabel for navigation primary camera with CameraWidget
        self.nav_primary_camera_label = CameraWidget(self.stream1, self.ui.nav_primary_camera_label, parent=self.ui.centralwidget)
        self.nav_primary_camera_label.setGeometry(self.ui.nav_primary_camera_label.geometry())
        self.ui.nav_primary_camera_label.deleteLater()
        self.ui.nav_primary_camera_label = self.nav_primary_camera_label

        # Replace QLabel for navigation secondary camera with CameraWidget
        self.nav_secondary_camera_label = CameraWidget(self.stream2, self.ui.nav_primary_camera_label, parent=self.ui.centralwidget)
        self.nav_secondary_camera_label.setGeometry(self.ui.nav_secondary_camera_label.geometry())
        self.ui.nav_secondary_camera_label.deleteLater()
        self.ui.nav_secondary_camera_label = self.nav_secondary_camera_label

        # Replace QLabel for work primary camera with CameraWidget
        self.work_primary_camera_label = CameraWidget(self.stream1, self.ui.nav_primary_camera_label, parent=self.ui.centralwidget)
        self.work_primary_camera_label.setGeometry(self.ui.work_primary_camera_label.geometry())
        self.ui.work_primary_camera_label.deleteLater()
        self.ui.work_primary_camera_label = self.work_primary_camera_label

        # Replace QLabel for work secondary camera with CameraWidget
        self.work_secondary_camera_label = CameraWidget(self.stream2, self.ui.nav_primary_camera_label, parent=self.ui.centralwidget)
        self.work_secondary_camera_label.setGeometry(self.ui.work_secondary_camera_label.geometry())
        self.ui.work_secondary_camera_label.deleteLater()
        self.ui.work_secondary_camera_label = self.work_secondary_camera_label

        # Access button and metrics display widgets
        self.work_mode_button = self.ui.work_mode_button
        self.nav_mode_button = self.ui.nav_mode_button
        self.speed_display = self.ui.speed_display
        self.distance_display = self.ui.distance_display

        # Connect buttons to their respective functions
        self.work_mode_button.clicked.connect(self.set_work_mode)
        self.nav_mode_button.clicked.connect(self.set_navigation_mode)

        # Connect mouse click events for secondary cameras
        self.nav_secondary_camera_label.mousePressEvent = self.swap_nav_cameras
        self.work_secondary_camera_label.mousePressEvent = self.swap_work_cameras

        # Start with navigation mode
        self.set_navigation_mode()

    def update_camera_feed(self):
        self.nav_primary_camera_label.update_image()
        self.nav_secondary_camera_label.update_image()
        self.work_primary_camera_label.update_image()
        self.work_secondary_camera_label.update_image()


    def swap_nav_cameras(self, event):

        if self.swapped == False:
            self.nav_primary_camera_label.update_new_stream(self.stream2)
            self.nav_secondary_camera_label.update_new_stream(self.stream1)
            self.swapped = True
        else:
            self.nav_primary_camera_label.update_new_stream(self.stream2)
            self.nav_secondary_camera_label.update_new_stream(self.stream1)
            self.swapped = False

        #self.nav_primary_camera_label, self.nav_secondary_camera_label = self.nav_secondary_camera_label, self.nav_primary_camera_label
        self.update_camera_feed()

    def swap_work_cameras(self, event):
        if self.swapped == False:
            self.work_primary_camera_label.update_new_stream(self.work_secondary_camera_label.camera_stream)
            self.work_secondary_camera_label.update_new_stream(self.work_primary_camera_label.camera_stream)
            self.swapped = True
        else:
            self.work_primary_camera_label.update_new_stream(self.ui.work_primary_camera_label.camera_stream)
            self.work_secondary_camera_label.update_new_stream(self.ui.work_secondary_camera_label.camera_stream)
            self.swapped = False
        self.update_camera_feed()

    def set_work_mode(self):
        # Show work mode camera widgets and hide navigation mode camera widgets
        self.work_primary_camera_label.show()
        self.work_secondary_camera_label.show()
        self.nav_primary_camera_label.hide()
        self.nav_secondary_camera_label.hide()

    def set_navigation_mode(self):
        # Show navigation mode camera widgets and hide work mode camera widgets
        self.work_primary_camera_label.hide()
        self.work_secondary_camera_label.hide()
        self.nav_primary_camera_label.show()
        self.nav_secondary_camera_label.show()


# Class for processing camera feed
class CameraStream:
    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(self.url)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.frame = None

        ret, self.frame = self.cap.read()
        if not ret:
            print("Error opening camera stream")
            self.cap.release()
            self.cap = None
        else:
            self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        else:
            self.frame = None
            self.cap.release()
            self.cap = cv2.VideoCapture(self.url)

    def get_frame(self):
        return self.frame

    def __del__(self):
        if self.cap is not None:
            self.cap.release()


# Class for displaying camera feeds in the widgets
class CameraWidget(QtWidgets.QWidget):
    def __init__(self, camera_stream, label, parent=None):
        super(CameraWidget, self).__init__(parent)
        self.camera_stream = camera_stream
        self.label = label  # Add label parameter

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)

    # For switching between camera feeds
    def update_new_stream(self, stream):
        self.camera_stream = stream

    def update_image(self):
        frame = self.camera_stream.get_frame()
        if frame is not None:
            height, width, channel = frame.shape
            image = QImage(frame.data, width, height, 3 * width, QImage.Format.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(image))  # Update the label directly
            self.label.setScaledContents(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Define the camera streams


    # Create the main window with the streams
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())