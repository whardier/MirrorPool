DATASTORE = "redis"

DATASTORE_URI = "redis://127.0.1.2:6379"

INTERFACES = (
  'cache.icp', #Use Defaults 0.0.0.0:3131
  ('proxy.http', {'port': 8080, 'interface': '127.0.1.2'}),
)

PROXIES = (
  'apple.software.updates',
# 'apple.software.appstore',
# 'apt.software.pool',
# 'rpm.software.pool',
# 'youtube',
# 'hulu',
)

COLLECTORS = (
  'apple.software.updates',
)
