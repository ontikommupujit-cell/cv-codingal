import cv2
image=cv2.imread('fortnitephoto.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 800, 500)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f'image dimensions: {image.shape}')