from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine('postgresql://user:password@host:port/dbname')

# Create a metadata object to hold the database schema
metadata = MetaData()

# Define a table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer))

# Create the table if it doesn't exist
metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a record into the table
new_user = users.insert().values(name='John Doe', age=30)
session.execute(new_user)
session.commit()

# Query the table
result = session.query(users).filter(users.c.age > 25).all()
for row in result:
    print(row.name, row.age)
