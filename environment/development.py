import os

# mysql+mysqlconnector://your-username:your-password@localhost/your-schema'
DATABASE_URI = 'mysql+mysqlconnector://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ.get('DB_USER'),
    dbpass=os.environ.get('DB_PASSWORD'),
    dbhost=os.environ.get('DB_HOST'),
    dbname=os.environ.get('DB_NAME')
)
