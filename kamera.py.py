import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
def save_image(frame):
    filename = "rasm.png"
    text_filename = "ma'lumotlar.txt"
    cv2.imwrite(filename, frame)
    with open(text_filename, "w") as file:
        file.write(f"Rasm saqlandi: {filename}\n")
while True:
    result, video_frame = video_capture.read()
    if result is False:
        break
    button_height = 50
    button_width = 200
    button_color = (50, 50, 50)
    text_color = (255, 255, 255)
    text = "Rasmga olish (s)"
    button_top_left = (int((500 - button_width) / 2), 500 - button_height - 10)
    button_bottom_right = (button_top_left[0] + button_width, button_top_left[1] + button_height)
    cv2.rectangle(video_frame, button_top_left, button_bottom_right, button_color, -1)
    cv2.putText(video_frame, text, (button_top_left[0] + 10, button_top_left[1] + 35), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)
    cv2.imshow("Kamera", video_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        save_image(video_frame)
        print("Rasm saqlandi.")
    if key == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
