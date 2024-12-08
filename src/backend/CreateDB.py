import pymysql

# Database connection details
db_config = {
    "host": "localhost",       # Change to your database host
    "user": "root",            # Change to your database user
    "password": "kenneth", # Change to your database password
    "charset": "utf8mb4",
}

database_name = "Petbook"

# SQL commands to create the database and tables
create_database_sql = f"CREATE DATABASE IF NOT EXISTS {database_name};"
use_database_sql = f"USE {database_name};"

create_tables_sql = [
    """
    CREATE TABLE IF NOT EXISTS Users (
        UserID INT PRIMARY KEY AUTO_INCREMENT,
        Username VARCHAR(50) UNIQUE NOT NULL,
        Email VARCHAR(100) UNIQUE NOT NULL,
        Password VARCHAR(255) NOT NULL,
        Name VARCHAR(100),
        Bio TEXT,
        ProfilePicture VARCHAR(255)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Pets (
        PetID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(100) NOT NULL,
        Species VARCHAR(50),
        BirthDate DATE,
        Notes TEXT,
        OwnerID INT NOT NULL,
        FOREIGN KEY (OwnerID) REFERENCES Users(UserID)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Posts (
        PostID INT PRIMARY KEY AUTO_INCREMENT,
        UserID INT NOT NULL,
        Content TEXT NOT NULL,
        MediaType VARCHAR(20),
        MediaURL VARCHAR(255),
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Comments (
        CommentID INT PRIMARY KEY AUTO_INCREMENT,
        PostID INT NOT NULL,
        UserID INT NOT NULL,
        Content TEXT NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (PostID) REFERENCES Posts(PostID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Likes (
        LikeID INT PRIMARY KEY AUTO_INCREMENT,
        PostID INT NOT NULL,
        UserID INT NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (PostID) REFERENCES Posts(PostID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Notifications (
        NotificationID INT PRIMARY KEY AUTO_INCREMENT,
        UserID INT NOT NULL,
        Content TEXT NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        IsRead BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    """
]

# Connect to the MySQL server and execute commands
try:
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # Create the database
    cursor.execute(create_database_sql)
    print(f"Database '{database_name}' created or already exists.")

    # Use the database
    cursor.execute(use_database_sql)

    # Create the tables
    for sql in create_tables_sql:
        cursor.execute(sql)
        print("Table created or already exists.")

    print("All tables successfully created.")
except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
    if connection:
        connection.close()