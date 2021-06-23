import requests
from datetime import datetime

import pandas as pd


def get_coins_list(REF_CUR="eur"):
    r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency={}&order=market_cap_desc&per_page=100&page=1&sparkline=false'.format(REF_CUR))
    return pd.DataFrame(r.json())


def get_coin_infos(id_):
    r = requests.get('https://api.coingecko.com/api/v3/coins/{}'.format(id_))
    return r.json()


def get_coin_histo_price(id_, ref_cur="eur", days="100"):
    """
        Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and
        90 days, Daily data will be used for duration above 90 days
    """
    r = requests.get(
        'https://api.coingecko.com/api/v3/coins/%s/market_chart?vs_currency=%s&days=%s' % (id_, ref_cur, days)
    )

    return {
        "dates": [datetime.fromtimestamp(d[0]/1000).strftime("%Y-%m-%d") for d in r.json()["prices"]],
        "prices": [d[1] for d in r.json()["prices"]]
    }
