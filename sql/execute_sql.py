import sqlite3


def execute_sql_file(database_path, sql_file_path):
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Read the SQL file
    with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()

    try:
        # Execute the SQL script
        cursor.executescript(sql_script)
        print("SQL script executed successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    database_path = '../data/karate.db'  # Path to your SQLite database
    sql_file_path = 'test.sql'  # Path to your SQL file

    execute_sql_file(database_path, sql_file_path)
