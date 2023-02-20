from PIL import Image
import pytesseract
import cv2
import argparse

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_path = "C:/Users/Vollinger/Desktop/sudoku.png"


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help=file_path)
ap.add_argument("-d", "--digits", type=int, default=1,
	help="whether or not *digits only* OCR will be performed")
args = vars(ap.parse_args())