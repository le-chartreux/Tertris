from modules.classes.controller.Controller import Controller
from time import sleep
import traceback

controller = Controller()

try:
    while(True):
        controller.setup()
        controller.do_tick()
        sleep(0.1)

except Exception as ex:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    raise ex

