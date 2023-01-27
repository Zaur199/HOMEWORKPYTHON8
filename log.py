from datetime import datetime


def log_temp(num_1, action, num_2, result):
    time = datetime.now().strftime('%d:%b:%Y:%H:%M:%S')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time} \nВвод пользователя: {num_1} {action} {num_2} \nРезультат:{str(result)}\n')
    
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time} \nВвод пользователя: {num_1} {action} {num_2} \nРезультат:{str(result)}\n')