#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
try:
    con = mdb.connect('localhost', 'PScrape', 'PASSWORD_HERE', 'wb');
    print(con)
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s " % ver
    
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
with con:
    a,b,c,d,e = 1,2,3,4,5
    cur = con.cursor()
    name_list=[u'MATH 16A', u'CS 70', u'EE 20N', u'EE 40', u'PHYSICS 7B', u'CS 169', u'PHYSICS 7A', u'CS 10', u'CS 61B', u'CS 61C', u'CHEMISTRY 1A']
    for c in name_list:
        print(str(c))
        print(c.split())
        c=c.split()
        print("".join(c))
        c=str("".join(c))
        cur.execute("CREATE TABLE %s (Id INT PRIMARY KEY AUTO_INCREMENT,Date datetime, Quest varchar(50), Contrib varchar(50), ins_resp varchar(50), stud_resp varchar(50), avg_resp_time varchar(50))" str(c))
        
    #cur.execute("CREATE TABLE PData (Id INT PRIMARY KEY AUTO_INCREMENT,Date datetime, Quest varchar(50), Contrib varchar(50), ins_resp varchar(50), stud_resp varchar(50), avg_resp_time varchar(50))")
    
    cur.execute("INSERT INTO PData (Date,Quest,Contrib,ins_resp,stud_resp,avg_resp_time) VALUES(NOW(),'0','0','0','0','0')")
    #cur.execute("INSERT INTO PData (Date,Quest,Contrib,ins_resp,stud_resp,avg_resp_time) VALUES(NOW(),%s,%s,%s,%s,%s)",(a,b,c,d,e))

    #NEED A FIND A WAY TO CONNECT TO DB AND ADD TO IT.
