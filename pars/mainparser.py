import bs4
import requests
from selenium import webdriver as wd


class Parser:
    def __init__(self) -> None:
        self.__st_accept__ = "text/html"
        self.__st_useragent__ = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
        self.headers = {
            "Accept": self.__st_accept__,
            "User-Agent": self.__st_useragent__
        }

    def request_html_code(self):
        req = requests.get("https://dota2protracker.com/", self.headers)
        src = req.text
        return src
    
class ReadParser(Parser):
    def __init__(self) -> None:
        pass

    
