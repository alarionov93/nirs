# -*- coding: utf-8 -*-

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import psycopg2
from django.core.mail import send_mail
from time import sleep
from random import randint

conn = psycopg2.connect("dbname=ruskonkurs.ru user=ruskonkurs.ru host=localhost password=varko2007")
cur = conn.cursor()

exclude_list = [
	'anna.v.semyonova@gmail.com',
	'dil@cea.ru',
	'portselyana@yandex.ru',
	'i210gd@yandex.ru',
	'tamir.ogli@gmail.com',
	'tsa-22@mail.ru',
]
include_list = ['alarionov93@yandex.ru', 'dan973@ya.ru', 'olga.v.soboleva@gmail.com']

subject = 'Конкурс ПНИПУ «Знатоки русского языка - 7»'
msg = 'Пермский национальный исследовательский политехнический университет приглашает Вас принять участие в новом интернет-конкурсе «Знатоки русского языка»!\n\
Ждем по адресу: http://ruskonkurs.ru/\n\
Участвуйте и побеждайте!\n\
С уважением,\n\
оргкомитет конкурса'
from_email = 'konkurs.pstu@gmail.com'

res = cur.execute("SELECT first_name, last_name, email, username FROM auth_user");
for a, b, c, d in cur.fetchall():
	email = ''
	status = 0
	if '@' in c:
		email = c
	elif '@' in d:
		email = d
	else:
		email = ''
	if len(email) > 0 and email not in exclude_list:
		i = randint(1, 10)
		# include_list.append(email)
		status = send_mail(subject, msg, from_email, [email], fail_silently=False)
		sleep(i)
		print(email, status)

