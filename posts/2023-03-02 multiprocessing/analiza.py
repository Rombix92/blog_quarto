def map_function(args_temp):
  import pandas as pd
  from datetime import datetime
  from time import sleep
  pd_results_temp=pd.DataFrame(columns=['a','sleep_time','started'])
  started = datetime.now()
  arg_a = args_temp[0]
  arg_sleep_time = args_temp[1]
  pd_results_temp = pd_results_temp.append({'a':arg_a,'sleep_time':arg_sleep_time,'started':started}, ignore_index=True)
  sleep(arg_sleep_time)
  return pd_results_temp
