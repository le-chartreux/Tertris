# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir des fonctions utiles pour debug, puisque Curses ne permet plus de print()
# ==========================================================

def print_in_output_dot_txt(text: str):
    output_dot_txt = open("output.txt", "a")
    output_dot_txt.write(text + '\n')
    output_dot_txt.close()
