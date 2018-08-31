

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
* **tabulate:** To print the output in a clean tabular format.


### Functions in newsdb.py:
* **run(query):** Connects to the PostgreSQL database and executes the query.
* **popular_articles():** Prints most popular three articles of all time.
* **popular_authors():** Prints most popular article authors of all time.
* **requests_error():** Print days on which more than 1% of requests lead to errors.
* **view_author_article_log():** Creates view popular_articles that drives first & second conclusion.

### Views Made:
* <h4>author_article_log</h4>
```sql
create view author_article_log as
select articles.title, authors.name,log.status, date(log.time)
from articles
join authors on articles.author = authors.id
join log on articles.slug = REPLACE(log.path, '/article/', '');
```

## Instructions
* <h4>Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></h4>
* <h4>Start the virtual machine</h4>
  From the terminal, inside of the project directory, run command `vagrant up`. This will cause download the Vagrant Linux operating system and install it.
  Then run `vagrant ssh` to log in to Linux VM!
* <h4>Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a></h4>
  After downloading unzip the file. Move newsdata.sql (the file inside the zip file) in the vagrant           directory.
* <h4>Setup Database</h4>
  To connect and load the database use:
  <code> psql -d news -f newsdata.sql; </code>
* <h4>Make Views</h4>
  Make views by running view query in the shell or by uncommenting code in python.
* <h4>Run Module</h4>
  <code>python newsdb.py</code>

### Output:
```sql
PRINTING RESULTS BELOW:

Top three articles of all time:

| Title                            |   Views |
|----------------------------------+---------|
| Candidate is jerk, alleges rival |  338647 |
| Bears love berries, alleges bear |  253801 |
| Bad things gone, say good people |  170098 |

Most popular article authors of all time:

| Author                 |   Views |
|------------------------+---------|
| Ursula La Multa        |  507594 |
| Rudolf von Treppenwitz |  423457 |
| Anonymous Contributor  |  170098 |
| Markoff Chaney         |   84557 |

Days with more than 1% of requests error:

| Date       |   Error_Percentage |
|------------+--------------------|
| 2016-07-17 |               2.26 |


TASK COMPLETED!
GOODBYE!
```
