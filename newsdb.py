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
