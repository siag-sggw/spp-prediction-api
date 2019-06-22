import argparse

DESCRIPTION = """Stock Price Prediction (SPP) API - CLI"""


def create_parser():
    parser = argparse.ArgumentParser(DESCRIPTION)
    parser.add_argument('-c', '--configuration',
                        help="Path to the configuration file")
    parser.add_argument('-p', '--model-directory',
                        help="Path to the directory containing models")
    return parser
