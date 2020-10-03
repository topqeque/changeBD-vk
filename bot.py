from datetime import datetime, timedelta
import time
import auth

vk = auth.session_api
day = datetime.today()


def change_bd():
    bd_vk = vk.account.getProfileInfo()['bdate']  # чек др вк
    str_bd_vk = (datetime.strptime(bd_vk, '%d.%m.%Y')).strftime('%d.%m')  # стринг др вк
    today = datetime.today()  # чек сегодня
    str_today = today.strftime('%d.%m')  # стринг сегодня

    dr_vk = datetime.strptime(str_bd_vk+'.2020', '%d.%m.%Y')
    today_zero = datetime.strptime(str_today+'.2020', '%d.%m.%Y')
    raz = today_zero-dr_vk
    if raz == timedelta(days=1):
        new_bd_vk = today_zero + timedelta(days=1)  # сет др
        str_new_bd = new_bd_vk.strftime('%d.%m') + '.2020'  # др в стринг
        vk.account.saveProfileInfo(bdate=str_new_bd)  # ред др вк
    elif raz == timedelta(days=2):
        new_bd_vk = today_zero  # сет др
        str_new_bd = new_bd_vk.strftime('%d.%m') + '.2020'  # др в стринг
        vk.account.saveProfileInfo(bdate=str_new_bd)  # ред др вк
    elif raz == timedelta(days=0):
        print('BirthDay today')


while True:
    change_bd()
    time.sleep(3600)


