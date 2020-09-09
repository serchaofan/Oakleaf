import argparse
from modules import get, run


class CLI():
    def __init__(self, callback=None):
        self.parser = argparse.ArgumentParser(
            prog="oakleaf", description="Oakleaf")
        self.callback = callback
