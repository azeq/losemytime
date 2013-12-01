#!/usr/bin/python
# coding: utf-8 

import sqlite3 as lite


class DatabaseExecutor:
    def __init__(self, nameOfDatabase, userStatsTable, top, path):
        self.name         = nameOfDatabase
        self.userStats    = userStatsTable
        self.index_bored  = 1
        self.index_number = 1
        self.path         = path
        self.top          = top

    def insertNewVote(self, videoId, getBored, userId):
        print "insertNewVote"
        print "videoId: "+videoId
        print "getBored: "+getBored
        print "userId: "+str(userId)

        valid = False
        con = lite.connect(self.path+'lyt.db')
        with con:
            cur = con.cursor()    
            
            # test if the entry exists
            cur.execute("select exists(select * from "+self.name+" where video_id=? and user_id=?)", (videoId, userId))
            rows = cur.fetchall() # its a list


            if len(rows) == 1:
                row = rows[0] # row is a tuple
                # if the entry exisits, update it        
                # update get bored for a video
                if row[0] == 1:
                    print "update database"
                    cur.execute("update "+self.name+" set get_bored=? where video_id=? and user_id=?", (getBored, videoId, userId))
                    valid = True
                # new entry
                elif row[0] == 0:
                    print "add new entry" 
                    cur.execute("insert into "+self.name+"(video_id, get_bored, user_id) values('"+videoId+"', '"+getBored+"', '"+userId+"')")

                    #increment number of video
                    self.incrementNumber(con, userId)
                    valid = True
                else:
                    valid = False
                    print "error"   
        return valid    

    def computeAllVotes(self, videoId = None):
        if videoId != None:
            con = lite.connect(self.path+'lyt.db')
            with con:
                cur = con.cursor()
                cur.execute("select * from "+self.name+" where video_id=? and get_bored=?", (videoId, 'True'))
                rowsBored = cur.fetchall()

                cur.execute("select * from "+self.name+" where video_id=? and get_bored=?", (videoId, 'False'))
                rowsLiked = cur.fetchall()

                return [len(rowsBored), len(rowsLiked)]
                
    def hasAlreadyVotedForThisVideo(self, videoId, userId):
        con = lite.connect(self.path+'lyt.db')
        with con:
            cur = con.cursor()    
            
            # test if the entry exists
            cur.execute("select * from "+self.name+" where video_id=? and user_id=?", (videoId, userId))
            rows = cur.fetchall() # its a list

            if len(rows) == 1: # the user has already voted
                row = rows[0] # row is a tuple
                return row[self.index_bored] # check his vote
            else:   
                return None # else return None to now that no vote

    def incrementNumber(self, con, userId):
        cur = con.cursor()
        cur.execute("select exists(select * from "+self.userStats+" where user_id=?)", [userId])
        rows = cur.fetchall() # its a list

        if len(rows) == 1:
            row = rows[0]
            if row[0] == 1:
                cur.execute("select * from "+self.userStats+" where user_id=?", [userId])
                entry = cur.fetchall()
                if len(entry) == 1:
                    entry = entry[0] # it is an update
                    n = entry[self.index_number] + 1 # increment
                    cur.execute("update "+self.userStats+" set number=? where user_id=?", (n, userId))
            elif row[0] == 0:
                cur.execute("insert into "+self.userStats+" (user_id, number) values('"+userId+"', '"+str(1)+"')")

    def getRanking(self):
        con = lite.connect(self.path+'lyt.db')
        with con:
            cur = con.cursor()
            cur.execute("select * from "+self.userStats+" order by number DESC")    
            rows = cur.fetchall()
            if len(rows) > 0:
                return rows[:self.top]



