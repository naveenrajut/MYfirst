#!/bin/python3
import time
import math
import os

# Complete the time_delta function below.
def time_delta(t1, t2):
    time1=int(time.mktime(time.strptime(t1,"%a %d %B %Y %H:%M:%S")))
    time2=int(time.mktime(time.strptime(t2,"%a %d %B %Y %H:%M:%S")))
    t = (time1-time2)
    print(t)
time_delta("Sun 11 May 2015 13:54:36","Sun 10 May 2015 13:54:36")
