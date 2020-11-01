from time import sleep
from traceback import format_exc

from modules.classes.Controller import Controller

try:
    controller = Controller()
    controller.setup()
    while controller.get_continue_game():
        controller.do_tick()
        sleep(0.05)


except:  # Pour avoir le message d'erreur et ne pas mess le terminal de l'utilisateur
    error_output = open("error_output.txt", "w")
    error_output.write(format_exc())
    error_output.close()
