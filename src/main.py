import traceback
import threading
import time

import model
import view
import common.message as p_message
import common.message.message_subject as p_message_subject

# Everything is in a try-except to get the error message if the program crashs
try:
    # creating the model part
    model = model.Model(0)

    def run_model():
        run_message = p_message.Message(p_message_subject.MessageSubject.RUN)
        model.process(run_message)

    model_thread = threading.Thread(target=run_model)

    # creating the view part
    # TODO
    # temporary print for testing
    def run_view():
        while True:
            grid = model.get_grid_with_active()
            for line in grid:
                print("|", end="")
                for column in line:
                    print("#" if column is not None else " ", end="")
                print("|")
            print("+----------+")
            time.sleep(0.3)
    view_thread = threading.Thread(target=run_view)

    model_thread.start()
    view_thread.start()

    view_thread.join()
    model.process(p_message.Message(p_message_subject.MessageSubject.PAUSE))
except Exception:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
