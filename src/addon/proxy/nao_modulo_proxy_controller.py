import sys
import os

diretorio_raiz = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(os.path.abspath(diretorio_raiz))

from src.events.utils.func_qualquer import ola_mundo

ola_mundo()