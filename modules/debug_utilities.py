# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir des fonctions utiles pour debug
# ==========================================================

def print_in_output_dot_txt(text: str):
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Ajoute le texte dans le fichier "output.txt", utile puisque curses ne permet pas de print de message
    # =============================
    output_dot_txt = open("output.txt", "a")
    output_dot_txt.write(text + '\n')
    output_dot_txt.close()
