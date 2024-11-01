import cv2
import numpy as np

class MockCamera:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.is_opened = True  # Simulate that the camera is open

    def read(self):
        if not self.is_opened:
            return False, None
        # Generate a random image frame
        frame = np.random.randint(0, 256, (self.height, self.width, 3), dtype=np.uint8)
        return True, frame

    def release(self):
        self.is_opened = False  # Simulate releasing the camera


class MovingShapeCamera:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.is_opened = True  # Simulate that the camera is open
        self.x = 0  # Starting x position of the shape
        self.direction = 1  # Direction of movement (1 for right, -1 for left)

    def read(self):
        if not self.is_opened:
            return False, None
        # Create a blank frame
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Draw a moving circle
        cv2.circle(frame, (self.x, self.height // 2), 20, (0, 255, 0), -1)  # Green circle

        # Update the x position for the next frame
        self.x += 5 * self.direction
        if self.x > self.width or self.x < 0:
            self.direction *= -1  # Reverse direction if the circle hits the wall

        return True, frame

    def release(self):
        self.is_opened = False  # Simulate releasing the camera
