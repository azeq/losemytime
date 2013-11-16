#!/usr/bin/python
# coding: utf-8 

import sqlite3 as lite
import sys

def insertNewVote(videoId, getBored, userId):
    con = lite.connect('lyt.db')

    print videoId
    print getBored
    print userId

    with con:
        cur = con.cursor()    
        #cur.execute("INSERT INTO videovote VALUES("+videoId+","+getBored+","+userId+");")
        # cur.execute("INSERT INTO videovote(video_id) VALUES ("+videoId+")")
        # cur.execute("INSERT INTO videovote(get_bored) VALUES ("+getBored+")")
        # cur.execute("INSERT INTO videovote(user_id) VALUES ("+userId+")") 

        # cur.execute("INSERT INTO videovote(video_id) VALUES ('ffff')")
        # cur.execute("INSERT INTO videovote(get_bored) VALUES (TRUE)")
        # cur.execute("INSERT INTO videovote(user_id) VALUES ('ddd')")

        # cur.execute('insert into videovote values (?,?,?,?,?)', ['ffff', 'TRUE', 'ddd', '3'])
        cur.execute("insert into videovote(video_id, get_bored, user_id) values('"+videoId+"', '"+getBored+"', '"+userId+"')")

        lid = cur.lastrowid
        print "The last Id of the inserted row is %s" % lid

        cur.execute("SELECT * FROM videovote")

        rows = cur.fetchall()

        for row in rows:
            print row