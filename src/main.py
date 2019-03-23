import cli

from application import TornadoApplication
from config import JsonConfigLoader
from routing import DictRouteBuilder

import os


if __name__ == "__main__":
    # Create parser and get user args
    args = cli.create_parser() \
              .parse_args()

    # Load application configuration
    config = JsonConfigLoader(args.configuration).load()

    # Get the application routes
    routes = config['networking']['routes']
    
    # Start the application
    TornadoApplication(config, DictRouteBuilder(routes)).run()