#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: function-docstrings.py
 
def printMax(x, y):
  '''Επιστρέφει τον μεγαλύτερο από δύο αριθμούς.

  Οι αριθμοί πρέπει να είναι ακέραιοι.'''
  x = int(x) # μετατροπή σε ακέραιο, αν είναι δυνατό.
  y = int(y)
 
  if x > y:
    print 'Το', x, 'είναι μεγαλύτερο.'
  else:
    print 'Το', y, 'είναι μεγαλύτερο.'
 
printMax(3, 5)
print printMax.__doc__
