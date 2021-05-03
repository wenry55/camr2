
import ctypes
import ctypes.util
import time


from datetime import datetime
date_time_str = '02/05/21 19:00:00'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y  %H:%M:%S')
print (date_time_obj)


time_tuple = (2021, 5, 2, 21, 59, 59, 0)
import subprocess
import shlex

time_string=datetime(*time_tuple).isoformat()
print(time_string)

subprocess.call(shlex.split(f"date -s '{time_string}'"))
#subprocess.call(shlex.split(f"hwclock -w"))
