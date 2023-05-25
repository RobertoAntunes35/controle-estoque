import pandas as pd 
import numpy as np 



class ConversionExcel:
    def __init__(self, filename, **columns) -> None:

        try:
            self.fileExcel = pd.read_excel(path + filename)

from config import *

pd.read_excel(path + FILE_CLIENTES)