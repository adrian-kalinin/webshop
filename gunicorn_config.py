bind = '0.0.0.0:8080'

workers = 3
worker_connections = 1000
timeout = 1200

worker_class = 'gevent'
raw_env = 'DJANGO_SETTINGS_MODULE=webshop.settings'
