# LearnMongoDB
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FUnpredictablePrashant%2FLearnMongoDB&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


## Starting off

Let's start the mongo server. Open a terminal and type:

```
mongod
```

This will start the server, now open another terminal and type:
```
mongo
```

Now you are inside the mongo instance, you can now create and play with different operations. Let's see which database we are currently in and what are the databases and collections available.

```
db 
show databases
show collections
```

Commands to create new database is `use`.


## HandsOn Demo

Let's create a database called as `learnmongo` and then we will create a collection called as `class`. Inside this `class` we will add student's name and their age, sample student can be:<br>
Name: Prashant<br>
Age: 25<br>

```
use learnmongo
db.createCollection('class')
db.class.insert({name: "Prashant", age: 52})
```

Let's see what data, I have added:
```
db.class.find().pretty()
```
Okay, I don't want to see `_id`

```
db.class.find({}, _id: 0).pretty()
```



Oops! I made a mistake. My age isn't 52, it's 25. Let me change it back.
```
db.class.update({name : Prashant}, {$set: {age: 25}})
```

## Filters

Displaying everyone whose age is less than 25 years:
```
db.class.find({$and:[{age : {$lt : 25}}]});
```
To display everyone whose age is less than 25 years and name is `Prashant`:
```
db.class.find({$and:[{age : {$lt : 25}}, {name: "Prashant"}]});
```

Note: `$lt` stands for `less than` and `$gt` stands for `greater than`.<br><br>



## CRUD in MongoDB



## Bonus Tips

Just in case you are interested in doing an export and import, you can use `mongodump` and `mongorestore` command. <br>

Note: In recent version of the mongo, mongodump and mongorestore are not part of official package, you have to download it seperately. You can follow this [link](https://www.mongodb.com/try/download/database-tools).