#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
from Bestseller_Search_engine import  BestsellerSearchEngine


TOKEN = '1151126802:AAGvjvmXw-60gUUlp3gR2HNlrOs9Q2xxSnA'
MAX_MSG_LENGTH = 300


def sendMessage(user, msg):
  try:
    bot.sendMessage(user, msg)
  except:
    traceback.print_exc(file=sys.stdout)

def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type != 'text': #텍스트인지 아닌지 구분
    sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
    return
  pprint(msg) #텔레그램 참가자의 메시지 출력

  text = msg['text']
  args = text.split(' ')
  if text.startswith('베스트셀러'):
    print('try to 베스트셀러')
    replyAptData(chat_id)
  elif text.startswith('저장') and len(args) > 1:
    print('try to 저장', args[1])
    save(chat_id, args[1])
  elif text.startswith('확인'):
    print('try to 확인')
    check(chat_id)
  else:
    sendMessage(chat_id, '모르는 명령어입니다.베스트셀러, 저장 [isbn번호], 확인 중 하나의 명령을 입력하세요.')

def replyAptData(user):
  BS_engine=BestsellerSearchEngine

  msg = "******"+current_month+"오늘의 베스트셀러"+"******\n"

  for b in BS_engine.searched_books:
    print(str(datetime.now()).split('.')[0], b)
    msg+="제목: "+b["title"]+"\n"+"isbn: "+b["isbn"]+"\n"+\
      "-----------------------"+"\n"
  if msg:
    sendMessage(user, msg)
  else:
    sendMessage(user, '%해당하는 데이터가 없습니다.' )

def save(user, loc_param):
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
  try:
    cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
  except sqlite3.IntegrityError:
    sendMessage(user, '이미 해당 정보가 저장되어 있습니다.')
    return
  else:
    sendMessage(user, '저장되었습니다.')
    conn.commit()

def check(user):
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
  cursor.execute('SELECT * from users WHERE user="%s"' % user)

  BS_engine = BestsellerSearchEngine

  msg=''
  for data in cursor.fetchall():
    for b in BS_engine.searched_books:
      d=""
      for i in data[1]:
        d+=i.replace("[","").replace("]","") #숫자만 뜨게 변경
      if str(b["isbn"]) == str(d):
        msg += "isbn: " + b["isbn"] +"\n"+"제목: " + b["title"] + "\n" + "저자: "+ b["author"]\
               +"\n" + "출판사: "+ b["publisher"]+"\n"+"-------------------------------"+"\n"

  sendMessage(user, msg)


bot=telepot.Bot(TOKEN)
pprint(bot.getMe()) # 텔레그램 봇의 정보 출력

today = date.today()
current_month = today.strftime('%Y%m')
print( '[',today,']received token :', TOKEN )

bot.message_loop(handle)
print("listening")

while 1:
  time.sleep(10)