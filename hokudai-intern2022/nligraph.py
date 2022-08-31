import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


for filename in glob.glob('mainpeople_newanalyse/*.txt'):
   print(filename.replace('mainpeople_newanalyse/',''))
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       cut = str(filename.replace('mainpeople_newanalyse/',''))