uah_course = float(input("Введите курс гривны: "))
rub_course = float(input("Введите курс рубля: "))
uah = float(input("Сколько гривен переводим: "))
sum_rub = ( uah / uah_course) * rub_course
finally_course = sum_rub / uah
print(f'На сейчас курс: {finally_course}')

get_uah = float(input("По какому курсу купили гривну: "))
salary = (sum_rub - (uah * get_uah)) / 2
print(f'Мой заработок: {salary} rub')