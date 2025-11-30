from main_parser.mainparser import DotaParser
from util.get_time_now import get_time_now

dotaparser = DotaParser()
dotaparser.dump_response(get_time_now(format_file=True))
