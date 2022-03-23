import pymysql #Libreria para conectar con MariaDB
import datetime
import serial
import time
from datetime import time, tzinfo, timedelta

num_sensor = 4


def range_temp(t):
	if t > 10 and t < 20:
		return 1
	elif t <= 10 or t >= 20:
		return 0

def range_hum(h):
	if h > 10 and h < 20:
		return 1
	elif h <= 10 or h >= 20:
		return 0

def range_co2(c):
	if c > 10 and c < 20:
		return 1
	elif c <= 10 or c >= 20:
		return 0

def range_lum(l):
	if l > 10 and l < 20:
		return 1
	elif l <= 10 or l >= 20:
		return 0

def selec(c):
    switcher = {
        1: range_temp(c),
        2: range_hum(c),
        3: range_co2(c),
        4: range_lum(c),
    }

    return switcher.get(c, "Invalid month")

def conver_str(lst):
	lst_str=""	
	for x in lst:
		if lst_str == "":
			lst_str = str(x)
		else:
			lst_str = lst_str + ":" + str(x)	

	return lst_str
    


db = pymysql.connect("mynodered.ddns.net","usuariow","usuariow","monitoreo") # Conector (direccion, usuario, contraseña, nombre_BD)
cu = db.cursor()# Declaracion del cursor

cu.execute("SELECT Planta, Valor FROM monitoreo2") # Se extraen los valores de la columan llamada "Valor"
values = cu.fetchall()
print(values)

num_data = len(values)

num_plant = num_data/num_sensor

count = 0
lst = []
for i in values:

	if count == 0:
		lst.append(i[0])
	if count < num_sensor:
		lst.append(i[1])
		count +=1
	elif count == num_sensor:
		lst.append(i[0])
		lst.append(i[1])
		count = 1



lst_to_send =[]
lim = num_sensor + 1
count = 0
for j in lst:
	
	if count == 0:
		lst_to_send.append(j)
		count +=1
	elif count < lim and count > 0:
		lst_to_send.append(j)
		lst_to_send.append(selec(count))
		count +=1
	elif count == lim:
		lst_to_send.append(j)
		count = 1	

print(lst)	
print(lst_to_send)


plant1_send = conver_str(lst_to_send[0:9])
plant2_send = conver_str(lst_to_send[9:18])
plant3_send = conver_str(lst_to_send[18:27])
plant4_send = conver_str(lst_to_send[27:36])

print(plant4_send)	





def get_sorted_recommendations(lst_mv_til):
    lst_mv= get_related_titles(lst_mv_til)
    lst_mv= sorted(lst_mv, key = lambda movieName: (get_movie_rating(get_movie_data(mv_name)), mv_name), reverse=True)
    
    return lst_mv

	

