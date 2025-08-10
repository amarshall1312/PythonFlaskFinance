from flask import Flask, render_template, request, redirect
import sqlite3
import os

FINANCES_DB = "finance.db"

if not os.path.exists(FINANCES_DB):
    connection = sqlite3.connect(FINANCES_DB)
    connection.execute("""
        CREATE TABLE savingpots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            target INTEGER,
            deadline INTEGER
        )
    """)
    connection.commit()
    connection.close()

