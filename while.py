#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: while.py
 
number = 23
running = True
 
while running:
  guess = int(raw_input('Εισάγετε έναν ακέραιο: '))
 
  if guess == number:
    print 'Συγχαρητήρια, το πετύχατε!'
    running = False # Αυτό προκαλεί διακοπή του βρόχου
  elif guess < number:
    print 'Χμ, δοκιμάστε έναν μεγαλύτερο ακέραιο.'
  else:
    print 'Χμ, δοκιμάστε έναν μικρότερο ακέραιο.'
else:
  print 'Ο βρόχος while ολοκληρώθηκε.'
  # Εδώ μπορείτε να βάλετε όποιες άλλες εντολές θέλετε...
 
print 'Τέλος.'
