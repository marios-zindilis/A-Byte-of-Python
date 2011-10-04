#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: continue.py
 
while True:
  s = raw_input('Εισάγετε κάτι: ')
  if s == 'quit':
    break
  if len(s) < 3:
    continue
  print 'Η είσοδος ήταν αρκετά μακριά.'
  # Κάντε ό,τι άλλο θέλετε εδώ...
