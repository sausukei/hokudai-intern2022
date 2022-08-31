import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os 
import re

for filename in glob.glob('nli/nli*.txt'):
   print(filename.replace('nli/nli',''))
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       cut = str(filename.replace('nli/nli',''))
       print(cut)