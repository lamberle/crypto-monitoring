from crypto_monitoring.utils.crypto import Crypto
from crypto_monitoring.utils.tools import get_coins_list, get_coin_infos
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # print(get_coin_infos("cardano"))
    # print(get_coin_infos("cardano").keys())
    ada = Crypto("cardano")
    print(ada)
    price_histo = ada.get_histo_price(2)
    plt.plot(price_histo["dates"], price_histo["prices"])
    plt.show()
