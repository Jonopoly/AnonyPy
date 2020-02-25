# AnonyPy
An open source python script which (_as of now_) can anonymize a MySQL Database.

## Table Of Content
- [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Requirements](#python-library-requirements)
- [Using AnonyPy](#Using-AnonyPy)
- [Setting up configuration](#Setting-up-configuration)
    - [database](#database)
    - [truncate](#truncate)
    - [custom_queries](#custom_queries)
    - [final_queries](#final_queries)
    - [table_data](#table_data)


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

### custom_queries
**Note:** These queries run before anonymizing.

Here you can run any query you wish. these would run before the anonymizing takes place. In the sample below i wanted to make sure certain users had a certain password.

**sample**
```json
   "custom_queries": [
    "UPDATE staff SET password='fg3545fj367676745532rrgf34gfh67th5' WHERE staff_id=1;"
  ]
```

### final_queries
**Note:** These queries run after anonymizing.

Here i can make any last minute changes. in the sample below i trucnate a table and set a user to have a special email address as he would have an anonymized email address beforehand.

```json
    "final_queries": [
    "Truncate rental",
    "UPDATE `sakila`.`staff` SET `email`='admin@anoy.py' WHERE staff_id=1;"
  ],
```

### table_data (data)
the table data in the main part of anonypy process. This will use the data and replace the fields based on what is in the value.

**template**
```json
  "table_data": {
    "name_of_table": {
      "data": {
        "unique_key_in_table": "PrimaryKey",
        "field_one": "fake_map",
        "field_two": "fake_map"
      }
    },
```
|key|value|
|---|---|
|name_of_table|Here you would have the name of the table you wish you anonymize.|
|data|data is a keyword where you can place the fields in.
|unique_key_in_table|This is the primarykey or somethingg that is unique on the table. as it used to update WHERE unique_id = ? |
|field_one, field_two|this would be replaced with the fields you would want to anonymize.|
|fake_map|this would be replaced with a selection from [fakeMap](#)|

in the sample below

**sample**
```json
  "table_data": {
    "actor": {
      "data": {
        "actor_id": "PrimaryKey",
        "first_name": "fake_first_name",
        "last_name": "fake_last_name"
      }
    },
```

### table_data (json)
Similar to the data this will anonymize json.

**Example**
```json
    "comments": {
      "json": {
        "commentsid": "primarykey",
        "comment" : "{\"comment\": {\"liked\": [\"fake_comment\"], \"title\": \"fake_company_name\", \"disliked\": [\"fake_comment\"]}}"
      }
```

Looking at the example  `comments` is the table name and instead of `json` is the keyword, `commentsid` is the primary key
