import traceback
import threading

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
    view_thread = threading.Thread(target=print)

    model_thread.start()
    view_thread.start()

    view_thread.join()
    model.process(p_message.Message(p_message_subject.MessageSubject.PAUSE))
except Exception:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
