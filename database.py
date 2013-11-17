#!/usr/bin/python
# coding: utf-8 

import sqlite3 as lite

def insertNewVote(videoId, getBored, userId):
    con = lite.connect('lyt.db')

    print "insertNewVote"
    print "videoId: "+videoId
    print "getBored: "+getBored
    print "userId: "+str(userId)

    with con:
        cur = con.cursor()    
        
        # test if the entry exists
        cur.execute("select exists(select * from videovote where video_id=? and user_id=?)", (videoId, userId))
        rows = cur.fetchall() # its a list

        if len(rows) == 1:
            row = rows[0] # row is a tuple

            # if the entry exisits, update it        
            # update get bored for a video
            if row[0] == 1:
                print "update database"
                cur.execute("update videovote set get_bored=? where video_id=? and user_id=?", (getBored, videoId, userId))
            # new entry
            elif row[0] == 0:
                print "add new entry" 
                cur.execute("insert into videovote(video_id, get_bored, user_id) values('"+videoId+"', '"+getBored+"', '"+userId+"')")
            else:
                print "error"       

    # lid = cur.lastrowid
    # print "The last Id of the inserted row is %s" % lid

        cur.execute("SELECT * FROM videovote")
        rows = cur.fetchall() # its a list

        for row in rows:
            print row
