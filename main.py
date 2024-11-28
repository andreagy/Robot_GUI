import sys
import cv2
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, Qt
from ui_main import Ui_RobotUIApp  # Import the generated UI class
from mock_camera_feed import MockCamera, MovingShapeCamera

class RobotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RobotUIApp()  # Create an instance of the generated UI class
        self.ui.setupUi(self)  # Set up the UI

        # Access the widgets defined in Qt Designer
        self.nav_primary_camera = self.ui.nav_primary_camera_label
        self.nav_secondary_camera = self.ui.nav_secondary_camera_label
        self.work_primary_camera = self.ui.work_primary_camera_label
        self.work_secondary_camera = self.ui.work_secondary_camera_label
        self.work_mode_button = self.ui.work_mode_button
        self.nav_mode_button = self.ui.nav_mode_button
        #self.snapshot_button = self.ui.snapshot_button
        #self.record_button = self.ui.record_button
        self.speed_display = self.ui.speed_display
        self.distance_display = self.ui.distance_display

        # Connect buttons to their respective functions
        self.work_mode_button.clicked.connect(self.set_work_mode)
        self.nav_mode_button.clicked.connect(self.set_navigation_mode)

        # Connect mouse click events for secondary cameras
        self.nav_secondary_camera.mousePressEvent = self.swap_nav_cameras
        self.work_secondary_camera.mousePressEvent = self.swap_work_cameras

        # Camera feeds initialization
        self.nav_primary_camera_feed = "rtmp://192.168.0.50:1935/live/mystream"
        self.nav_secondary_camera_feed = "rtmp://192.168.0.50:1935/live/mystream2"
        self.work_primary_camera_feed = 0  # Change this to GoPro URL
        self.work_secondary_camera_feed = 0  # Change this to GoPro URL

        # Open camera feeds
        self.nav_capture_primary = cv2.VideoCapture(0)
        self.nav_capture_secondary = MockCamera()
        self.work_capture_primary = self.nav_capture_primary # using this for testing, replace these with the respective gopro feed
        self.work_capture_secondary = MovingShapeCamera()

        # Set up the camera
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        self.camera_timer.start(100)  # Update every 100 ms

        # Timer to update dummy data (speed, distance, battery)
        self.data_timer = QTimer(self)
        self.data_timer.timeout.connect(self.update_dummy_data)
        self.data_timer.start(1000)  # Update every second

        self.set_navigation_mode()  # Start in navigation mode

    def swap_nav_cameras(self, event):
        self.nav_capture_primary, self.nav_capture_secondary = self.nav_capture_secondary, self.nav_capture_primary
        self.update_camera_feed()

    def swap_work_cameras(self, event):
        self.work_capture_primary, self.work_capture_secondary = self.work_capture_secondary, self.work_capture_primary
        self.update_camera_feed()

    def set_work_mode(self):
        # Show work mode camera widgets and hide navigation mode camera widgets
        self.work_primary_camera.show()
        self.work_secondary_camera.show()
        self.nav_primary_camera.hide()
        self.nav_secondary_camera.hide()

    def set_navigation_mode(self):
        # Show navigation mode camera widgets and hide work mode camera widgets
        self.work_primary_camera.hide()
        self.work_secondary_camera.hide()
        self.nav_primary_camera.show()
        self.nav_secondary_camera.show()

    def update_camera_feed(self):
        # Update each camera feed and display in the appropriate QLabel
        self.display_feed(self.nav_capture_primary, self.nav_primary_camera)
        self.display_feed(self.nav_capture_secondary, self.nav_secondary_camera)
        self.display_feed(self.work_capture_primary, self.work_primary_camera)
        self.display_feed(self.work_capture_secondary, self.work_secondary_camera)

    def display_feed(self, capture, label):
        ret, frame = capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

            # Convert to QPixmap
            pixmap = QPixmap.fromImage(qimg)

            # Scale the pixmap to fit the label while preserving the aspect ratio
            scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                          Qt.TransformationMode.SmoothTransformation)

            # Set the scaled pixmap to the label
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(True)  # Ensure the label scales its contents
            label.repaint()  # Ensure QLabel refreshes to display the new frame

    def closeEvent(self, event):
        # Release all cameras when the application is closed
        self.nav_capture_primary.release()
        self.nav_capture_secondary.release()
        self.work_capture_primary.release()
        self.work_capture_secondary.release()
        event.accept()

    def closeEvent(self, event):
        # Release all cameras when the application closes
        self.nav_capture_primary.release()
        self.nav_capture_secondary.release()
        self.work_capture_primary.release()
        self.work_capture_secondary.release()
        event.accept()

    def update_dummy_data(self):
        # Update dummy speed
        speed = random.uniform(0.0, 0.58)  # Random speed between 0 and 0.58 m/s
        self.speed_display.display(round(speed, 2))

        # Update dummy distance (assume it's incrementing based on the speed)
        distance = self.distance_display.intValue() + random.randint(1, 3)
        self.distance_display.display(distance)

    def closeEvent(self, event):
        # Release the camera when the application is closed
        self.cap.release()
        event.accept()

# Main application
app = QApplication(sys.argv)
window = RobotUI()
window.show()
sys.exit(app.exec())