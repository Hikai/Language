# -*- coding: utf-8 -*-
"""
SQLite3 module example.

To-do:
"""
import sqlite3


def main():
    """Main."""
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from table")
    for x in cursor.fetchall():
        print(x)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
