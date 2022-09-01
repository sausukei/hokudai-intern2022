import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os 
import re

posi_data=[]
nega_data=[]
neu_data=[]

plt.ylim(-1,1)
for filename in glob.glob('nli/nli*.txt'):
   print(filename.replace('nli/nli',''))
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       cut = str(filename.replace('nli/nli',''))
       print(cut)