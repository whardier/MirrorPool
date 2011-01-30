DATASTORE = ("redis", {'host': '127.0.1.2', 'port': 6379})

INTERFACES = (
  'cache.icp', 
  ('proxy.http', {'port': 8080, 'interface': '127.0.1.2'}),
)

PROXIES = (
  ('apple.software.updates', {'watch': True}),
# 'apple.software.appstore',
# 'apt.software.pool',
# 'rpm.software.pool',
# 'youtube',
# 'hulu',
)

COLLECTORS = (
  'apple.software.updates',
)
