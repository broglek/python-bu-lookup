#!/usr/bin/python

from distutils.core import setup, Extension

setup (name = 'BULookup',
       version = '0.2',
       description = 'A trivial interface between python-phquery and various useradd tools.',
       author = "Matthew Miller",
       author_email = 'mattdm@mattdm.org',
       maintainer = "Matthew Miller",
       maintainer_email = 'mattdm@mattdm.org',
       classifiers=['Development Status :: 4 - Beta',
                    'Intended Audience :: System Administrators',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    'Topic :: System :: Systems Administration :: Authentication/Directory'
                    ],
       py_modules = ['BULookup']
       )
