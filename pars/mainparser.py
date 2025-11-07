import requests as rq
from util.get_data_env import get_stratz_api_env
from util.get_time_now import get_time_now
from typing import Dict
import json

class DotaParser:
    def __init__(self) -> None:
        self.__graphql_endpoint__ = 'https://api.stratz.com/graphql'
        self.header = {"user-agent": "STRATZ_API",
                       "Authorization": f"Bearer {get_stratz_api_env()}",
                       "Content-Type": "application/json"}

    def send_query(self, query: str, save_as_json=False) -> Dict | None:
        response = rq.post(url=self.__graphql_endpoint__, headers=self.header, json={"query": query})
        if response.status_code == 200:
            if save_as_json:
                time = get_time_now()
                with open(f'D:\\pyproject\\DotaParser\\data\\AnswerQuery_{time}', 'w', encoding='utf-8') as file:
                    json.dump(response.json(), file, indent=4, ensure_ascii=False)
                    print(f'query saved in DotaParser\data\AnswerQuery_{time}')
                    return None
            else:
                return response.json()
        else:
            raise Exception(response.status_code)

