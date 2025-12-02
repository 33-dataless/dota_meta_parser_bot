from main_parser.mainparser import DotaParser
from util.get_time_now import get_time_now

dotaparser = DotaParser()
response = dotaparser.get_response(link=dotaparser.__link_all_position__)
vector = dotaparser.create_vector(response=response)
dotaparser.print_vector(vector=vector)

# dotaparser.dump_response(response=response, position="5pos", time=get_time_now(format_file=True))

