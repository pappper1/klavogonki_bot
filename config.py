user_id = '11111'

def cookies_conf(previous_game_id):
	cookies = {}

	return cookies

def headers_conf(game_id):
	headers = {
        'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
        'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin':'https://klavogonki.ru',
        'Referer':f'https://klavogonki.ru/g/?gmid={game_id}',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Prototype-Version':'1.7',
        'X-Requested-With':'XMLHttpRequest',
        'sec-ch-ua':'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
    }

	return headers