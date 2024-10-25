import sys
import cv2
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, Qt
from ui_main import Ui_RobotUIApp  # Import the generated UI class

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
        self.snapshot_button = self.ui.snapshot_button
        self.record_button = self.ui.record_button
        self.speed_display = self.ui.speed_display
        self.distance_display = self.ui.distance_display
        self.primary_battery = self.ui.primary_battery
        self.secondary_battery = self.ui.secondary_battery

        # Connect buttons to their respective functions
        self.work_mode_button.clicked.connect(self.set_work_mode)
        self.nav_mode_button.clicked.connect(self.set_navigation_mode)

        # Camera feeds initialization
        self.nav_primary_camera_feed = 0  # Change this to GoPro URL
        self.nav_secondary_camera_feed = "rtmp://localhost/live/gopro_max_stream"  # Change this to GoPro URL
        self.work_primary_camera_feed = 0  # Change this to GoPro URL
        self.work_secondary_camera_feed = 0  # Change this to GoPro URL

        # Open camera feeds
        self.nav_capture_primary = cv2.VideoCapture(self.nav_primary_camera_feed)
        self.nav_capture_secondary = cv2.VideoCapture(self.nav_secondary_camera_feed)  # using this for testing, replace these with the respective gopro feed
        self.work_capture_primary = self.nav_capture_primary
        self.work_capture_secondary = self.nav_capture_primary

        # Set up the camera
        self.cap = cv2.VideoCapture(0)  # Open the laptop's camera (temporary solution)
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        self.camera_timer.start(100)  # Update every 100 ms

        # Timer to update dummy data (speed, distance, battery)
        self.data_timer = QTimer(self)
        self.data_timer.timeout.connect(self.update_dummy_data)
        self.data_timer.start(1000)  # Update every second

        self.set_navigation_mode()  # Start in navigation mode

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

            # Convert to QPixmap and scale with respect to QLabel size
            pixmap = QPixmap.fromImage(qimg)
            scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            label.setPixmap(scaled_pixmap)
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

        # Update dummy battery levels (decreasing over time)
        front_battery_level = self.primary_battery.value() - random.randint(0, 2)
        rear_battery_level = self.secondary_battery.value() - random.randint(0, 2)
        self.primary_battery.setValue(max(0, front_battery_level))
        self.secondary_battery.setValue(max(0, rear_battery_level))

    def closeEvent(self, event):
        # Release the camera when the application is closed
        self.cap.release()
        event.accept()

# Main application
app = QApplication(sys.argv)
window = RobotUI()
window.show()
sys.exit(app.exec())