from crypto_monitoring.utils.tools import get_coin_infos, get_coin_histo_price


class Crypto:
    id: str
    symbol: str
    name: str
    price: float
    market_cap: float
    ref_cur: str

    def __init__(self, id_, ref_cur="eur"):
        self.id = id_
        self.ref_cur = ref_cur
        infos = get_coin_infos(id_)
        self.symbol = infos["symbol"]
        self.name = infos["name"]
        self.price = infos["market_data"]["current_price"][ref_cur]
        self.market_cap = infos["market_data"]["market_cap"][ref_cur]

    def __repr__(self) -> str:
        return "%s - %s - %s - %s - %s - %s" % (
            self.id, self.symbol, self.name, self.ref_cur, self.price, self.market_cap
        )

    def get_histo_price(self, days):
        return get_coin_histo_price(self.id, self.ref_cur, days)