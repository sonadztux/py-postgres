import sys
import psycopg2
from decouple import config

host = config('HOST')
dbname = config('DBNAME')
user = config('USERNAME')
password = config('PASSWORD')
sslmode = 'require'

conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)

if not conn.closed:
    print('[OK] Connection established')
else:
    print('[!] Connection failed')
    sys.exit()