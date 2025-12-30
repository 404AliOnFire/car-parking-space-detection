import cv2 as cv
import numpy as np
import cvzone
import pickle

from matplotlib.style.core import available

WIDTH = 108
HEIGHT = 46


def get_pos_list():
    try:
        with open('car_pos', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print('No car pos defined')


def process_image(img, pos_list):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray, 11, 0)
    threshold = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 2)
    threshold = cv.dilate(threshold, np.ones((1, 1), np.uint8), iterations=3)

    return threshold


def check_parking(img, pos_list):
    threshold = process_image(img, pos_list)
    available_parks = 0

    for pos in pos_list:
        x, y = pos

        park = threshold[y:y + HEIGHT, x:x + WIDTH]
        white_pixels = cv.countNonZero(park)

        if white_pixels < 280:
            thic = 4
            available_parks += 1
            color = (0, 255, 0)
        else:
            thic = 3
            color = (0, 0, 255)

        cv.rectangle(img, (x, y), (x + WIDTH, y + HEIGHT), color, thic)

        cvzone.putTextRect(img, str(white_pixels), (x + 10, y + 40), 1, 1, (255, 255, 255), offset=1)
        cvzone.putTextRect(img, f"Free: {available_parks}", (50, 20), 2, 2, (255, 255, 255), offset=1)
        cv.imshow('threshold', threshold)


def main():
    pos_list = get_pos_list()
    cap = cv.VideoCapture('carPark.mp4')
    frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    while True:
        sucess, img = cap.read()
        if not sucess:
            pass

        check_parking(img, pos_list)

        cv.imshow('Park', img)
        current_frame = int(cap.get(cv.CAP_PROP_POS_FRAMES))

        if current_frame == frame_count:
            cap.set(cv.CAP_PROP_POS_FRAMES, 0)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
