#!/usr/bin/python3
'''script that takes in the name of a state as an argument
and lists all cities of that state, using the database '''
if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=args[1], passwd=args[2], db=args[3])

    cursor = connection.cursor()
    cursor.execute('SELECT cities.name\
                   FROM cities LEFT JOIN states ON\
                   cities.state_id = states.id\
                   WHERE states.name = %s', (args[4],))

    result = cursor.fetchall()
    print(", ".join([row[0] for row in result]))
