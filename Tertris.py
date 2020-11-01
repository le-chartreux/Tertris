from modules.classes.controller.Controller import Controller
from time import sleep
import traceback

controller = Controller()

try:
    while(True):
        controller.setup()
        controller.do_tick()
        sleep(0.05)

except:  # Pour avoir le message d'erreur et ne pas mess le terminal de l'utilisateur
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
