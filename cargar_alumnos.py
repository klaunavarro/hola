# -*- coding: utf-8 -*-
import sqlite3
import csv

conn = sqlite3.connect("alumnos2.db")

c = conn.cursor()

# # 1 Create table
c.execute('''CREATE TABLE alumnos (rut text primary key, nombres text, apellidos text, correo text)''')

alumnos = []

with open('alumnos.csv', 'rb') as csvfile:
	freader = csv.reader(csvfile, delimiter=';')
	for row in freader:
		alumnos.append([row[3], row[1], row[0], row[2]])

c.executemany('INSERT INTO alumnos VALUES(?,?,?,?)', alumnos)
conn.commit()

