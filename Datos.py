import os
import time
from dependencias import *
class Datos:
    driver = None

    def __init__(self):
        dep_paquetes()
        self.driver = dep_driver()

    def get_driver(self):
        return self.driver