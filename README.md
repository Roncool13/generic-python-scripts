# generic-python-scripts
Repo for generic multi-purpose python scripts.

# database_feeder.py
Script for feeding sample data directly into database. I was searching around the net for script for this purpose but didn't find it, so made one to help others like me.

Format for Sample Data:-
product/productId: B001E4KFG0
review/userId: A3SGXH7AUHU8GW
review/profileName: delmartian
review/helpfulness: 1/1
review/score: 5.0
review/time: 1303862400
review/summary: Good Quality Dog Food
review/text: I have bought several of the Vitality canned dog food products and have found them all to be of good quality.\n

Database Table Schema:-
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| sno         | int(11)      | NO   | PRI | NULL    |       |
| productID   | longtext     | NO   |     | NULL    |       |
| userID      | longtext     | NO   |     | NULL    |       |
| profileName | longtext     | NO   |     | NULL    |       |
| helpfulness | longtext     | NO   |     | NULL    |       |
| reviewscore | decimal(2,1) | NO   |     | NULL    |       |
| time        | longtext     | NO   |     | NULL    |       |
| summary     | longtext     | NO   |     | NULL    |       |
| text        | longtext     | NO   |     | NULL    |       |
| score       | decimal(5,4) | YES  |     | 0.0000  |       |
+-------------+--------------+------+-----+---------+-------+

NOTE:- Number of columns can be modified according to needs.
