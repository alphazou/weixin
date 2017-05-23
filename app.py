# coding=utf8
import itchat
import time
from itchat.content import *
import os

global order
orders = [None]


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    print(msg)

    if msg['Text'] == '关机' and msg['FromUserName'] == '@3701ce1817fa945377c79297aaf4246e':
        itchat.send('回复“是”确认关机！', msg['FromUserName'])
        orders[0] = '关机'
    if (msg['Text'] == '是' and orders[0] == '关机') and msg['FromUserName'] == '@3701ce1817fa945377c79297aaf4246e':
        orders[0] = None
        itchat.send('即将关机！', msg['FromUserName'])
        # os.system('poweroff')


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    fileDir = '%s%s' % (msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received' % msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

#
# @itchat.msg_register('Friends')
# def add_friend(msg):
#     itchat.add_friend(**msg['Text'])
#     itchat.get_contract()
#     itchat.send('Nice to meet you!', msg['RecommendInfo']['UserName'])
#
#
# @itchat.msg_register('Text', isGroupChat=False)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
