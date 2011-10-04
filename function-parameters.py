#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: function-parameters.py
 
def printMax(a, b):
  if a > b:
    print 'Το', a, 'είναι μεγαλύτερο.'
  else:
    print 'Το', b, 'είναι μεγαλύτερο.'
 
printMax(3, 4) # Κλήση με κυριολεκτικές σταθερές ως ορίσματα.
 
x = 5
y = 7
 
printMax(x, y) # Κλήση με μεταβλητές ως ορίσματα.
