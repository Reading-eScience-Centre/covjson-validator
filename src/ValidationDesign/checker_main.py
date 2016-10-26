__author__ = 'Bug'

import argparse

def create_parser(args=None):
    """

    :return: Invocation arguments
    """
    # srg for path to schema if not in default location


    # http://www.alanbriolat.co.uk/optional-positional-arguments-with-argparse.html
    parser = argparse.ArgumentParser(description='All configuration parameters are contained in ./land_cover_config.ini'
                                                 'Use -f switch to override with an alternative file.')

    parser.add_argument('-file', '-f', default=cfg_const.defs['file'], nargs='?',
                        help="Name of configuration file to load")
    parser.add_argument('-test', default='No', nargs='?',
                        help="Run program in test mode, development only")
    return parser.parse_args(args=args)

def main():
    # create main class here and call starter method
    pass

if __name__ == '__main__':
    parse_args = create_parser()
    try:
        main(parse_args)
    except:
        print("EXIT")