# News Scrapper Practice

Run below command to run the program:

```python
# Terminal
activate venv
pip install -r requirements.txt

# create db in PostgreSQL
create database aiohttpdemo_polls;
create user aiohttpdemo_user with password 'aiohttpdemo_pass';
grant all privileges on database aiohttpdemo_polls to aiohttpdemo_user ;

# dump initial data to db
python init_db.py

python aiohttpdemo_polls/main.py

# visit the following url
http://127.0.0.1:8080/
```
