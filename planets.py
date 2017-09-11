# -*- coding: utf-8 -*-
"""
Script by John Wigg
"""

import ephem
import datetime
import time

def get_state(planet):
    data = [0] * 3
    obs.date = datetime.datetime.utcnow()
    data[1] = obs.next_rising(planet)
    data[2] = obs.next_setting(planet)
    if data[1] > data[2]:
        data[0] = True
    else:
        data[0] = False
    return data

obs = ephem.Observer()
obs.lat = '50.9'
obs.long = '11.6'

mercury = ephem.Mercury()
venus = ephem.Venus()
mars = ephem.Mars()
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()
uranus = ephem.Uranus()
neptune = ephem.Neptune()

while 1:
    print(obs.date, "UTC+0")
    print(get_state(mercury))
    print(get_state(venus))
    print(get_state(mars))
    print(get_state(jupiter))
    print(get_state(saturn))
    print(get_state(uranus))
    print(get_state(neptune))
    print("-------------------------------------------------------------------")
    time.sleep(10)
