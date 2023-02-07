import pandas as pd
from datetime import datetime
from time import sleep

def map_function(combo):
    pd_results_temp=pd.DataFrame(columns=['a','b','c','started'])
    started = datetime.now()
    a = combo[0]
    b = combo[1]
    c = combo[2]
    pd_results_temp = pd_results_temp.append({'a':a,'b':b,'c':c,'started':started}, ignore_index=True)
    sleep(b)
    return pd_results_temp
