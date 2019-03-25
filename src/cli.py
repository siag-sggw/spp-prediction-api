import argparse

DESCRIPTION = """Stock Price Prediction (SPP) API - CLI"""

def create_parser():
    parser = argparse.ArgumentParser(DESCRIPTION)
    parser.add_argument('-c', '--configuration', 
                        help="Path to the configuration file")
    return parser