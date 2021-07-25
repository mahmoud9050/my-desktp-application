from peewee import *
import datetime


db = MySQLDatabase('test', user='root', password='Mahmoud90##',
                         host='127.0.0.1', port=3306)


class Publisher(Model):
    name=CharField(unique=True)
    location=CharField(null=True)

    class Meta:
        database=db

class Author (Model):
    name=CharField(unique=True)
    mail=CharField(null=True)

    class Meta:
        database=db
class Category (Model):
    Category_name = CharField(unique=True)
    parent_Category= IntegerField(null=True)
    class Meta:
        database=db

class Branch (Model):
    Name=CharField()
    Code=CharField(null=True,unique=True)
    Location=CharField(null=True)
    class Meta:
        database=db


        
Books_Status =(
     (1,'new'),
     (2,'used'),
     (3,'Damaged'),

    )


class Books(Model):
    title = CharField(unique=True)
    description = TextField(null=True)
    category =ForeignKeyField(Category ,backref='Category',null=True)
    code=CharField(null=True)
    barcode=CharField()
    #part
    part_order=IntegerField(null=True )
    price=DecimalField(null=True)
    publisher=ForeignKeyField(Publisher, backref='Puplisher',null=True)
    author=ForeignKeyField(Author,backref='author',null=True)
    image=CharField(null=True)
    status=CharField(choices=Books_Status)
    date=DateTimeField(default=datetime.datetime.now)


    class Meta:
        database=db



class Clients(Model):
    Name=CharField()
    Male=CharField(null=True,unique=True)
    Phone=CharField(null=True)
    date=DateTimeField(default=datetime.datetime.now)
    national_id=IntegerField(null=True,unique=True)
    class Meta:
        database=db

class Employee(Model):
    Name = CharField()
    Mail = CharField(null=True,unique=True)
    Phone = CharField(null=True)
    date = DateTimeField(default=datetime.datetime.now)
    national_id = IntegerField(null=True,unique=True)
    periority = CharField(null=True)

    class Meta:
        database=db


Type_process=(
    (1,'Rent'),
    (2,'Retrieve'),
   
        )


class Daily_Movement(Model):
    Book=ForeignKeyField(Books,backref='daily_Book')
    Client=ForeignKeyField(Clients,backref='book_clients')
    type=CharField(choices=Type_process)             #[rent-retrieve]
    date=DateTimeField(default=datetime.datetime.now)
    Branch=ForeignKeyField(Branch,backref='Daily_branch',null=True)
    Book_from=DateField(null=True)
    Book_to=DateField(null=True)
    employee=ForeignKeyField(Employee,backref='daily_employee',null=True)

    class Meta:
        database=db 
Action_type=(
    (1,'Login'),
    (2,'Update'),
    (3,'Create'),
    (4,'Delete'),

    )


Table_choices=(
         (1,'Books'),
         (2,'Clients'),
         (3,'Employee'),
         (4,'Category'),
         (5,'Branch'),
         (6,'Daily Movement'),
         (7,'publisher'),
         (8,'Author'),


    )


class History (Model):
    employee=ForeignKeyField(Employee,backref='History_Employee')
    action =CharField(choices=Action_type)
    table=CharField(choices=Table_choices)
    date=DateTimeField(default=datetime.datetime.now)
    branch=ForeignKeyField(Branch,backref='History_Branch')
    class Meta:
        database=db




    
db.connect()
db.create_tables([Category,Branch,Publisher,Author,Books,Clients,Employee,Daily_Movement,History])
