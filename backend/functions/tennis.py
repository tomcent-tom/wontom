import requests
import re
import datetime
import json
import time
import logging

def log_in(session):
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    payload = "first_name=Tom&email=tom.hh.evers%40gmail.com&remember=1"
    session.post(
        'https://jensenstennis.intrac.com.au/tennis/login.cfm?return=clubevent.cfm?event=13408', headers=header,
        data=payload)


def get_tennis_data():
    logging.info("starting tennis data fetching")
    # fetch raw data
    r = requests.get('https://jensenstennis.intrac.com.au/tennis/event.cfm?type=4&title=Class#a13408')
    text = r.text

    # transform into list of games
    games_regex = re.findall("event=[0-9]+", text)
    games = [e[6:] for e in games_regex]
    session = requests.Session()
    first = True
    game_infos = []
    i = 1
    for game in games:
        if first:
            first = False
            log_in(session)
        try:
            result = session.get('https://jensenstennis.intrac.com.au/tennis/clubevent.cfm?event={}'.format(game))


            if result.status_code != 200:
                log_in(session)
                print("waiting 1 second")
                time.sleep(1)
                result = session.get('https://jensenstennis.intrac.com.au/tennis/clubevent.cfm?event={}'.format(game))
                if result.status_code != 200:
                    raise Exception()

            game_info_regex = re.findall("Class: .* \| .* \|[A-z ]+", result.text)[0]

            dates = re.findall("<tr>.*[0-9]+ [A-z]{3} [0-9]+.*", result.text)
            for available_date in dates:
                game_info = {
                    'level': re.findall("Class: [A-z 0-9 \/\-]+ \|", game_info_regex)[0][7:-2],
                    'time': re.findall("[A-z0-9\:]+-[A-z0-9\: ]+[A-z]{2}", game_info_regex)[0],
                    'place': re.findall("\|[A-z ]+", game_info_regex)[1][2:-1]
                }
                remaining_regex = re.findall("([0-9]+ spots available)", available_date)
                if len(remaining_regex) > 0:
                    remaining = str(int(remaining_regex[0][:1]))
                else:
                    remaining = '0'
                game_info['remaining'] = remaining

                date_regex = re.findall("[0-9]+ [A-z]+ [0-9]+", available_date)[0]
                date = datetime.datetime.strptime(date_regex, '%d %b %Y').date().strftime("%Y-%m-%d")
                game_info['date'] = date
                game_info['id'] = i
                game_info['game'] = game
                game_infos.append(game_info)
                i +=1
        except Exception as e:
            if result.status_code != 200:
                print("http error: {} for id {}".format(result.status_code, game))
            else:
                raise e

    with open('/Users/tom/Projects/Wontom/backend/cache/availabilities.json', 'w+') as file:
        json.dump(game_infos, file)

if __name__ == "__main__":
    get_tennis_data()