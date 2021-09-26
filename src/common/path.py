"""
File that defines functions to get path to ressources
"""

from os import path

WORKING_DIR = path.dirname(__file__)
RES_DIR = path.join(WORKING_DIR, "../..", "res")


def get_absolute_res_path(res_path: str) -> str:
    """
    :param res_path: chemin vers la ressource depuis le répertoire res
    :return: chemin absolu vers la ressource
    """
    return path.join(RES_DIR, res_path)
