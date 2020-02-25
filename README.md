# AnonyPy
An open source python script which (_as of now_) can anonymize a MySQL Database.

## Table Of Content
- [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Requirements](#python-library-requirements)
- [Using AnonyPy](#Using-AnonyPy)
- [Configuration](#Setting-up-configuration)


## Getting Started


### Prerequisites
Using the sample database you can create a database in MySQL to test the AnonyPy.
You're going to need mysql installed with an account. [You can follow instuctions on MySql website](https://dev.mysql.com/downloads/installer/)

Import the SQL file into MySQL Workbench using the following:

```
mysql -u Your_Username -pYour_Password < mock_data.sql
```

### Python Library Requirements.
- a
- b
- c

## Using AnonyPy
Before you run AnonyPy you're gonna want to make sure your database is backed up.
Make sure you read through your configuration file before running.


## Setting up configuration 
### database
Access the configuration file [`config/settings.json`] 
**Sample**
```json
  "database": {
    "host": "localhost",
    "user": "anony",
    "password": "pi",
    "database": "sakila",
    "dump_path": "Dump"
  }
```
The sample is based on if you install the mock data. Replace the details with the credentials to access your database.
`dump_path` (_optional_) is where you would dump the database if needed.

### truncate
if you wish to truncate any tables you would add them here. 
the sample below will add two tables to the list and each will be truncated one after the other. 

**sample**
```json
  "truncate": [
    "payment",
    "rental"
  ],
```

### custom queries
**Note:** These queries run before anonymizing.

Here you can run any query you wish. these would run before the anonymizing takes place. In the sample below i wanted to make sure certain users had a certain password.

**sample**
```json
  "custom_queries": [
    "UPDATE staff SET password='fg3545fj367676745532rrgf34gfh67th5' WHERE staff_id=1;"
  ]
```

### final queries
**Note:** These queries run after anonymizing.

Here i can make any last minute changes. in the sample below i trucnate a table and set a user to have a special email address as he would have an anonymized email address beforehand.

```json
    "final_queries": [
    "Truncate rental",
    "UPDATE `sakila`.`staff` SET `email`='admin@anoy.py' WHERE staff_id=1;"
  ],
```

