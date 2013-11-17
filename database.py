#!/usr/bin/python
# coding: utf-8 

import sqlite3 as lite

nameOfDatabase = u"videovote"

def insertNewVote(videoId, getBored, userId):
    print "insertNewVote"
    print "videoId: "+videoId
    print "getBored: "+getBored
    print "userId: "+str(userId)

    valid = False
    con = lite.connect('lyt.db')
    with con:
        cur = con.cursor()    
        
        # test if the entry exists
        cur.execute("select exists(select * from "+nameOfDatabase+" where video_id=? and user_id=?)", (videoId, userId))
        rows = cur.fetchall() # its a list

        if len(rows) == 1:
            row = rows[0] # row is a tuple
            # if the entry exisits, update it        
            # update get bored for a video
            if row[0] == 1:
                print "update database"
                cur.execute("update "+nameOfDatabase+" set get_bored=? where video_id=? and user_id=?", (getBored, videoId, userId))
                valid = True
            # new entry
            elif row[0] == 0:
                print "add new entry" 
                cur.execute("insert into "+nameOfDatabase+"(video_id, get_bored, user_id) values('"+videoId+"', '"+getBored+"', '"+userId+"')")
                valid = True
            else:
                valid = False
                print "error"   
    return valid    

    # lid = cur.lastrowid
    # print "The last Id of the inserted row is %s" % lid

    # cur.execute("SELECT * FROM "+nameOfDatabase)
    # rows = cur.fetchall() # its a list

    # for row in rows:
    #     print row

def computeAllVotes(videoId = None):
    if videoId != None:
        con = lite.connect('lyt.db')
        with con:
            cur = con.cursor()
            cur.execute("select * from "+nameOfDatabase+" where video_id=? and get_bored=?", (videoId, 'True'))
            rowsBored = cur.fetchall()

            cur.execute("select * from "+nameOfDatabase+" where video_id=? and get_bored=?", (videoId, 'False'))
            rowsLiked = cur.fetchall()

            return [len(rowsBored), len(rowsLiked)]
            
            # print len(rowsBored)
            # print len(rowsLiked)

