from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
import location_g as loc
from calcu import *
import zodiaclist
import window2
from window import person_




print(type(person_), type(person_.dat()))
bdate = person_.dat()
btime = person_.tim()
bplace = person_.pla()
bzone = person_.zon()

bplace = loc.loco(bplace)

birthdate = Datetime(bdate, btime, bzone)
birthplace = GeoPos(bplace.split()[0], bplace.split()[1])

chart = Chart(birthdate, birthplace)

year = int(bdate[:4])

zodiac ={'lagna' : trotosid(chart.get(const.ASC).lon, year), 'sun' : trotosid(chart.get(const.SUN).lon, year),
'moon' : trotosid(chart.get(const.MOON).lon, year),
'mars' : trotosid(chart.get(const.MARS).lon, year), 'jupiter' : trotosid(chart.get(const.JUPITER).lon, year),
'mercury' : trotosid(chart.get(const.MERCURY).lon, year),
'venus' : trotosid(chart.get(const.VENUS).lon, year),
'saturn' : trotosid(chart.get(const.SATURN).lon, year), 
'rahu' : trotosid(chart.get(const.NORTH_NODE).lon, year), 
'ketu' : trotosid(chart.get(const.SOUTH_NODE).lon, year)}


ephemtable = [['Planets', 'Sign', 'Longitude', 'Nakshatra', 'Pada']]

for i in zodiaclist.planets_: 
    ephemtable.append([i.capitalize(), degree_to_zodiac(zodiac[i])[0], degree_to_zodiac(zodiac[i])[1], get_nakshatra(zodiac[i])[0], get_nakshatra(zodiac[i])[1]])


window2.distablewind(ephemtable)
