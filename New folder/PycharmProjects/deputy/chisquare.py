import numpy as np
import pandas as pd
from scipy import stats
import bioinfokit.analys as
data = pd.DataFrame({'mineral':['A','B','C','D'],
                      'Observed':[30,20,15,19]})
data = data.set_index('mineral')
print(data)
stats.chi2_contingency(data)

