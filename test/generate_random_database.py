#!/usr/bin/python
# coding: utf-8 

import sys
import random
sys.path.append('/Users/Paul/Applications/git/losemytime')
from database import DatabaseExecutor

videoUUID = ['a', 'b', '3', '5', '9', 'p', '-', 'v']
userID = ['12335253242', '23545432', '425121664232', '566563433', '44543542321', '16543254523']
bored = ['True', 'False']

nameOfDatabase = u"videoVoteForTest"
userDatabase = u"userStatsForTest"

def fillRamdomly(dbExecutor):
    userIds = createFakeUserId(15)
    print userIds
    for i  in range(50):
        videoId = ''
        for j in range(11):
            videoId += random.choice(videoUUID)
        getBored = random.choice(bored)
        userId = random.choice(userIds)
        dbExecutor.insertNewVote(videoId, getBored, userId)

def createFakeUserId(number):
    li = list()
    for k in range(number):
        userId = ''
        for j in range(10):
            userId += str(random.choice(range(10)))
        li.append(userId)
    return li

if __name__ == '__main__':
    dbExec = DatabaseExecutor(nameOfDatabase, userDatabase, 3, '/Users/Paul/Applications/git/losemytime/')
    #fillRamdomly(dbExec)
    print dbExec.getRanking()