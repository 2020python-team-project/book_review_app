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
  if text.startswith('도서명') and len(args) > 1:
    print('try to 도서명', args[1])
  elif text.startswith('저장') and len(args) > 1:
    print('try to 저장', args[1])
  elif text.startswith('확인'):
    print('try to 확인')
  else:
    sendMessage(chat_id, '모르는 명령어입니다.도서검색 [도서명], 저장 [isbn번호], 확인 중 하나의 명령을 입력하세요.')


bot=telepot.Bot(TOKEN)
pprint(bot.getMe()) # 텔레그램 봇의 정보 출력

today = date.today()
current_month = today.strftime('%Y%m')
print( '[',today,']received token :', TOKEN )

bot.message_loop(handle)
print("listening")

while 1:
  time.sleep(10)