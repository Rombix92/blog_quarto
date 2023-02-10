def map_function(args_temp):
  import pandas as pd
  from datetime import datetime
  from time import sleep
  pd_results_temp=pd.DataFrame(columns=['a','b','started'])
  started = datetime.now()
  a = args_temp[0]
  b = args_temp[1]
  pd_results_temp = pd_results_temp.append({'a':a,'b':b,'started':started}, ignore_index=True)
  sleep(b)
  return pd_results_temp
