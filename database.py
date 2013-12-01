#!/usr/bin/python
# coding: utf-8 

import sqlite3 as lite
import pdb

nameOfDatabase = u"videovote"
index_bored = 1; # index in the sql base

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
            
def hasAlreadyVotedForThisVideo(videoId, userId):
    con = lite.connect('lyt.db')
    with con:
        cur = con.cursor()    
        
        # test if the entry exists
        cur.execute("select * from "+nameOfDatabase+" where video_id=? and user_id=?", (videoId, userId))
        rows = cur.fetchall() # its a list

        if len(rows) == 1: # the user has already voted
            row = rows[0] # row is a tuple
            return row[index_bored] # check his vote
        else:   
            return None # else return None to now that no vote




