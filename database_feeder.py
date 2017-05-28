6import pymysql.cursors
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import threading
import time
from itertools import izip_longest

#GLOBAL VARIABLE DECLARATIONS
count = 1

#"Collect data into fixed-length chunks or blocks"
# grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

#Function used for converting text data into relational database record and feeding it to the database
def converter(file_name):
    flag = False
    data_list = []

    with countLock:
        global count
        local_count = count
        count += 2000

    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="mysql123",
                         db="foodreviewdataset",
                         cursorclass=pymysql.cursors.DictCursor)

    with open(file_name,'r') as input_file:
        for word in input_file:
            if word != '\n':
                flag = False
                word = word.rstrip('\n')
                line = word.split(":")
                data_list.append(line[1])
            else:
                print "\n", local_count
                if flag: continue
                flag = True
                try:
                    with db.cursor() as cursor:
                        sql = "INSERT INTO `foods` (`sno`,`productID`,`userID`,`profileName`,`helpfulnes`,`reviewscore`,`time`,`summary`,`text`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql,(local_count,data_list[0],data_list[1],data_list[2],data_list[3],data_list[4],data_list[5],data_list[6],data_list[7]))
                    db.commit()
                finally:
                    print "Data feeded"
                data_list = []
                local_count += 1

    db.close()


n = 18000
fileList = []
with open('sample3.txt','r') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        fileList.append('small_file_{0}.txt'.format(i * n))
        with open('small_file_{0}.txt'.format(i * n), 'w') as fout:
            fout.writelines(g)

startTime = time.time()
countLock = threading.Lock()
pool = ThreadPool(25)
results = pool.map(converter,fileList)
print "Time taken for feeding of data into database is ",time.time() - startTime," seconds"
