import requests as rq
from requests import Response
import json

class DotaParser:
    link_all_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=all&order_by=matches&min_matches=20&period=8&legacy=false"
    link_1pos_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=pos%201&order_by=matches&min_matches=20&period=8&legacy=false"
    link_2pos_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=pos%202&order_by=matches&min_matches=20&period=8&legacy=false"
    link_3pos_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=pos%203&order_by=matches&min_matches=20&period=8&legacy=false"
    link_4pos_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=pos%204&order_by=matches&min_matches=20&period=8&legacy=false"
    link_5pos_position = "https://dota2protracker.com/api/heroes/stats?mmr=7000&position=pos%205&order_by=matches&min_matches=20&period=8&legacy=false"

    def get_response(self, link: str) -> Response:
        return rq.get(link)
    
    """for debug"""
    @staticmethod
    def print_vector(vector: list):
        for elem in vector:
            print(elem)

    def get_winrate(self, wins, matches):
        return (wins/matches)*100

    def create_vector(self, response: Response):
        status_code = response.status_code
        if status_code == 200:
            data = json.loads(response.text)
            id = 0
            vector = []
            for data in data:
                vector.append([id, data["hero_id"], data["hero_name"], data["d2pt_rating"], data["facet_name"], data["matches"], data["wins"], data["position"], data["updated_at"]])
                id += 1
            else:
                vector = sorted(vector, key=lambda row: row[3], reverse=True)[0:10]        
                answer = []
                for elem in vector:
                    winrate = self.get_winrate(elem[6] ,elem[5])
                    answer.append([elem[2], elem[3], elem[4], int(winrate), elem[-1]])
                else:
                    return answer      
        else:  
            print(f"error | status code > {status_code}")
            return None
    
    """for debug"""
    @staticmethod
    def dump_response(time: str, position: str, response: Response):
        with open(f"D:\\pyproject\\DotaParser\\main_parser\\response\\{position}_{time}.json", "w") as file:
            json.dump(response.text, file, ensure_ascii=False, indent=2)

    


                   
