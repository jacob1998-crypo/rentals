from djangodb import connection

with connection.cursor() as cursor:
    cursor.execute("SET time_zone = 'Africa/Nairobi'")