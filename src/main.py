import traceback

import model
import view

# Everything is in a try-except to get the error message if the program crashs
try:
    model = model.Model(0)
except Exception:
    error_output = open("error_output.txt", "w")
    error_output.write(traceback.format_exc())
    error_output.close()
