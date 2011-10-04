#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: function-locals.py
 
def func(x):
  print 'Το x είναι:', x
  x = 2
  print 'Το x άλλαξε μέσα στη συνάρτηση σε:', x
 
x = 50
func(x)
print 'Έξω από τη συνάρτηση το x είναι πάλι:', x
