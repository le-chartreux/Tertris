from traceback import format_exc

from modules.Controller import Controller

try:
    controller = Controller()
    controller.run()


except Exception:  # Pour avoir le message d'erreur et ne pas détruire le terminal de l'utilisateur car ça a crash
    # sans le restorer
    error_output = open("error_output.txt", "w")
    error_output.write(format_exc())
    error_output.close()
