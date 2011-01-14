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

  pprint.pprint(sys.modules)

  asyncore.loop()
