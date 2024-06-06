import cv2
import numpy as np

def event_frame(event_x, event_y, event_polarity, image_shape):
    event_image = np.ones(image_shape) * 127
    
    for x, y, polarity in zip(event_x, event_y, event_polarity):
        event_image[y, x] = 255 if polarity == 1 else 0
    
    event_image = event_image.astype(np.uint8)
    
    return event_image

with open("13/mats/events.txt", "r") as file:
    timestamps = []
    x_coordinates = []
    y_coordinates = []
    polarities = []

    for line in file:
        parts = line.split()
        timestamp = float(parts[0])
        x_coord = int(parts[1])
        y_coord = int(parts[2])
        polarity = int(parts[3])
        
        if 1 < timestamp < 2:
            timestamps.append(timestamp)
            x_coordinates.append(x_coord)
            y_coordinates.append(y_coord)
            polarity = 1 if polarity == 1 else -1
            polarities.append(polarity)

tau = 0.01

temp_timestamps = []
temp_x = []
temp_y = []
temp_polarities = []
for timestamp, x, y, polarity in zip(timestamps, x_coordinates, y_coordinates, polarities):
    temp_timestamps.append(timestamp)
    temp_x.append(x)
    temp_y.append(y)
    temp_polarities.append(polarity)
    
    if temp_timestamps[-1] - temp_timestamps[0] > tau:
        event_img = event_frame(temp_x, temp_y, temp_polarities, (180, 240))

        cv2.imshow("Event Frame", event_img)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

        temp_timestamps.clear()
        temp_x.clear()
        temp_y.clear()
        temp_polarities.clear()
        
cv2.destroyAllWindows()
