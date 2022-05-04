import cv2


def sketch(image):
    img_grey_ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_grey = cv2.flip(img_grey_, 1)
    img_grey_blur = cv2.GaussianBlur(img_grey, (5, 5), 0)
    canny_edges = cv2.Canny(img_grey_blur, 10, 70)

    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
