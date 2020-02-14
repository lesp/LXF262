import requests
from gpiozero import MotionSensor
from picamera import PiCamera
from signal import pause
from filestack import Client

client = Client("YOUR FILESTACK API KEY")
camera = PiCamera()
camera.resolution = (1920, 1080)
def send_alert():
    camera.capture("image.jpg")
    new_filelink = client.upload(filepath="image.jpg")
    print(new_filelink.url)
    r = requests.post("https://maker.ifttt.com/trigger/trigger/with/key/IFTTT API KEY", json={"value1" : new_filelink.url})
    if r.status_code == 200:
        print("Alert Sent")
    else:
        print("Error")

pir = MotionSensor(17)
pir.when_motion = send_alert
pause()
