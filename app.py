import os
import sys
from time import sleep


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

try:
    print('Iniciando app!!!')
    os.system('{} & python {} runserver'.format(resource_path('venv/Scripts/activate'),
                                                resource_path('./core/manage.py')))
except Exception as error:
    print(error)
    sleep(10)