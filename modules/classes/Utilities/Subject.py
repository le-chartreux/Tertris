# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Subject, les sujets des query
# -----------------------------
# REMARQUES :
# - Les sujets valant entre 100 et 199 viennent de la vue
# - Les sujets entre 200 et 299 viennent du modèle
# ==========================================================

from enum import Enum


class Subject(Enum):
    # queries from view
    KEY_ENTRY = 100

    # queries from model
    UPDATE_VIEW = 200
