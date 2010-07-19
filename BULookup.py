#!/usr/bin/python

## BULookup.py - uses phquery to look up user info given a username
## Copyright (C) 2003 Matthew Miller
## A few minor updates, 11/29/2005 John N. Laliberte <allanonjl@gentoo.org>
## - restructured some of the logic to use map,lambda f(x)'s,reverse,etc.
## - added small section so the module can be tested by itself.

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import string
import phquery
import sys
DEBUG=False

def getIDAndFullName(username):

	try:
		phinfo = phquery.query('ns8.bu.edu','alias',username)
	except:
		raise Exception, "getIDAndFullName: %s" % (sys.exc_info()[1])

	# the result should only be ONE unique person!
	if 1 < len(phinfo):
		if DEBUG: print "Number of results: %s \n Results: %s " % (str(phinfo.count),str(phinfo))
		return(-1, "For some reason, the user alias is not unique!")


	try:
                person = phinfo[0].information
	except:
                raise Exception, "Unknown User"

	nameparts = string.split(person['name'],",")

	stripw = lambda part_of_name: string.strip(part_of_name)
	nameparts = map(stripw, nameparts)

#	nameparts.reverse()
        
	fullname = string.join([string.join(nameparts[1:]), nameparts[0]])

	userid = string.atoi(person['index_id'][1:])

	return (userid,fullname)

# Allows you to test this module by itself.
# Example: python BULookup.py allanonl
if __name__=='__main__':
	DEBUG=True
	(userid,fullname) = getIDAndFullName(sys.argv[1])
	print userid,fullname
