import argparse as cli


from application import TornadoApplication
from config import JsonConfigLoader
from routing import FileRouteBuilder


if __name__ == "__main__":
    # Load application configuration
    config = JsonConfigLoader('./app.json').load()

    # Start the application
    TornadoApplication(config).run()