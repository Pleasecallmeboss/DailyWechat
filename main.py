from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage
import os
import json
from function import *


if __name__ == '__main__':
    app_id = os.getenv("APP_ID")
    app_secret = os.getenv("APP_SECRET")
    template_id = os.getenv("TEMPLATE_ID")
    weather_key = os.getenv("WEATHER_API_KEY")
    key = os.getenv("XINZUO_API_KEY")

    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)

    f = open("./users_info.json", encoding="utf-8")
    js_text = json.load(f)
    f.close()
    data = js_text['data']
    num = 0
    w1, w2, w3, w4, w5 =fix_words(get_words())
    word1, word2, word3, word4,word5,= fix_words(get_yunshi(key, "cancer"))
    for user_info in data:
        born_date = user_info['born_date']
        birthday = born_date[5:]
        city = user_info['city']
        user_id = user_info['user_id']
        name = user_info['user_name'].upper()
        begin_day = user_info['begin_day']
        

        wea_city,weather = get_weather(city,weather_key)
        
        data = dict()
        data['time'] = {
            'value': get_time(),
        }
        data['lasting_day'] = {
            'value': get_count(begin_day),
        }
        data['name'] = {
            'value': name,
        }
        data['yunshi'] = {
            'value':word1
        }
        data['yunshi2'] = {
            'value':word2
        }
        data['yunshi3'] = {
            'value':word3
        }
        data['yunshi4'] = {
            'value':word4
        }
        data['yunshi5'] = {
            'value':word5
        }
        data['weather'] = {
            'value': weather['text_day'],
        }
        data['city'] = {
            'value': wea_city,
        }
        data['tem_high'] = {
            'value': weather['high'],
        }
        data['tem_low'] = {
            'value': weather['low'],
        }
        data['born_days'] = {
            'value': get_count(born_date),
        }
        data['birthday_left'] = {
            'value': get_birthday(birthday),
        }
        data['wind'] = {
            'value': weather['wind_direction'],
        }

        data['words'] = {
            'value': w1,
        }
        data['words2'] = {
            'value': w2,
        }
        data['words3'] = {
            'value': w3,
        }
        data['words4'] = {
            'value': w4,
        }
        data['words5'] = {
            'value': w5,
        }
        res = wm.send_template(user_id, template_id, data)
        print(data)
        print(res)
        num += 1
    print(f"成功发送{num}条信息")
