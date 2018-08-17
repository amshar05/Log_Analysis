

# Log-Analysis-Udacity-Project
This project is a reporting tool that uses information from an extensive database of a web server and draws conclusions from that information.
(Project from [Full Stack Web Development Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/))

## Introduction
The database contains newspaper articles, authors and web server logs for the website. The database includes below three tables:
* **authors** table which includes information about the article authors.
* **articles** table includes the article title, body, slug and ids of authors.
* **log table** includes one status and method of user access to the website.

#### The project drives following conclusions:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

### Python modules in newsdb.py:
* **psycopg2:** To connect to the database and execute the query.

### Functions in newsdb.py:
* **run(query):** Connects to the PostgreSQL database and executes the query.
