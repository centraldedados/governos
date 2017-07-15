#!/usr/bin/python3

import re
import csv

old_file = csv.reader(open("governos-cargos.csv", encoding="utf-8"))
new_file = csv.writer(open("novos-governos-cargos.csv", "w", encoding="utf-8"))

for line in old_file:
	new_line = []
	cell_counter = 0
	for cell in line:
		if cell_counter == 4 or cell_counter == 5:
			cell = re.sub(r'(\d{2})-(\d{2})-(\d{4})',r'\3-\2-\1',cell)
		
		new_line.append(cell) 
		cell_counter += 1

	new_file.writerow(new_line)
