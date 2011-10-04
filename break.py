#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: break.py
 
while True:
  s = raw_input('Εισάγετε κάτι: ')
  if s == 'quit':
    break
  print 'Το μήκος της συμβολοσειράς είναι:', len(s)
print 'Τέλος.'
