import traceback
import threading
import time

import model as m_model
import view.game_view as m_game_view
import view.player_input as m_player_input
import common.message as p_message
import common.message.message_subject as p_message_subject

# Everything is in a try-except to get the error message if the program crashs
try:
    # model part
    model = m_model.Model(0)
    model_thread = threading.Thread(target=model.main_loop)

    # view part
    view = m_game_view.GameView(model)
    view.setup()

    def run_view():
        run_message = p_message.Message(p_message_subject.MessageSubject.TOGGL_PAUSED)
        model.receive(run_message)

        while True:
            view.print_windows()
            player_input = view.get_player_input()
            while player_input is not player_input.NOTHING:
                view.treat_player_input(player_input)
                player_input = view.get_player_input()

    view_thread = threading.Thread(target=run_view)

    model_thread.start()
    view_thread.start()

    view_thread.join()

except Exception:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
