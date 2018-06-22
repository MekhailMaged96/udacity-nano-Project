# !/usr/bin/env python3

import psycopg2
import time
# DataBase Name that you want to connect
DBNAME = "news"
# three queries
query1 = (
       "select articles.title, count(*) as views "
       "from articles inner join log on log.path "
       "like concat('%', articles.slug, '%') "
       "where log.status like '%200%' group by "
       "articles.title, log.path order by views desc limit 3")
query2 = (
       "select authors.name, count(*) as views from articles inner "
       "join authors on articles.author = authors.id inner join log "
       "on log.path like concat('%', articles.slug, '%') where "
       "log.status like '%200%' group "
       "by authors.name order by views desc")

query3 = (
       "select  * from ("
       "select date(time),round(100.0*sum(case log.status when '200 OK'"
       "then 0 else 1 end)/count(log.status),2) as per from log "
       "group by date(time)) as error where per > 1")


# connect to database
def connect():
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        return c, db
    except:
        print("Faild to connect")

# get first query


def get_fir_query(query1):
    c, db = connect()
    c.execute(query1)
    posts = c.fetchall()
    for i in range(len(posts)):
        title = posts[i][0]
        views = posts[i][1]
        print("%s--%d" % (title, views))
    db.close()


def get_sec_query(query2):
    # get second query
    c, db = connect()
    c.execute(query2)
    posts = c.fetchall()
    for i in range(len(posts)):
        name = posts[i][0]
        views = posts[i][1]
        print("%s--%d" % (name, views))
    db.close()


def get_thir_query(query3):
    # get third query
    c, db = connect()
    c.execute(query3)
    results = c.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        error_precent = results[i][1]
        print("%s--%.1f %%" % (date, error_precent))


if __name__ == '__main__':
    print("\n"+"What are the most popular three articles of all time?"+"\n")
    get_fir_query(query1)
    print("\n")
    print("Who are the most popular article authors of all time?"+"\n")
    get_sec_query(query2)
    print("\n")
    print("On which days did more than 1% of requests lead to errors?"+"\n")
    get_thir_query(query3)
    print("\n")
