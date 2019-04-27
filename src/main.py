import src.cli

from src.application import SPPApi
from src.config import Config
from src.routing import DictRouteBuilder

import os


if __name__ == "__main__":
    # Create parser and get user args
    args = src.cli.create_parser() \
              .parse_args()

    # Load application configuration
    config = Config().load(args.configuration)
    
    # Start the application
    SPPApi(config, DictRouteBuilder(config.routes)).run()
