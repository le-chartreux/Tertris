import traceback
import threading

import model as m_model
import view.game_view as m_game_view
import common.message as p_message
import common.message.message_subject as p_message_subject

# Everything is in a try-except to get the error message if the program crashs
# noinspection PyBroadException
try:
    # setup of the model part (init and thread creation)
    model = m_model.Model()
    model_thread = threading.Thread(target=model.main_loop)

    # setup of the view part (init and thread creation)
    view = m_game_view.GameView(model)
    view.setup()
    view_thread = threading.Thread(target=view.main_loop)

    # adding a starting request to the game, so it will start when the model thread will start
    run_message = p_message.Message(p_message_subject.MessageSubject.TOGGL_PAUSED)
    model.receive(run_message)

    # starting the two threads (model and view)
    model_thread.start()
    view_thread.start()

    # waiting for the threads to stop
    model_thread.join()
    view_thread.join()

except Exception:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
