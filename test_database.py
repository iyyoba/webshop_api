
from sqlalchemy import text

from app.database import engine


print("Trying to connect to MariaDB...")

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connected!")
        print("Database result:", result.fetchone())

except Exception as error:
    print("Database connection failed!")
    print("Error:", error)

