#! /usr/bin/python

#Compare 4 arrays(lists)

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
b = [ 2, 4, 6, 8, 10, 12, 14, 16, 18 ]
c = [ 3, 6, 9, 12, 15, 18 ]
d = [ 6, 12, 18 ]


print set(a) & set(b) & set(c) & set(d)