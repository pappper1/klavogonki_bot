import time
import requests
import json
import keyboard

from config import *

data = {
    'chat_last_id': '0',
    'cached_users': f'0,{user_id}',
    'need_text': '1',
    'player_v': '2',
}

def get_game_text(game_id, previous_game_id):
    cookies = cookies_conf(previous_game_id)
    headers =headers_conf(game_id)
    try:
        response = requests.post(f'https://klavogonki.ru/g/{game_id}.info', cookies=cookies, headers=headers, data=data)
        print(response.text)
        text = json.loads(response.text)['text']['text']

    except Exception as e:
        print(e)
        exit()

    return text

def main():
    previous_game_id = input('Введите ID предыдущей игры: ')
    game_id = input('Введите ID игры: ')
    text = get_game_text(game_id, previous_game_id)
    print(text)
    keyboard.wait('backspace')
    for word in text.split():
        time_sleep = 0.97 if len(word) >= 4 else 0.67
        keyboard.write(word)
        time.sleep(time_sleep)
        keyboard.press_and_release('space')


if __name__ == '__main__':
    while True:
        main()