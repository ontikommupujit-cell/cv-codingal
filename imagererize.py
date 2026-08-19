import cv2
image = cv2.imread("fortnitephoto.jpg")
sizes = [
    (320, 240),
    (640, 480),
    (1280, 720)
]
for width, height in sizes:
    resized = cv2.resize(image, (width, height))
    cv2.imshow(f"{width}x{height}", resized)
    cv2.imwrite(f"resized_{width}x{height}.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()