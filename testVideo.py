import cv2

# Initialize a video feed
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    res = cv2.waitKey(1)

    # Stop if the user presses "q"
    if res & 0xFF == ord('q'):
        break

