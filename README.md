# QR-CODE-READER
#### Simple QR Code Reader, made using OpenCV library of Python.

## Project Structure
#### The project consist of a main.py file , an image file -- myQR1.png and a README.md file.

## How to use
#### Simply run the main.py file . The program is set to read the qr codes of present in the file myQR1.png. To extract the information of any qr code, just write it's path inside cv2.imread() function.

## How does it work
#### QR Code reader is an application of OpenCV framework. It starts with loading the qr file by using imread() function of cv2 module. Then a reference class of cv2.QRCodeDetector() is created. And then the loaded file is passed to this reference class which returns the actual value stored in QR Code.

