import base64
import datetime
import json
from decimal import Decimal
import matplotlib.pyplot as plt
import matplotlib.dates as md
import io


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return json.JSONEncoder.default(self, obj)


def plot(records):
    # plt.subplots_adjust(bottom=0.2)
    # plt.xticks(rotation=25)
    # ax = plt.gca()
    # xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    # ax.xaxis.set_major_formatter(xfmt)
    # ax.set_ylabel('Počet hráčů', rotation=90, color='k', labelpad=15)

    dates = [datetime.datetime.fromisoformat(record['timestamp']) for record in records]
    players_count = [record['currentPlayerCount'] for record in records]

    fig = plt.figure(figsize=(19.2, 10.8))
    plt.suptitle("Demona - Návštěvnost", fontsize=36)
    plt.title(f"Aktuálně hraje hráčů: {players_count[len(players_count) - 1]}, Aktualizováno: {dates[len(dates) - 1].strftime('%H:%M:%S')}", fontsize=24)
    plt.xlabel("Datum", fontsize=24)
    plt.ylabel("Počet hráčů", fontsize=24)
    plt.xticks(fontsize=18, rotation=45)
    plt.yticks(fontsize=18)
    plt.subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M'))
    plt.plot(dates, players_count, linewidth=0.7)

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')

    return img_buf.getvalue()