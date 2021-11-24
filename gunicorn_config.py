bind = '127.0.0.1:8080'
workers = 2
worker_connections = 1000
timeout = 1200
worker_class = 'gevent'
raw_env = 'DJANGO_SETTINGS_MODULE=webshop.settings'
