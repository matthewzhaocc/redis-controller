import redis
connection = redis.Redis(
    host='10.20.0.37',
    port=6379,
    password='D4c6Ga5qE4dl230zRfsWpxpBkcGGSI3eWbrXa4j0JQ01zwYXRZB9vow75pD+5R9MZsLfiBP+t5t1fWgn'
)
connection.set('test','hello')
print(connection.get('test'))