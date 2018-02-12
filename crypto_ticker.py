import requests

def get_data_koinex():
    price = {}
    url = 'https://koinex.in/api/ticker'
    return requests.get(url).json()


if __name__ == '__main__':
    data = get_data_koinex()
    print "Bitcoin " + data['prices']["BTC"]
    print "Etherium " + data['prices']["ETH"]
    print "Ripple " + data['prices']["XRP"]