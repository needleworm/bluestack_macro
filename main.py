import pywinmacro as pw
import time
import os


imgList = []
for el in os.listdir():
    if el.endswith(".jpg") or el.endswith(".JPG"):
        imgList.append(el)


def find_and_click(filename):
    test = pw.find_on_screen(filename, confidence=0.7)
    if test:
        pw.click(test)


while True:
    for el in imgList:
        find_and_click(el)
        time.sleep(10)

