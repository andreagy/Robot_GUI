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
        self.front_camera_label = self.ui.front_camera_label
        self.rear_camera_label = self.ui.rear_camera_label
        self.snapshot_button = self.ui.snapshot_button
        self.record_button = self.ui.record_button
        self.speed_display = self.ui.speed_display
        self.distance_display = self.ui.distance_display
        self.front_battery = self.ui.front_battery
        self.rear_battery = self.ui.rear_battery

        # Set up the camera
        self.cap = cv2.VideoCapture(0)  # Open the laptop's camera (temporary solution)
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        self.camera_timer.start(100)  # Update every 100 ms

        # Timer to update dummy data (speed, distance, battery)
        self.data_timer = QTimer(self)
        self.data_timer.timeout.connect(self.update_dummy_data)
        self.data_timer.start(1000)  # Update every second

    def update_camera_feed(self):
        # Read frame from the camera
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to QImage format for display in PyQt
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color from BGR to RGB
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

            # Calculate the aspect ratio of the camera feed
            cam_aspect_ratio = width / height

            # Resize the image to fit the QLabel while maintaining aspect ratio
            def resize_pixmap(pixmap, label):
                label_width, label_height = label.size().width(), label.size().height()
                label_aspect_ratio = label_width / label_height

                if cam_aspect_ratio > label_aspect_ratio:
                    # Fit to width, adjust height
                    scaled_pixmap = pixmap.scaledToWidth(label_width, Qt.TransformationMode.SmoothTransformation)
                    scaled_pixmap = scaled_pixmap.scaledToHeight(label_height, Qt.TransformationMode.SmoothTransformation)
                else:
                    # Fit to height, adjust width
                    scaled_pixmap = pixmap.scaledToHeight(label_height, Qt.TransformationMode.SmoothTransformation)
                    scaled_pixmap = scaled_pixmap.scaledToWidth(label_width, Qt.TransformationMode.SmoothTransformation)

                return scaled_pixmap

            # Display the frame on the front and rear camera labels
            front_pixmap = QPixmap.fromImage(qimg)
            rear_pixmap = QPixmap.fromImage(qimg)

            self.front_camera_label.setPixmap(resize_pixmap(front_pixmap, self.front_camera_label))
            self.rear_camera_label.setPixmap(resize_pixmap(rear_pixmap, self.rear_camera_label))  # Use same feed for now

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_camera_feed()  # Update the camera feed to fit the new size

    def update_dummy_data(self):
        # Update dummy speed
        speed = random.uniform(0.0, 0.58)  # Random speed between 0 and 0.58 m/s
        self.speed_display.display(round(speed, 2))

        # Update dummy distance (assume it's incrementing based on the speed)
        distance = self.distance_display.intValue() + random.randint(1, 3)
        self.distance_display.display(distance)

        # Update dummy battery levels (decreasing over time)
        front_battery_level = self.front_battery.value() - random.randint(0, 2)
        rear_battery_level = self.rear_battery.value() - random.randint(0, 2)
        self.front_battery.setValue(max(0, front_battery_level))
        self.rear_battery.setValue(max(0, rear_battery_level))

    def closeEvent(self, event):
        # Release the camera when the application is closed
        self.cap.release()
        event.accept()

# Main application
app = QApplication(sys.argv)
window = RobotUI()
window.show()
sys.exit(app.exec())
