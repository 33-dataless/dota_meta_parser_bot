import requests as rq
import json

class DotaParser:
    def __init__(self):
        self.__link_all_position__ = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=all&order_by=matches&min_matches=20&period=8&legacy=false"

    
    def dump_response(self, time: str):
        with open(f"D:\\pyproject\\DotaParser\\main_parser\\response\\all_position_{time}.json", "w") as file:
            json.dump(rq.get(self.__link_all_position__).text, file, ensure_ascii=False, indent=4)

    @staticmethod
    def log(jdata, id):
        print(f"""id героя - {jdata[id]["hero_id"]} | name - {jdata[id]["hero_name"]} | аспект - {jdata[id]["hero_variant"]} | {jdata[id]["facet_name"]} 
            mathes - {jdata[id]["matches"]} | wins - {jdata[id]["wins"]}, | winrate - {jdata[id]["contest_rate"]}""")
        
    

    def get_winrate_all_position(self):
        data = rq.get(self.__link_all_position__)
        if data.status_code == 200:
            jdata = json.loads(data.text)
            id = -1
            while True:
                id += 1
                if jdata[id]["facet_name"] == 'Shadowhawk':
                    self.log(jdata, id)
                    break
                else:
                    self.log(jdata, id)
                   
