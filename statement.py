from utils import *


def show():
    if txns == 0:
        print(" no Transaction ")
        return
    
    for _ in txns:
        print(_)