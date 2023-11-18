#!/usr/bin/python3
'''safe list of all rows'''
if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=args[1], passwd=args[2], db=args[3])

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM states WHERE name = %s', (args[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
