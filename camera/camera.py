import datetime
from picamera import PiCamera
from time import sleep

USER_NAME = "pi/"
HOME_DIR = "/home/" + USER_NAME
SAVE_DIR = HOME_DIR + "N1/camera/"

datetime = datetime.datetime.today()
datetime_formatted = datetime.strftime("%Y_%m%d_%H:%M:%S")

file_name = datetime_formatted + ".jpg"

camera = PiCamera()

# start to take photo
camera.start_preview()

sleep(5)

camera.capture(SAVE_DIR + file_name)

camera.stop_preview()
