#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: using-sys.py
 
import sys
 
print 'Τα ορίσματα από τη γραμμή εντολών είναι:'
for i in sys.argv:
  print i

print '\n\nΗ μεταβλητή περιβάλλοντος PYTHONPATH είναι:', sys.path, '\n'
