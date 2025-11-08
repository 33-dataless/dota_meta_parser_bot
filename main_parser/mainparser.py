import requests as rq
from util.get_time_now import get_time_now
import json

class DotaParser:
    def __init__(self):
        #TODO доделать остальные линки
        self.__link_all_position__ = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=all&order_by=matches&min_matches=20&period=8&legacy=false"

    def get_winrate_all_position(self, count: int):
        if isinstance(count, int) and 0 < count <= 126:
            data = rq.get(self.__link_all_position__)
            if data.status_code == 200:
                pass
                #TODO do it

