import calendar
import pandas as pd
from datetime import datetime, timedelta
import pytz
def liste_olustur(baslangic_sayi, arttirma_miktari, iterasyon_sayisi):

  liste = []
  
  for i in range(iterasyon_sayisi):
    baslangic_sayi = baslangic_sayi + arttirma_miktari
    liste.append(format(baslangic_sayi, ".3f"))
  return liste


liste = liste_olustur(2460223.60764, 2.7277427, 100)


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


jd_list = liste
utc_list = convert_jd_to_utc(jd_list)

start_list = []
finish_list = []
for i in range(len(utc_list)):
  start = utc_list[i] - timedelta(hours=5,minutes=34)
  start_list.append(start)
  finish = utc_list[i] + timedelta(hours=5, minutes=34)
  finish_list.append(finish)


start_list_string = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in start_list]
finish_list_string = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in finish_list]

time_string_list = [datetime_obj.strftime('%d/%m/%Y %H:%M') for datetime_obj in utc_list]

print(time_string_list)

df = pd.DataFrame({"Epoch" : liste, "Start" : start_list_string ,"Mid": time_string_list, "Finish" : finish_list_string})


df.to_excel("D:\\Kodlama\\Ephemeris2.xlsx")