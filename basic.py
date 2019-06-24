import time

def sleep_timer(a,b):
    time.sleep(random.randint(a,b))

from difflib import SequenceMatcher

def match_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()

    ### TEST TEST
