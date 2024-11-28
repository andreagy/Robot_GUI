import cv2
import ffmpeg
import numpy as np

http_url = "http://192.168.2.2:8889/cam1/"

def fetch_http_stream_ffmpeg(url):
    process = (
        ffmpeg
        .input(url)
        .output('pipe:', format='rawvideo', pix_fmt='bgr24')
        .run_async(pipe_stdout=True)
    )
    while True:
        in_bytes = process.stdout.read(640 * 480 * 3)  # Adjust resolution to match the stream
        if not in_bytes:
            break
        frame = np.frombuffer(in_bytes, np.uint8).reshape(480, 640, 3)  # Adjust resolution here
        yield frame

# Example Usage
for frame in fetch_http_stream_ffmpeg(http_url):
    cv2.imshow("HTTP Stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
