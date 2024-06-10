import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 230)
"""
cv2.createTrackbar("Hue Min", "TrackBars", 11, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 23, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 131, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 72, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 212, 255, empty)

cv2.createTrackbar("Hue Min", "TrackBars", 8, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 29, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 123, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 162, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 78, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 212, 255, empty)
"""
cv2.createTrackbar("Hue Min", "TrackBars", 139, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 114, 255, empty) #123
cv2.createTrackbar("Sat Max", "TrackBars", 197, 255, empty) #140
cv2.createTrackbar("Val Min", "TrackBars", 151, 255, empty) #160
cv2.createTrackbar("Val Max", "TrackBars", 212, 255, empty)

while True:


    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])



    print(h_min, h_max, s_min, s_max, v_min, v_max)



    cap = cv2.VideoCapture('video_1.mp4')
    while cap.isOpened():
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        ret, frame = cap.read()
        if not ret:
            break

        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV, lower, upper)
        frameResult = cv2.bitwise_and(frame, frame, mask=mask)
        #frameResult = cv2.morphologyEx(frameResult, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8), iterations=2)
        frameResult = cv2.morphologyEx(frameResult, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8), iterations=2)
        frameResult = cv2.dilate(frameResult, np.ones((5, 5), np.uint8))
        frameResult = cv2.dilate(frameResult, np.ones((5, 5), np.uint8))
        frameResult = cv2.medianBlur(frameResult, 7)
        #frameResult = cv2.morphologyEx(frameResult, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8), iterations=2)
        #frameResult = cv2.dilate(frameResult, np.ones((5, 5), np.uint8))


        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        frameHSV = cv2.resize(frameHSV, (0, 0), fx=0.4, fy=0.4)
        mask = cv2.resize(mask, (0, 0), fx=0.4, fy=0.4)
        frameResult = cv2.resize(frameResult, (0, 0), fx=1, fy=1)

        concat = np.concatenate((frame, frameResult), axis=1)

        result2 = frameResult.copy()
        labeled = frame.copy()
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY))
        objects_on_screen = num_labels > 1
        if objects_on_screen:
            skipped_objects = 0
            for object_index in range(1, num_labels):
                x, y, w, h, area = stats[object_index]

                if area < 20:
                    continue
                centroid_x, centroid_y = centroids[object_index]
                
                cv2.rectangle(labeled, (x-5, y-5), (x + w  + 5, y + h + 5), (0, 0, 255), 2)



        cv2.imshow("Original", frame)
        cv2.imshow("HSV", frameHSV)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", frameResult)
        cv2.imshow("Concat", concat)
        cv2.imshow("Labeled", labeled)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
