import pandas as pd 
import numpy as np 

from config import *

class ConversionExcel:
    def __init__(self, filename, **columns) -> None:
        
        
        
        self.fileExcel = pd.read_excel(path + filename)
