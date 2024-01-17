user_id = '773010'

def cookies_conf(previous_game_id):
	cookies = {
		'__utmc':'208942541',
		'_ym_uid':'169842420138073774',
		'_ym_d':'1698424201',
		'PHPSESSID':'ucojr4l6n96bkkv55orab4iqo4',
		'__gads':'ID=656801ee93076d96-22b64fd7ace40001:T=1698424218:RT=1699040681:S=ALNI_MYXmA5m189SufnEKCsWbTLg6_wXOw',
		'__gpi':'UID=00000caa322d88e2:T=1698424218:RT=1699040681:S=ALNI_MY7SLNbit9EwzUOQDRZhAtkMTQBPQ',
		'played_once_already':'1',
		'__prefs2':'chat_active_room%3Dgame%7Clowspeed%3D1%7Cstats_gametype%3Dvoc-8835%7Cparam_keyboard%3Dtrue%7Cchat-game-hide%3Dtrue%7Chide_gametype_alert_normal%3D1',
		'__utma':'208942541.401237835.1698424201.1702401027.1703274228.24',
		'__utmz':'208942541.1703274228.24.15.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
		'__utmt':'1',
		'_ym_isad':'2',
		'_ym_visorc':'w',
		'XSRF-TOKEN':'3ca27da6',
		'user':'popnyjdrochila%3Bcaa377ec546f063d3ee1db3b48b8d60c',
		'ul':'94cac%2C93eae',
		'__utmb':'208942541.11.10.1703274228',
		'__game__':f'{previous_game_id}',
	}

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