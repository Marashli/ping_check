import os
import subprocess
import time

p = os.popen('ping 8.8.8.8')
start = False

while True:
    main_str = p.readline()
    main_str = main_str.split()
    if main_str[0] == 'Request':
        print('Пакет потерян!')
        subprocess.call(["afplay", "/Users/ilyamarashli//PycharmProjects/ping_check/pocket_loss.mp3"])

        start = False
    main_str = main_str[-2]
    data = ''
    if start is True:
        # print(main_str[0])

        for i in range(len(main_str)):
            if main_str[i] == 't' or main_str[i] == 'i' or main_str[i] == 'm' or main_str[i] == 'e' \
                    or main_str[i] == '=':
                pass
            else:
                data += main_str[i]

        data = float(data)

        if data <= 20:
            print('Пинг отличный')
            subprocess.call(["afplay", "/Users/ilyamarashli/PycharmProjects/ping_check/ping_ex.mp3"])
        elif 20 < data <= 160:
            print('Пинг нормальный')
            subprocess.call(["afplay", "/Users/ilyamarashli/PycharmProjects/ping_check/ping_good.mp3"])
        elif 160 < data <= 370:
            print('Пинг приемлимый')
            subprocess.call(["afplay", "/Users/ilyamarashli/PycharmProjects/ping_check/ping_300.mp3"])
        elif 370 < data < 700:
            print('Пинг плохой')
        else:
            print('Пинг ужастный')

        # print(data)

    start = True
    # time.sleep(1)

p.close()
