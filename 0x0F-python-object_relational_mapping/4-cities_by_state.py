#!/usr/bin/python3
'''lists all cities from the database'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=args[1], passwd=args[2], db=args[3])

    cursor = connection.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name\
                   FROM cities LEFT JOIN states ON\
                   cities.state_id = states.id\
                   ORDER BY states.id')

    result = cursor.fetchall()
    for row in result:
        print(row)
