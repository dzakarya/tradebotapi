from Trade_api import trade
import json
import time
coin_ob = {
            "name": None,
            "high": None,
            "low": None,
            "vol_idr": None,
            "last": None
        }
jack_api  = {
    "api_key" : "NG2SVWPI-5HGTYM3O-C9BUDHJX-3SY6NSUH-JQYR0TNR",
    "secret_key" : b"3f73833544bf132add6a25d5168869f860d09d87e9191e435a340bed0d35bfc83559ae984353bf7e",
    "balance" : []
}

def get_balance():
    info = trader.getInfo()

    for bal in info["return"]["balance"]:
        if float(info["return"]["balance"][bal]) > 0:
            jack_api["balance"].append([bal+"idr",float(info["return"]["balance"][bal])])

if __name__=="__main__":
    trader = trade(jack_api["api_key"],jack_api["secret_key"])
    get_balance()
    while True:
        cur_val = []
        for coin in jack_api["balance"]:
            temp = {
            "name": None,
            "high": None,
            "low": None,
            "vol_idr": None,
            "last": None
        }
            coin_info = trader.getTicker(coin[0])
            temp["name"] = coin[0]
            temp["last"] = coin_info["last"]
            temp["low"] = coin_info["low"]
            temp["high"] = coin_info["high"]
            temp["vol_idr"] = coin_info["vol_idr"]
            cur_val.append([temp["name"],temp["last"]])
        print (cur_val)
        time.sleep(1)