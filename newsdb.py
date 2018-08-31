#!/usr/bin/env python3

import psycopg2
from tabulate import tabulate

DBNAME = 'news'


def run(query):
    db = psycopg2.connect(database=DBNAME)
    x = db.cursor()
    x.execute(query)
    db.close
    return x.fetchall()


def popular_articles():
    query = """
    Select articles.title, count(*) as views
    From articles
    join log on articles.slug = REPLACE(log.path, '/article/', '')
    Group by articles.title
    Order by count(*) desc
    limit 3; """
    result = run(query)
    print('\n Top three articles of all time: \n')
    print tabulate((result), headers=['Title', 'Views'], tablefmt='orgtbl')
    return
popular_articles()


def popular_authors():
    query = """
        select authors.name, count(*) as views
        from articles join authors on authors.id = articles.author
        join log on REPLACE(log.path, '/article/', '')= articles.slug
        group by authors.name
        order by count(*) desc;"""
    result = run(query)
    print('\n Most popular article authors of all time: \n')
    print tabulate((result), headers=['Author', 'Views'], tablefmt='orgtbl')
    return
popular_authors()


def requests_error():
    query = """
    select sq1.date,
    round (((sq1.num * 1.0)/(sq2.total) * 100 ),2 )  as percentage
    from (select date(log.time) as date, count(*) as num
    from log where status = '404 NOT FOUND'
    group by date(log.time)
    order by date(log.time)) as sq1
    join (select date(log.time), count(*) as total
    from log group by date(log.time)) as sq2
    on sq1.date = sq2.date
    Where sq1.num > 0.01 * sq2.total;"""
    result = run(query)
    print('\n Days with more than 1% of requests error:\n')
    print(tabulate((result), headers=['Date', 'Error_Percentage'],
          tablefmt='orgtbl')+'\n')
    return
requests_error()
