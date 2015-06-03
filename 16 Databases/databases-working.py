#!/usr/bin/python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row  # allow you to specify how row returns from cursor
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')
    db.execute('insert into test(t1,i1) values(?,?)',('one',1))
    db.execute('insert into test(t1,i1) values(?,?)',('two',2))
    db.execute('insert into test(t1,i1) values(?,?)',('three',3))
    db.execute('insert into test(t1,i1) values(?,?)',('four',4))
    db.commit()
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        # print (row)
        # print(dict(row))
        print(row['t1'],row['i1'])


if __name__ == "__main__": main()
