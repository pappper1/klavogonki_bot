import time
import requests
import json
import keyboard

from config import *


class Parser:
    def __init__(self, game_id, previous_game_id, cookies, headers):
        self.data = {
            'chat_last_id': '0',
            'cached_users': f'0,{user_id}',
            'need_text': '1',
            'player_v': '2',
            }
        self.game_id = game_id
        self.previous_game_id = previous_game_id
        self.cookies = cookies
        self.headers = headers

    def get_game_text(self):
        try:
            response = requests.post(f'https://klavogonki.ru/g/{self.game_id}.info', cookies=self.cookies, headers=self.headers, data=self.data)
            text = json.loads(response.text)['text']['text']

        except Exception as e:
            print(e)
            exit()

        return text

def main():
    previous_game_id = input('Введите ID предыдущей игры: ')
    game_id = input('Введите ID игры: ')
    text = Parser(game_id, previous_game_id, cookies_conf(previous_game_id), headers_conf(game_id)).get_game_text()
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