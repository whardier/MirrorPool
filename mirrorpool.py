#!/usr/bin/env python

import os
import sys

import settings
import proxies
import collectors
import interfaces
import datastores

if __name__ == '__main__':
  import asyncore
  import pprint

  for module in sys.modules:
    try:
      t = getattr(sys.modules[module], 'args')
      print module, t
    except:
      pass

  asyncore.loop()
