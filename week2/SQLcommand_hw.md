## Querying a SQL Database

In this challenge you are given a SQL database with data inside. You will need to mine it for important information.

Open it up in terminal by typing
```bash
$ sqlite3 sitemetrics.db
```
To see the existing tables and columns, use the .schema command. Map this by hand or on SQL designer so you have a greater understanding of what we're working with.

#### Answer the following questions in this file, with the results and the sql you wrote to get it.
-------------

##### How many people are from California?  14

SELECT COUNT(*) FROM users WHERE state="CA";

##### Who has the most page views? How many do they have, and where are they from?  Edison Mcintyre 19,937 Mauriceville|ME

SELECT MAX(page_views) FROM users 

 SELECT name, page_views FROM users WHERE page_views = (SELECT max (page_views) FROM users);
Edison Mcintyre|19937

##### Who has the least page views? How many do they have and where are they from?   Hattie Ross  16   Hubbard|MA

sqlite> SELECT name, page_views FROM users WHERE page_views = (SELECT min (page_views) FROM users);
Hattie Ross|16

sqlite> SELECT MIN(page_views) FROM users;
16
sqlite> SELECT * FROM users WHERE page_views=16

##### Who are the most recent visitors to the site?(at least 3)

sqlite> SELECT last_visit, name FROM users ORDER BY last_visit DESC LIMIT 5;          
2014-10-08|Otha Ortiz
2014-10-08|Selina Hardy
2014-10-08|Terrance Allen
2014-10-07|Anderson Hodges
2014-10-06|Delmer Ibarra

SELECT last_visit FROM users ORDER BY last_visit DESC LIMIT 5;


##### Who was the first visitor?

2013-10-08|Woodrow Duffy


##### Who has an email address with the domain 'horse.edu'?

sqlite> SELECT name,email FROM users WHERE email LIKE '%horse.edu%';
Fern Byers|lino.jarod@hornhorse.edu
Valentine Gonzales|steve.louis.jeremy@horse.edu

##### How many people are from the city Graford?

sqlite> SELECT COUNT(*) city FROM users WHERE city='Graford';
3

sqlite> SELECT name,city FROM users WHERE city='Graford'
   ...> ;
Nelly Beach|Graford
Corinne Patton|Graford
Paulina Rankin|Graford



##### What are the names of all the cities that start with the letter V, in alphabetical order?

sqlite> SELECT city FROM users WHERE city LIKE 'V%' ORDER BY city ASC 
   ...> ;
Valley View
Valley View
Van
Van
Vega
Victoria
Victoria


##### What are the names and home cities for people searched for the word "drain"?
 
SELECT name,city,search_terms.word FROM users JOIN user_searches ON user_searches.user_id=users.id 
JOIN search_terms ON search_terms.id=user_searches.term_id WHERE search_terms.word='drain';


Nelly Beach|Graford|drain
Penelope Stein|Runaway Bay|drain
Tisha Gill|Bausell and Ellis|drain
Rolando Crowley|Buda|drain


##### How many times was "trousers" a search term?

 SELECT COUNT(*) FROM search_terms JOIN user_searches ON user_searches.term_id=search_terms.id WHERE search_terms.word='trousers';
2

SELECT users.name,user_searches.user_id,search_terms.word FROM users JOIN user_searches ON users.id=user_searches.user_id JOIN search_terms 
ON search_terms.id=user_searches.term_id WHERE search_terms.word='trousers';


##### What were the search terms used by visitors who last visited on August 22 2014?

sqlite> SELECT search_terms.word,name,last_visit FROM users JOIN user_searches ON user_searches.user_id=users.id 
JOIN search_terms ON search_terms.id=user_searches.term_id WHERE users.last_visit='2014-08-22';

sweet|Damien Grace|2014-08-22
or|Damien Grace|2014-08-22
left|Damien Grace|2014-08-22
word|Damien Grace|2014-08-22
female|Damien Grace|2014-08-22
ball|Dennis Velazquez|2014-08-22


##### What was the most frequently used search term by people from Idaho?




##### What is the name of user 391, and what are his search terms?

sqlite> SELECT users.id,name,search_terms.word FROM users JOIN search_terms ON search_terms.id=user_searches.term_id 
JOIN user_searches ON user_searches.user_id=users.id WHERE users.id=391;

391|Stan Alston|ornament
391|Stan Alston|heat
391|Stan Alston|sex
391|Stan Alston|secret
391|Stan Alston|dry