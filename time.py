from datetime import datetime
import pytz



tz_Omsk = pytz.timezone('Asia/Omsk')
datetime_Omsk = datetime.now(tz_Omsk)
#print("Omsk time:", datetime_Omsk.strftime("%H:%M:%S"))

tz_Novosibirsk = pytz.timezone('Asia/Novosibirsk')
datetime_Novosibirsk = datetime.now(tz_Novosibirsk)
#print("Novosibirsk time:", datetime_Novosibirsk.strftime("%H:%M:%S"))

tz_Moscow = pytz.timezone('Europe/Moscow')
datetime_Moscow = datetime.now(tz_Moscow)
#print("Moscow time:", datetime_Moscow.strftime("%H:%M:%S"))


print("Города:\n 1 - Омск\n 2 - Новосибирск\n 3 - Москва")
x = input("Пожалуйста, выберете город:\n")

x = int(x)

if x is 1:
    print("Omsk time:", datetime_Omsk.strftime("%H:%M:%S"))
elif x is 2:
    print("Novosibirsk time:", datetime_Novosibirsk.strftime("%H:%M:%S"))
elif x is 3:
    print("Moscow time:", datetime_Moscow.strftime("%H:%M:%S"))
else:
    print('Город не найден')