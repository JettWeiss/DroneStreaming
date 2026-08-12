import cv2

cap = cv2.VideoCapture('rtsp://localhost:8554/droneStream')
if not cap.isOpened():
    raise Exception("can't open video capture")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output/output.mp4', -1, 30.0, (width,height))

while True:
    ret, frame = cap.read()

    if ret == True:

        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)

    if not ret:
        raise Exception("can't receive frame")\

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()