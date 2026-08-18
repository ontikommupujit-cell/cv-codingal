import cv2
image=cv2.imread('fortnitephoto.jpg')
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize_gray_image=cv2.resize(gray_image, (224, 224))
cv2.imshow('Gray Image', resize_gray_image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('gray_fortnitephoto.jpg', resize_gray_image)
    print('Image saved as gray_fortnitephoto.jpg')
else:
    print('Image not saved')
cv2.destroyAllWindows()
print(f'gray image dimensions: {resize_gray_image.shape}')