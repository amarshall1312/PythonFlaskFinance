from flask import Flask, render_template, request, redirect
import sqlite3
import os

FINANCES_DB = "finance.db"

if not os.path.exists(FINANCES_DB):
    connection = sqlite3.connect(FINANCES_DB)
    connection.executescript("""
        CREATE TABLE savingpots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            target INTEGER,
            deadline INTEGER
        );
        CREATE TABLE outgoings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            fixed INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            frequency TEXT NOT NULL,
            date INTEGER,
            category TEXT
        );
        CREATE TABLE owners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        CREATE TABLE baseincomes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            frequency TEXT NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES owners(id)
        );
        CREATE TABLE additionalincomes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            frequency TEXT,
            date date,
            FOREIGN KEY (owner_id) REFERENCES owners(id)
        );
    """)
    connection.commit()
    connection.close()

