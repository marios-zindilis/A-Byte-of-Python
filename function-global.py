#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: function-global.py
 
def func():
  global x
 
  print 'Το x είναι:', x
  x = 2
  print 'Το x αλλάχτηκε και εκτός συνάρτησης σε:', x
 
x = 50
func()
print 'Το x εκτός συνάρτησης είναι:', x
