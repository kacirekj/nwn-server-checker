import requests
import re


def get_current_server_stats():
    response = requests.get("https://iscandar.ch/server.php?ip=3.64.204.102&port=5121&template=black&font=classic")
    groups = re.findall(r'(.*?)(Players.*?>)(.*?)(\/)(.*?)(<\/)', response.text)
    print(groups)
    return {
        'currentPlayerCount': int(groups[0][2]),
        'maxPlayerCount': int(groups[0][4]),
    }

