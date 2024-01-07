# import pyqrcode
# import cv2
# import png
# data = 'plain text string'
# url = pyqrcode.create(data)
# url.png('myQR1.png',scale = 6)


import cv2
img = cv2.imread('myQR1.png')
detector = cv2.QRCodeDetector()
value, points, st_code = detector.detectAndDecode(img)
print(value)
