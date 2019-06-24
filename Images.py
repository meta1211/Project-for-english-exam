import cv2
import numpy as np
from datetime import datetime, timedelta
import os

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
def get_black_background():
    return np.zeros((500, 500))

start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, 
                (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), 
                font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    return image

projectFolder = os.path.dirname(__file__)
folder = os.path.join(projectFolder, 'time_images')
while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    text = text.replace(':','_')
    path = os.path.join(folder, text +'.jpg')
    cv2.imwrite(path, image)
    start_time += timedelta(minutes=1)
