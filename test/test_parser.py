from pars.mainparser import Parser

class TestParser:
    def test_parser():
        parser = Parser()
        parser.request_html_code()

if __name__ == '__main__':
    test_parser = TestParser
    test_parser.test_parser()

