from pars.mainparser import DotaParser

query = '''
heroStats {
    winWeek(positionIds:POSITION_1, gameModeIds:ALL_PICK {
        heroId,
        winCount,
        matchCount,
        },
    }
}    
'''

def get_query():
    dota_parser = DotaParser()
    return dota_parser.send_query(query, save_as_json=False)

def save_query() -> None:
    dota_parser = DotaParser()
    return dota_parser.send_query(query, save_as_json=True)

if __name__ == "__main__":
    get_query()
    print("=" * 15)
    save_query()
