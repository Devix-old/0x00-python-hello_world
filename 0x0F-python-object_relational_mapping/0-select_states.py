#!/usr/bin/python3
'''print all states'''
if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=args[1], passwd=args[2], db=args[3])

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    states = cursor.fetchall()
    for state in states:
        print(state)
