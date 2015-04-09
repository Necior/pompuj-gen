#!/usr/bin/env python

import datetime
import gspread
import pygal

import config

gc = gspread.login(config.login, config.password)
wks = gc.open(config.sheet_name).sheet1

names2reps = []
for i in range(config.starting_row, config.ending_row+1):
    names2reps.append((wks.cell(i, 1).value, int(wks.cell(i, 2).value)))

title = datetime.datetime.now().strftime('Last update: %d %b @ %H:%M')
bar_chart = pygal.Bar(title=title, style=pygal.style.DarkSolarizedStyle)

for name, reps in names2reps:
    bar_chart.add(name, [reps])

bar_chart.render_to_file(config.svg_path)
