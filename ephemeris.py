import calendar
import pandas as pd
from datetime import datetime, timedelta
import pytz

def create_jd_list(julian_date, period, iteration_number):

  jd_list = []
  
  for i in range(iteration_number):
    julian_date = julian_date + period
    jd_list.append(format(julian_date, ".3f"))
  return jd_list


jd_list = create_jd_list(julian_date=2460238.518, period=2.0562997, iteration_number=20)

def convert_jd_to_utc(jd_list):
    utc_list = []

    for i in range(len(jd_list)):
        jd = float(jd_list[i])
        # Convert JD to MJD (Modified Julian Date)
        mjd = jd - 2400000.5

        # Convert MJD to datetime
        dt = datetime(1858, 11, 17) + timedelta(days=mjd)

        # Convert datetime to UTC
        utc = dt.replace(tzinfo=pytz.utc)

        # Append UTC to the list
        utc_list.append(utc)

    return utc_list
def convert_utc_to_ut(utc_list):
    ut_list = []
    for i in range(len(utc_list)):
        ut = utc_list[i] + timedelta(hours=0)  #Note: Please input the local time zone difference of your region. Example: Turkey +3
        ut_list.append(ut)         
        
    return ut_list

utc_list = convert_jd_to_utc(jd_list)
ut_list = convert_utc_to_ut(utc_list)

start_list = []
finish_list = []

start1_list = []
finish1_list = []

for i in range(len(utc_list)):
    start = utc_list[i] - timedelta(hours=3, minutes=42)
    start_list.append(start)
    start1 = start + timedelta(hours=0) #Note: Please input the local time zone difference of your region. Example: Turkey +3
    start1_list.append(start1)
    
    finish = utc_list[i] + timedelta(hours=3, minutes=42)
    finish_list.append(finish)
    finish1 = finish + timedelta(hours=0) #Note: Please input the local time zone difference of your region. Example: Turkey +3
    finish1_list.append(finish1)

start_list_string = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in start1_list]
finish_list_string = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in finish1_list]
time_string_list = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in ut_list]

print(time_string_list)

time_string_list = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in utc_list]

print(time_string_list)

df = pd.DataFrame({"Epoch" : jd_list, "Start" : start_list_string ,"Mid": time_string_list, "Finish" : finish_list_string})


df.to_excel("C:\\location\\ephemeris.xlsx")