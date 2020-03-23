# AnonyPy
                                   
Anonypy is an open source python project which is designed to anonymize a MySql database.

## Overview
Working as a Junior developer I would test my code against a small database that was created for testing. It would pass all the criteria, failing at the last hurdle when testing against a copy of live data with issues such as; timeout, corrupt old data.
I came up with this program as a solution to this issue, the software would in theory clone your live data and anonymize it so that it can be used on a development environment.

This project is to anonymize databases. This is so you can anonymize your production database which allows for more accuracy in development testing.
AnonyPy would like to anonymize all databases (_SQL, Mongo etc..._) currently it only works with MySQL. AnonyPy anonymize's client data replacing identifiable information with 'fake' data.

![Overview of how this works](https://ras-cf-public.s3-eu-west-1.amazonaws.com/images/Slide1.png)

This project would be useful for you to anonymize a copy of your live data so that you can use it on your development enviroments to test code against a database similary to your production database.


![Alt Text](https://media.giphy.com/media/hpXLca0svDLvq0O5tr/giphy.gif)

## Table Of Content
- [How to contribute](#how-to-contribute)
- [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Requirements](#python-library-requirements)
- [Using AnonyPy](#Using-AnonyPy)
- [Setting up configuration](#Setting-up-configuration)
    - [fakeMap](#anonymizedatamap)
    - [database](#database)
    - [truncate](#truncate)
    - [custom_queries](#custom_queries)
    - [final_queries](#final_queries)
    - [table_data (data)](#table_data-data)
    - [table_data (json)](#table_data-json)
- [Licence](#license)


## How to contribute
see the [CONTRIBUTING.md](https://github.com/Jonopoly/AnonyPy/blob/master/CONTRIBUTING.md)

## Getting Started

### Prerequisites
Using the sample data you can create a database in MySQL to test the AnonyPy.
You're going to need mysql installed with an account. [You can follow instuctions on MySql website](https://dev.mysql.com/downloads/installer/)

Inside `sample data/` you wil find mock_data.sql you can import it using the follow command line script:
```
mysql -u Your_Username -pYour_Password < mock_data.sql
```

### Python Library Requirements.
- art v4.1
- beautifulsoup4 v4.8.1
- colorama v0.4.1
- Faker v2.0.2
- mysql-connector-python v8.0.17
- numpy v1.17.2

```
pip install -r requirements.txt
```
## Using AnonyPy
Before you run AnonyPy ensure your database is backed up. You can find some instructions on backing up your database on the [MySql Website](https://dev.mysql.com/doc/mysql-backup-excerpt/5.7/en/backup-and-recovery.html)

Once you've backed up check your configuration file before running.


## Setting up configuration 
### anonymizeDataMap
|key|defintion|
|---|---|
|fake_name| returns a fake name (_e.g. John Smith_) |
|fake_email| returns a fake email addreess (_e.g. JohnSmith124@anonypy.fake_)|
|fake_phone_number| returns a fake phone number (_e.g. +44(23) 4444 1234_)|
|fake_first_name| returns a first name (_e.g. John_)|
|fake_last_name| returns a surname (_e.g. smith_)|
|fake_location| returns a country (_e.g. France_)|
|fake_job|returns a job (_e.g. Administrator_)|
|fake_company_name|returns a fake company name (_e.g. Pierce Group PLC3018_)|
|fake_random_words|return two random words with an int at the end (_e.g. House_door452_)|
|fake_paragraph|returns a fake random 10-50 word sentence (_e.g. 'Significant then remember of several another president less all one lawyer reveal late when maintain on through artist artist way step paper send team article know._)|
|fake_comment|similar to paragraph but returns 1-75 words|
|fake_password|returns a fake password (_e.g. 9JEgaujaEDQYp4CHa1pMPa0Cm_|
|fake_html_answer| similar to fake html answer it returns 10-50 words wrapped in <p></p> (_e.g. \<p>Else let free anyone tough case help ever should chair stop explain.\</p>_|
|fake_words_replace| returns the same total of words with fake words (_e.g. 'Hello World' could be 'cartoon milk')|
|fake_street| returns a fake street address (_e.g. 72251 Leonard Path_)|
|fake_us_postcode|returns a fake postcode (_e.g. 61210_)|


### database
The configuration file is located at:   [`config/settings.json`] 

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
Here is an example of credentials used to log in to a database. Replace the example credentials with your own to access the database.
`dump_path` (_optional_) is where you would dump the database if needed.

### truncate
If you need to truncate any tables you would add them here. 
The sample below will add two tables to the list and each will be truncated one after the other. 

**sample**
```json
  "truncate": [
    "payment",
    "rental"
  ],
```

### custom_queries
**Note:** These queries run before anonymizing.

Here you can run any query. These will run before the anonymizing takes place. Below is an example of running a query before anonymizing. 

**sample**
```json
   "custom_queries": [
    "UPDATE staff SET password='fg3545fj367676745532rrgf34gfh67th5' WHERE staff_id=1;"
  ]
```

### final_queries
**Note:** These queries run after anonymizing.

Here final changes can be made. The sample below shows two queries will be executed after the data is anonymized. 

```json
    "final_queries": [
    "Truncate rental",
    "UPDATE `sakila`.`staff` SET `email`='admin@anoy.py' WHERE staff_id=1;"
  ],
```

### table_data (data)
The table data is the main part of Anonypy's process, here you can replace data within the fields of the table. 

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
|name_of_table|Here you would have the name of the table will anonymize.|
|data|Data is an identifier where you can place your keys and values. 
|unique_key_in_table|This is the primarykey or something that is unique in the table. It is used to update WHERE unique_id = ? |
|field_one, field_two|This would be replaced with the fields you want to anonymize.|
|fake_map|This would be replaced with a selection from [fakeMap](#anonymizedatamap)|

The sample below shows that the table "actor" has been selected and two fields are replaced with "fake_first_name" and "fake_last_name"

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
Similar to the "table_data (data) " this will anonymize json.
Below is a sample JSON from `comment` in the `comments` table. The example further down has the `comments` table selected `json` is the identifier AnonyPy will look for.
The selected of json I want to anonymize are `liked`, `title` and `disliked` these are replaced with `fake_comment` and `fake_sentence` (_[Click here for more fake labels](#anonymizedatamap)_)

**Sample JSON**
```json
  "comment" : {
    "liked": [
               "Great Movie!, Soundtrack was great!"
    ],
    "title": "The movie for me", 
    "disliked": [
                  "Original was better!"
    ]
         
  }
```

**Example**
```json
    "comments": {
      "json": {
        "commentsid": "primarykey",
        "comment" : "{\"comment\": {\"liked\": [\"fake_comment\"], \"title\": \"fake_sentence\", \"disliked\": [\"fake_comment\"]}}"
      }
```


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Jonopoly/AnonyPy/blob/master/LICENSE) file for details
