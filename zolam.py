# -*- coding: utf-8 -*-
#Alphrazolam_Bot
import ALPHRAZOLAM
from ALPHRAZOLAM.lib.curve.ttypes import *	
from datetime import datetime	
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile,glob
import requests
import urllib
import urllib2
import subprocess
import profile
import wikipedia
import requests
import os
from gtts import gTTS
from bs4 import BeautifulSoup
from threading import Thread

avril = ALPHRAZOLAM.LINE()
#avril.login(qr=True)
avril.login(token='ErmydO3qD4CUXi1X38Cd.LIcAldG+wLrErDwSHfhYhq.Aw8qg6RE0hR44KgiChT94WGT/CrTGkM2EDEZYgy3wGs=')
avril.loginResult()
print "Avrilia-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


helpMessage ="""
ᴀ    ʟ    ᴘ   ʜ    ʀ   ᴀ   ᴢ   ᴏ   ʟ   ᴀ   ᴍ
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏[𖤓]˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇
█░࿇˶̏˶̏ᙩĿᎯƇҠ_ᎯᮜƓᣯĿS˵̋˵̋࿇
█░࿇˶̏˶̏˶̏[༺𖤓𖡹𖤓༻]˵̋˵̋˵̋࿇
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
     ║✶║ ᴀʟᴘʀʜᴀ ᴢᴏʟᴀᴍ ║✶║
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
█░║✶║〘sᴇʟғ〙
█░║✶║〘ʜɪ〙
█░║✶║〘ᴍᴇ〙
█░║✶║〘ʏᴏᴜ〙
█░║✶║〘ʟᴏᴠᴇ〙
█░║✶║〘ᴍʏʟᴏᴠᴇ〙
█░║✶║〘ᴍʏᴍɪᴅ〙
█░║✶║〘ᴍɪᴅ @〙
█░║✶║〘sᴇᴀʀᴄʜɪᴅ (ɪᴅ ʟɪɴᴇ)〙
█░║✶║〘ᴄʜᴇᴄᴋᴅᴀᴛᴇ:ᴅᴅ/ᴍᴍ/ʏʏ〙
█░║✶║〘ᴋᴀʟᴇɴᴅᴇʀ〙
█░║✶║〘sᴛᴇᴀʟ ᴄᴏɴᴛᴀᴄᴛ〙
█░║✶║〘ᴘᴘ @〙
█░║✶║〘ᴄᴏᴠᴇʀ @〙
█░║✶║〘ᴀᴜᴛᴏ ʟɪᴋᴇ〙
█░║✶║〘sᴄʙᴄ ᴛᴇxᴛ〙
█░║✶║〘ᴄʙᴄ ᴛᴇxᴛ〙
█░║✶║〘ɢʙᴄ ᴛᴇxᴛ〙
█░║✶║〘ʙɪᴏ @〙
█░║✶║〘ɪɴғᴏ @〙
█░║✶║〘ɴᴀᴍᴇ @〙
█░║✶║〘ᴘʀᴏғɪʟᴇ @〙
█░║✶║〘ᴄᴏɴᴛᴀᴄᴛ @〙
█░║✶║〘ɢᴇᴛᴠɪᴅ @〙
█░║✶║〘ғʀɪᴇɴᴅʟɪsᴛ〙
█░║✶║〘ᴍɪᴄᴀᴅᴅ @〙
█░║✶║〘ᴍɪᴄᴅᴇʟ @〙
█░║✶║〘ᴍɪᴄʟɪsᴛ〙
█░║✶║〘ᴀʙsᴇɴ〙
█░║✶║〘sᴘ,sᴘᴇᴇᴅ〙
█░║✶║〘ʀᴇsᴘᴏɴ〙
█░║✶║〘ʀᴜɴᴛɪᴍᴇ〙
█░║✶║〘ᴄᴏᴘʏ @〙
█░║✶║〘ᴄᴏᴘʏᴄᴏɴᴛᴀᴄᴛ〙
█░║✶║〘ᴍʏʙᴀᴄᴋᴜᴘ〙
█░║✶║〘ᴍʏʙɪᴏ (ᴛᴇxᴛ)〙
█░║✶║〘ᴍʏɴᴀᴍᴇ (ᴛᴇxᴛ)〙
█░║✶║〘@ʙʏᴇ〙
█░║✶║〘ʙᴏᴛ ᴏɴ/ᴏғғ〙
█░║✶║〘ɢɪғᴛ〙
█░║✶║〘ɢɪғᴛʙʏᴄᴏɴᴛᴀᴄᴛ〙
█░║✶║〘ɢɪғ ɢᴏʀᴇ〙
█░║✶║〘ɢᴏᴏɢʟᴇ (ᴛᴇxᴛ)〙
█░║✶║〘ᴘʟᴀʏsᴛᴏʀᴇ ɴᴀᴍᴀᴀᴘᴘ〙
█░║✶║〘ғᴀɴᴄʏᴛᴇxᴛ ᴛᴇxᴛ〙
█░║✶║〘ᴍᴜsɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
█░║✶║〘ʟɪʀɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
█░║✶║〘ᴍᴜsʀɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
█░║✶║〘ɪɢ ᴜʀsɴᴀᴍᴇɪɴsᴛᴀɢʀᴀᴍ〙
█░║✶║〘ᴄʜᴇᴄᴋɪɢ ɴᴀᴍᴇɪɴsᴛᴀɢʀᴀᴍ〙
█░║✶║〘ᴀᴘᴀᴋᴀʜ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
█░║✶║〘ᴋᴀᴘᴀɴ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
█░║✶║〘ʜᴀʀɪ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
█░║✶║〘ʙᴇʀᴀᴘᴀ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
█░║✶║〘ʙᴇʀᴀᴘᴀᴋᴀʜ ᴛᴇxᴛ〙
█░║✶║〘ʏᴏᴜᴛᴜʙᴇ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ〙
█░║✶║〘ʏᴏᴜᴛᴜʙᴇᴠɪᴅᴇᴏ :ᴠɪᴅᴇᴏ〙
█░║✶║〘ʏᴏᴜᴛᴜʙᴇsᴇᴀʀᴄʜ:ᴠɪᴅᴇᴏ〙
█░║✶║〘ɪᴍᴀɢᴇ ɴᴀᴍᴀɢᴀᴍʙᴀʀ〙
█░║✶║〘sᴀʏ ᴛᴇxᴛ〙
█░║✶║〘sᴀʏ-ᴇɴ ᴛᴇxᴛ〙
█░║✶║〘sᴀʏ-ᴊᴘ ᴛᴇxᴛ〙
█░║✶║〘ᴛʀ-ɪᴅ ᴛᴇxᴛ( ᴇɴ ᴋᴇ ɪᴅ〙
█░║✶║〘ᴛʀ-ᴇɴ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴇɴ〙
█░║✶║〘ᴛʀ-ᴛʜ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴛʜ〙
█░║✶║〘ɪᴅ@ᴇɴ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴇɴ〙
█░║✶║〘ɪᴅ@ᴛʜ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴛʜ〙
█░║✶║〘ᴇɴ@ɪᴅ ᴛᴇxᴛ( ᴇɴ ᴋᴇ ɪᴅ〙
█░║✶║〘ᴡᴇʟᴄᴏᴍᴇ〙
█░║✶║〘sᴀʏ ᴡᴇʟᴄᴏᴍᴇ〙
█░║✶║〘ɪɴᴠɪᴛᴇ ᴄʀᴇᴀᴛᴏʀ〙
█░║✶║〘sᴇᴛᴠɪᴇᴡ/ᴄᴄᴛᴠ〙
█░║✶║〘ᴠɪᴇᴡsᴇᴇɴ/ᴄɪᴅᴜᴋ〙
█░║✶║〘ɢɴ: (ɴᴀᴍᴀɢʀᴏᴜᴘ)〙
█░║✶║〘ᴛᴀɢ ᴀʟʟ〙
█░║✶║〘ʟᴜʀᴋ ᴏɴ/ᴏғғ〙
█░║✶║〘ʟᴜʀᴋᴇʀs〙
█░║✶║〘ʀᴇᴄᴏᴠᴇʀ〙
█░║✶║〘ᴄᴀɴᴄᴇʟ〙
█░║✶║〘ᴄᴀɴᴄᴇʟᴀʟʟ〙
█░║✶║〘ɢᴄʀᴇᴀᴛᴏʀ〙
█░║✶║〘ɢɪɴғᴏ〙
█░║✶║〘ɢᴜʀʟ〙
█░║✶║〘ʟɪsᴛ ɢʀᴏᴜᴘ〙
█░║✶║〘ᴘɪᴄᴛ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
█░║✶║〘sᴘᴀᴍ: (ᴛᴇxᴛ)〙
█░║✶║〘ᴀᴅᴅ ᴀʟʟ〙
█░║✶║〘ᴋɪᴄᴋ: (ᴍɪᴅ)〙
█░║✶║〘ɪɴᴠɪᴛᴇ: (ᴍɪᴅ)〙
█░║✶║〘ɪɴᴠɪᴛᴇ〙
█░║✶║〘ᴍᴇᴍʟɪsᴛ〙
█░║✶║〘ɢᴇᴛɢʀᴏᴜᴘ ɪᴍᴀɢᴇ〙
█░║✶║〘ᴜʀʟɢʀᴏᴜᴘ ɪᴍᴀɢᴇ〙
█░║✶║〘sᴀᴍʙᴜᴛᴀɴ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴍɪᴍɪᴄ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴜʀʟ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴀʟᴡᴀʏsʀᴇᴀᴅ ᴏɴ/ᴏғғ〙
█░║✶║〘sɪᴅᴇʀ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴄᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ〙
█░║✶║〘sᴛɪᴄᴋᴇʀ ᴏɴ〙
█░║✶║〘sɪᴍɪsɪᴍɪ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴄᴏᴅᴇ #13〙
█░║✶║〘ᴋɪᴄᴋᴀʟʟ〙
█░║✶║〘ʙᴀʀ〙
█░║✶║〘ʙᴄ: (ᴛᴇxᴛ)〙
█░║✶║〘ᴊᴏɪɴ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
█░║✶║〘ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
█░║✶║〘ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ〙
█░║✶║〘ᴛᴀɢ ᴏɴ/ᴏғғ〙
█░║✶║〘ʙᴏᴛ ʀᴇsᴛᴀʀᴛ〙
█░║✶║〘ᴛᴜʀɴ ᴏғғ〙
█░║✶║〘ʙᴀɴ〙
█░║✶║〘ᴜɴʙᴀɴ〙
█░║✶║〘ʙᴀɴ @〙
█░║✶║〘ᴜɴʙᴀɴ @〙
█░║✶║〘ʙᴀɴ ʟɪsᴛ〙
█░║✶║〘ᴄʟᴇᴀʀ ʙᴀɴ〙
█░║✶║〘ᴋɪʟʟ〙
█░║✶║〘ᴋɪᴄᴋ @〙
█░║✶║〘sᴇᴛ ᴍᴇᴍʙᴇʀ: (ᴊᴜᴍʙʟᴀʜ)〙
█░║✶║〘ʙᴀɴ ɢʀᴏᴜᴘ: (ɴᴀᴍᴀɢʀᴏᴜᴘ〙
█░║✶║〘ᴅᴇʟ ʙᴀɴ: (ɴᴀᴍᴀɢʀᴏᴜᴘ〙
█░║✶║〘ʟɪsᴛ ʙᴀɴ〙
█░║✶║〘ᴋɪʟʟ ʙᴀɴ〙
█░║✶║〘ɢʟɪsᴛ〙
█░║✶║〘sᴘ @:sᴘᴀᴍ ᴄᴏɴᴛᴀᴄᴛ〙
█░║✶║〘ᴛᴏ @ᴛᴀʀɢᴇᴛ〙
█░║✶║〘ᴋᴇʟɪɴᴄɪ @ᴛᴀʀɢᴇᴛ〙
█░║✶║〘ɢʟɪsᴛᴍɪᴅ〙
█░║✶║〘ᴅᴇᴛᴀɪʟs ɢʀᴏᴜᴘ: (ɢɪᴅ)〙
█░║✶║〘ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ: (ɢɪᴅ)〙
█░║✶║〘ɪɴᴠɪᴛᴇᴍᴇᴛᴏ: (ɢɪᴅ)〙
█░║✶║〘ᴀᴄᴄ ɪɴᴠɪᴛᴇ〙
█░║✶║〘ʀᴇᴍᴏᴠᴇᴄʜᴀᴛ〙
█░║✶║〘ϙʀ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴀᴜᴛᴏᴋɪᴄᴋ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴀᴜᴛᴏᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ〙
█░║✶║〘ɪɴᴠɪᴛᴇᴘʀᴏ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴊᴏɪɴ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴊᴏɪɴᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ〙
█░║✶║〘ʀᴇsᴘᴏɴ1 ᴏɴ/ᴏғғ〙
█░║✶║〘ʀᴇsᴘᴏɴ2 ᴏɴ/ᴏғғ〙
█░║✶║〘ʀᴇsᴘᴏɴ3 ᴏɴ/ᴏғғ〙
█░║✶║〘ʀᴇsᴘᴏɴᴋɪᴄᴋ ᴏɴ/ᴏғғ〙
█░║✶║〘ᴛᴀɢᴠɪʀᴜs ᴏɴ/ᴏғғ〙
█░║✶║〘ᴀʟʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ〙
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏ [𖤓] ˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇
█░࿇A̸͟͞V̸͟͞R̸͟͞I̸͟͞L̸͟͞I̸͟͞A̸͟͞ [𖡹] L̸͟͞E̸͟͞V̸͟͞A̸͟͞N̸͟͞A࿇
█░࿇˶̏˶̏˶̏[༺𖤓𖡹𖤓༻]˵̋˵̋˵̋࿇
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄█
"""

zolam="ubd7b4dd119abd73ab3df542fb58a8a65"

KAC=[avril]
mid = avril.getProfile().mid
Bots=[mid]
Creator=["ubd7b4dd119abd73ab3df542fb58a8a65","u96209a2c383f5a545e45d5ac8451f21d"]
admin=["ubd7b4dd119abd73ab3df542fb58a8a65","u96209a2c383f5a545e45d5ac8451f21d"]

contact = avril.getProfile()
backup1 = avril.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = avril.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":True,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    "Add":True,
    'pap':{},
    'invite':{},
    'spammed':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':True,
    'Tagvirus':False,
    'detectMention2':False,
    'detectMention3':True,
    'kickMention':False,  
    'sticker':False,
    'Crash':False,
    'timeline':True,
    "Timeline":True,
    "autoAdd":True,
    "comment":"【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n  http://line.me/ti/p/AqTXMqygnD\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄",    
    "commentOn":True,
    "commentBlack":{},
    "message":"╔═──────┅═ই۝ई═┅──────\n_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n  http://line.me/ti/p/AqTXMqygnD\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█\n╚═────────┅═ই۝ई═┅─────────",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"success"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=True)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image success')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Success')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithUrl(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithURL(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Success')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Success')
  
def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "⛧ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "⛥ᴍᴇɴᴛɪᴏɴ⛦\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      avril.sendMessage(msg)
    except Exception as error:
      print error          
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       avril.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65','"}
              if (wait["message"] in [""," ","\n",None]):
                  pass
              else:
                  avril.sendText(op.param1,str(wait["message"]))
                  avril.sendMessage(c)


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = avril.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n☠ "   + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        avril.sendText(op.param1, "Ehh Ada " + "❂•••{ "  + Name +  " }•••❂")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        avril.sendText(op.param1, "Hay " + "❂•••{ "  + Name +  " }•••❂")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    avril.sendText(op.param1, "Hallo " + "❂•••{ "  + Name +  " }•••❂" )
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            avril.leaveRoom(op.param1)

        if op.type == 21:
            avril.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    avril.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = avril.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        avril.acceptGroupInvitation(op.param1)
                        avril.sendText(op.param1,"Maaf " + avril.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        avril.leaveGroup(op.param1)                        
		    else:
                        avril.acceptGroupInvitation(op.param1)
			avril.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = avril.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        avril.rejectGroupInvitation(op.param1)
		    else:
                        avril.acceptGroupInvitation(op.param1)
			avril.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        avril.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			avril.cancelGroupInvitation(op.param1, [op.param3])
			avril.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    avril.cancelGroupInvitation(op.param1,[op.param3])
                    avril.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               avril.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    avril.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        avril.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        avril.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        avril.kickoutFromGroup(op.param1,[op.param2])
			avril.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    avril.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        avril.kickoutFromGroup(op.param1,[op.param2])
			avril.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                avril.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        avril.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    avril.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    avril.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = avril.getGroup(op.param1)
            contact = avril.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            avril.sendText(op.param1,"🄷🄰🄻🄻🄾... " + avril.getContact(op.param2).displayName + "\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█░░╔╦╗ ╔╗░░█\n█░░─║─ ║║░░█\n█░░─╩ ─╚╝░░█\n\n⛦•••{ " + str(ginfo.name) + " }•••⛦" + "\n\nBudayakan Cek Note\nDan Semoga Betah Disini..\nJangan Lupa Nikung Kak,..Yehkan..\n\nDah Gitu Ajah..\n\n\n===❍•••{☠ʟᴇᴠᴀɴᴀ☠}•••❍===\n"+ datetime.now().strftime('%H:%M:%S'))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            avril.sendMessage(c)  
            avril.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            avril.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            avril.sendText(op.param1,"Nahhhh Lohhhhh " + avril.getContact(op.param2).displayName +  "\nBaper Tuh Orang . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            avril.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
 
        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in admin:
           if op.param2 in Bots:
               pass
          else:
            try:
              G = avril.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = avril.reissueGroupTicket(op.param1)
              avril.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              avril.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              avril.sendMessage(c)
              avril.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              avril.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = avril.getGroup(op.param1)
              G.preventJoinByTicket = False
              avril.updateGroup(G)
              Ticket = avril.reissueGroupTicket(op.param1)
              avril.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              avril.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              avril.sendMessage(c)
              avril.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              avril.updateGroup(G)
              wait["blacklist"][op.param2] = True


         
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        avril.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                avril.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = avril.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  avril.sendText(msg.to,ret_)
                                  avril.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait['Tagvirus'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65'"}
                                  avril.sendMessage(msg)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = avril.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  avril.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  avril.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:
                    contact = avril.getContact(msg.from_)
                    cName = contact.displayName
                    #balas = ""
                    balas1 = "@" +cName
                    #ret_ = random.choice(balas)
                    image ="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  #avril.sendText(msg.to,ret_)
                                  avril.sendText(msg.to,balas1)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': msg.from_}
                                  avril.sendMessage(msg)
                                  h = avril.getContact(msg.from_)
                                  avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)                       
                                  h = avril.getContact(msg.from_)
                                  cu = avril.channel.getCover(msg.from_)
                                  path = str(cu)
                                  avril.sendImageWithURL(msg.to, path)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKPKGID": "10682",
                                                       "STKTXT": "[]",
                                                       "STKVER": "1",
                                                       "STKID": "31916166"}
                                  avril.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                avril.sendText(msg.to,"Bot Sudah On Boss Quh.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                avril.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    avril.sendChatChecked(msg.from_,msg.id)
                else:
                    avril.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     avril.like(url[25:58], url[66:], likeType=1005)
                     avril.comment(url[25:58], url[66:], wait["comment"])
                     avril.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False

            if "Show " in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = avril.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            avril.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            avril.sendText(msg.to,"Ditambahkan")
		    else:
			avril.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        avril.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        avril.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     avril.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = avril.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = avril.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         avril.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = avril.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = avril.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         avril.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = avril.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        avril.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        avril.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Can not be used outside the group")
                    else:
                        avril.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                avril.sendText(msg.to,"❂••••••=═ই✪͜͡✪۝✪͜͡✪ई═=•••••❂")
                avril.sendText(msg.to,"❂••••••••••✧✧✧••••••••••❂")
                avril.sendMessage(msg)
                h = avril.getContact(mid)
                #avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                avril.sendMessage(msg)
		avril.sendText(msg.to,"❂•••••{ C_R_E_A_T_O_R }•••••❂")
		avril.sendText(msg.to,"❂••••••=═ই✪͜͡✪۝✪͜͡✪ई═=•••••❂")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = avril.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                avril.sendMessage(msg)
		avril.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    avril.sendText(msg.to,msg.text)


            elif cms(msg.text,["Add"]):
                    avril.sendText(msg.to,"❂••••••[_Ꭺ҉ Ꭰ҉ Ꭰ҉ _]••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u17a086ccff618e754588a1108335867f"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2552e86aab1b1426749dd0439b0f8c7f"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc67a847198ce188b412a058d86f10367"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u190afbb99dd1c28cc57642627f2aa1a2"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u12322ff2ca2b48474389f3d91b9ff385"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2beb70887d61c0e3abf3ac327b7b21d9"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub08e59948aaf244041d99091254e743c"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2c83fe9f836a2f74f7f9316e0c184f9d"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u02c62ba90a4f9ff95950d1a5ee9f2154"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u47b8e60143e0e1c6fdebe67e6a355ad2"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u70489ca3e0d013e866a556665ee9d99b"}
                    avril.sendMessage(msg)
                    avril.sendText(msg.to,"❂••••••• [_TQ_] ••••••❂ ")
                    avril.sendText(msg.to,"ADD AJA BOSS...")

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = avril.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                avril.findAndAddContactsByMid(target)
                                contact = avril.getContact(target)
                                cu = avril.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                avril.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                avril.sendText(msg.to,"Profile Picture " + contact.displayName)
                                avril.sendImageWithURL(msg.to,image)
                                avril.sendText(msg.to,"Cover " + contact.displayName)
                                avril.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = avril.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                avril.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                avril.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = avril.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        avril.sendText(msg.to, "Ok...")
                        pass
                    else:
                        for target in targets:
                            try:
                                avril.CloneContactProfile(target)
                                avril.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = avril.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             avril.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 avril.findAndAddContactsByMid(target)
                                 avril.inviteIntoGroup(msg.to,[target])
                                 avril.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      avril.sendText(msg.to,"Success Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                avril.sendText(msg.to,creatorMessage)

            elif msg.text in ["Aku","Bot","Comand"]:
                avril.sendText(msg.to,akuMessage)

            elif msg.text in ["Key","List","Help"]:
                avril.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Self"]:
                avril.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                avril.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                avril.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                avril.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                avril.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = avril.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = avril.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    avril.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = avril.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = avril.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    avril.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    avril.sendText(msg.to, "Khusus avril")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        avril.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +avril.getGroup(gid).name + "\n"
                        avril.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    avril.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if avril.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    avril.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    avril.sendText(msg.to, "Khusus avril")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = avril.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = avril.getGroup(i).name
		            if h == ng:
		                avril.inviteIntoGroup(i,[Creator])
			        avril.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        avril.sendText(msg.to,"Khusus avril")
		except Exception as e:
		    avril.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = avril.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = avril.getGroup(i).name
		        if h == ng:
			    avril.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            avril.leaveGroup(i)
			    avril.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    avril.sendText(msg.to,"Khusus avril")
 
	    elif "Leave all group" == msg.text:
		gid = avril.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			avril.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        avril.leaveGroup(i)
		    avril.sendText(msg.to,"Success Leave All Group")
		else:
		    avril.sendText(msg.to,"Khusus avril")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = avril.getGroupIdsJoined()
                for i in gid:
                    h = avril.getGroup(i).name
                    gna = avril.getGroup(i)
                    if h == saya:
                        avril.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = avril.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        avril.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        avril.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    avril.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = avril.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    avril.updateGroup(X)
                    avril.sendText(msg.to,"Url Sudah Aktif")
                else:
                    avril.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = avril.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    avril.updateGroup(X)
                    avril.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    avril.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    avril.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    avril.sendText(msg.to,"Khusus avril")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    avril.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    avril.sendText(msg.to,"Khusus avril")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    avril.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    avril.sendText(msg.to,"Khusus avril")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    avril.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    avril.sendText(msg.to,"Khusus avril")		    
		    
 
            elif msg.text in ["Virus on"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = True
                    wait["Ghost"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    avril.sendText(msg.to,"Virus Tag Sudah Aktif Mohon Berhati-hatilah")
		else:
		    avril.sendText(msg.to,"Khusus Avril Boss")

            elif msg.text in ["Virus off"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = False
                    avril.sendText(msg.to,"Virus Tag Sudah Off")
		else:
		    avril.sendText(msg.to,"Khusus Avril Bos")	
		    
		    
            elif msg.text in ["Ghost on"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = False
                    wait["Ghost"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    avril.sendText(msg.to,"Ghost Sudah Di Aktifkan")
		else:
		    avril.sendText(msg.to,"Khusus Avril Bos")
            elif msg.text in ["Ghost off"]:
		if msg.from_ in admin:
                    wait["Ghost"] = False
                    avril.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
		else:
		    avril.sendText(msg.to,"Khusus Avril Bos")	
		    

            elif msg.text in ["Tag on"]:
		if msg.from_ in admin:
                    wait["Virus"] = False
                    wait["Ghost"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    avril.sendText(msg.to,"Auto Tag Sudah Aktif")
		else:
		    avril.sendText(msg.to,"Khusus avril")

            elif msg.text in ["Tag off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    avril.sendText(msg.to,"Auto Tag Di Nonaktifkan")
		else:
		    avril.sendText(msg.to,"Khusus avril")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["Virus"] = False
                    wait["Ghost"] = False
                    wait["detectMention3"] = False                    
                    avril.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    avril.sendText(msg.to,"Khusus avril")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    avril.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    avril.sendText(msg.to,"Khusus avril")			  
		 
            elif msg.text in ["Add:on","Add on"]:
                if wait["autoAdd"] == True:
                   if wait["lang"] == "JP":
                       avril.sendText(msg.to,"Sudah On Bos Quh")
                   else:
                       avril.sendText(msg.to,"Sudah On Bos Quh")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sudah On Bos Quh")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah on")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Hal ini sudah off")
                    else:
                        avril.sendText(msg.to,"Hal ini sudah dimatikan")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sudah Off Bos Quh")
                    else:
                        avril.sendText(msg.to,"Untuk mengaktifkan-off")

 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                avril.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    avril.sendText(msg.to,"Khusus avril")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                avril.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    avril.sendText(msg.to,"Khusus avril")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                avril.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    avril.sendText(msg.to,"Khusus avril")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                avril.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    avril.sendText(msg.to,"Khusus avril")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	avril.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    avril.sendText(msg.to,"Khusus avril")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	avril.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    avril.sendText(msg.to,"Khusus avril")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     avril.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        avril.sendText(msg.to,"Khusus avril")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     avril.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        avril.sendText(msg.to,"Khusus avril")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True
                    avril.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    avril.sendText(msg.to,"Khusus avril")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False
                    avril.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    avril.sendText(msg.to,"Khusus avril")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                avril.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                avril.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                avril.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                avril.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sambutan Di Aktifkan")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Sudah Off(p′︵‵。)")

            elif "Send " in msg.text:
                    cond = msg.text.split(" ")
                    target = cond[1]
                    text = msg.text.replace("Send " + str(target) + " Chat ","")
                    try:
                        avril.findAndAddContactsByMid(target)
                        sendMessage(target,"From Alin : \"" + text + "\"")
                        sendMessage(msg.to,"Berhasil mengirim pesan")
                    except:
                        sendMessage(msg.to,"Gagal mengirim pesan, mungkin midnya salah")
                        
            elif "Sniper on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                avril.sendText(msg.to,"Mode Sniper On")
                
            elif "Sniper off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    avril.sendText(msg.to, "Mode Sniper Off")
                else:
                    avril.sendText(msg.to, "Heh Belom Di Set")                         

            elif msg.text in ["Set"]:
                md = ""
		if wait["Sambutan"] == True: md+="🔧 Sambutan : On🔓\n\n"
		else:md+="🔧🔒 Sambutan : Off\n\n"
		if wait["AutoJoin"] == True: md+="🔧 Auto Join : On🔓\n\n"
                else: md +="🔧🔒 Auto Join : Off\n\n"
		if wait["AutoJoinCancel"] == True: md+="🔧 Auto Join Cancel : On🔓\n\n"
                else: md +="🔧🔒 Auto Join Cancel : Off\n\n"                
		if wait["Contact"] == True: md+="🔧 Info Contact : On🔓\n\n"
		else: md+="🔧🔒 Info Contact : Off\n\n"
                if wait["AutoCancel"] == True:md+="🔧 Auto Cancel : On🔓\n\n"
                else: md+= "🔧🔒 Auto Cancel : Off\n\n"
                if wait["autoAdd"] == True:md+="🔧 Auto Add : On🔓\n\n"
                else: md+= "🔧🔒 Auto Add : Off\n\n"
                if wait["inviteprotect"] == True:md+="🔧 Invite Protect : On🔓\n\n"
                else: md+= "🔧🔒 Invite Protect : Off\n\n"                
		if wait["Qr"] == True: md+="🔧 Qr Protect : On🔓\n\n"
		else:md+="🔧🔒 Qr Protect : Off\n\n"
		if wait["AutoKick"] == True: md+="🔧 Auto Kick : On🔓\n\n"
		else:md+="🔧🔒 Auto Kick : Off\n\n"
		if wait["Ghost"] == True: md+="🔧 Ghost : On🔓\n\n"
		else:md+="🔧🔒 Ghost : Off\n\n"
		if wait["alwaysRead"] == True: md+="🔧 Always Read : On🔓\n\n"
		else:md+="🔧🔒 Always Read: Off\n\n"
		if wait["Tagvirus"] == True: md+="🔧 Virus : On🔓\n\n"
		else:md+="🔧🔒 Virus : Off\n\n"		
		if wait["detectMention2"] == True: md+="🔧 Auto Respon2 : On🔓\n\n"
		else:md+="🔧🔒 Auto Respon2 : Off\n\n"	
		if wait["detectMention3"] == True: md+="🔧 Auto Respon3 : On🔓\n\n"
		else:md+="🔧🔒 Auto Respon3 : Off\n\n"			
		if wait["kickMention"] == True: md+="🔧 Auto Respon Kick : On🔓\n\n"
		else:md+="🔧🔒 Auto Respon Kick : Off\n\n"				
		if wait["Sider"] == True: md+="🔧 Auto Sider : On🔓\n\n"
		else:md+="🔧🔒 Auto Sider: Off\n\n"	
		if wait["Simi"] == True: md+="🔧 Simisimi : On🔓\n\n"
		else:md+="🔧🔒 Simisimi: Off\n"		
                avril.sendText(msg.to,"⛥҉ S҉ E҉ T҉ T҉ I҉ N҉ G҉ S҉ ⛦҉ \n\n"+md+"\n\n")

            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                avril.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = avril.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    avril.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    avril.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = avril.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 avril.sendMessage(cnt)
                 
#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag","Cuy","Hem","Crit"]:
                  group = avril.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                      tagall(msg.to, nama)
                  if jml > 100 and jml < 500:
                      for i in range(0,99):
                          nm1 += [nama[i]]
                      tagall(msg.to, nm1)
                      for j in range(100, len(nama)-1):
                          nm2 += [nama[j]]
                      tagall(msg.to, nm2)
                      for k in range(200, len(nama)-1):
                          nm3 += [nama[k]]
                      tagall(msg.to, nm3)
                      for l in range(300, len(nama)-1):
                          nm4 += [nama[l]]
                      tagall(msg.to, nm4)
                      for m in range(400, len(nama)-1):
                          nm5 += [nama[m]]
                      tagall(msg.to, nm5)
                  cnt = Message()
                  cnt.text = "Total : " + str(jml) +  " Nyawa "
                  cnt.text = "❍••••••{Mention By:}••••••❍\n\n❍•••{ᎪᏙᎡᏆᏞᏆᎪ_ᏞᎬᏙᎪNᎪ}•••❍\n\nTotal: " + str(jml) +  " Nyawa\n"+ datetime.now().strftime('%H:%M:%S')
                  cnt.to = msg.to
                  avril.sendMessage(cnt)
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "❂••••••{Mention By:}••••••❂\n\n❂•••{ᎪᏙᎡᏆᏞᏆᎪ_ᏞᎬᏙᎪNᎪ}•••❂\n\n"+ datetime.now().strftime('%H:%M:%S')
                      cnt.to = msg.to
                      avril.sendMessage(cnt)
#-------------Fungsi Tag All Finish--------------#
            elif "tagall" == msg.text.lower():
                 group = avril.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 avril.sendMessage(cnt)                 


            elif msg.text in ["Setview","Start","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                avril.sendText(msg.to, "L O A D I N G S . . . .")
                avril.sendText(msg.to, "███████████▒%")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Finish","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('success')
                            pass
                    contactId = avril.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔❂•┅═ই✪͜͡ KANG NGINTIP ͜͡✪ई═┅•❂\n║\n╠ ͜͡✪➢"
                        grp = '\n╠ ͜͡✪➢ '.join(str(f) for f in dataResult)
                        total = '\n║\n╠❂•••┅═ই✪͜͡ ❂❂❂ ͜͡✪ई═┅•••❂\n║\n╠ ͜͡✪➢ Total %i Kang Ngintip (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n║\n║\n╚❂•┅═ই✪͜͡ KANG NGINTIP ͜͡✪ई═┅•❂"
                        avril.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        avril.sendText(msg.to, "Cctv Jones Seumur Hidup...amiin ")                        
                    else:
                        avril.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    avril.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    avril.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = avril.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    avril.findAndAddContactsByMids(mi_d)
		    avril.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                avril.sendText(msg.to,"Send Contact")
                
                
            elif msg.text in ["Runtime"]:
                avril.sendText(msg.to,"Bot Has Ben Acktif : 196 jam 02 menit 48 detik")
                
                

            elif msg.text in ["Like on"]:
                wait["likeOn"] = True
                avril.sendText(msg.to,"Likers Activ")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                avril.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                avril.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                avril.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                avril.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                avril.sendText(msg.to,"Bot Sudah Di Nonaktifkan Boss Quh...")  

	    elif "Recover" in msg.text:
		thisgroup = avril.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		avril.createGroup("Recover", mi_d)
		avril.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = avril.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    avril.updateGroup(X)
                else:
                    avril.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    avril.kickoutFromGroup(msg.to,[midd])
		else:
		    avril.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                avril.findAndAddContactsByMid(midd)
                avril.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "ubd7b4dd119abd73ab3df542fb58a8a65"
                avril.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = avril.getGroup(msg.to)
                avril.sendText(msg.to,"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█░░╔╦╗ ╔╗░░█\n█░░─║─ ║║░░█\n█░░─╩ ─╚╝░░█\n\n❍•••{☠ :" + gs.name+ ": ☠}•••❍\n\nSemoga Betah Kakak\nJangan Lupa Nikung Yehkan...\nDah Gitu Ajah\n\n[TQ]\n\n\n===❍•••{☠ʟᴇᴠᴀɴᴀ☠}•••❍===\n\n"+ datetime.now().strftime('%H:%M:%S'))
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                avril.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = avril.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			avril.sendText(i,"╔═──────┅═ই✪͜͡ B⃫̳̳ ̳R⃫̳̳ ̳O⃫̳̳ ̳A⃫̳̳ ̳D⃫̳̳ ̳C⃫̳̳ ̳A⃫̳̳ ̳S⃫̳̳ ̳T⃫̳̳ ̳ ͜͡✪ई═┅───────\n\n"+bc+"\n\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠̶A̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེV̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེR̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེI̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེL̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེI̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེA̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶ེ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────\n"+ datetime.now().strftime('%H:%M:%S'))
		    avril.sendText(msg.to,"Success BC BosQ")
		else:
		    avril.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = avril.getGroupIdsInvited()
                for i in gid:
                    avril.rejectGroupInvitation(i)
                avril.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = avril.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        avril.updateGroup(x)
                    gurl = avril.reissueGroupTicket(msg.to)
                    avril.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        avril.sendText(msg.to,"Can't be used outside the group")
                    else:
                        avril.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = avril.activity(limit=5)
		    avril.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    avril.leaveGroup(msg.to)		    
		    
#-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Jam",""]:
              #if msg.from_ in admin:
                avril.sendText(msg.to,"̶Timer:̶ " + datetime.now().strftime('%H:%M:%S'))


            elif msg.text.lower() in ["respon"]:
                avril.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start                
                avril.sendText(msg.to, "「Progress...」\n「 99%##############.」")
                avril.sendText(msg.to, "%sseconds" % (elapsed_time))
                                
            elif msg.text in ["Testing"]:
                start = time.time()
                avril.sendText(msg.to, "Speedy...")
                avril.sendText(msg.to, "「Progress...」\n「 99%##############.」")
                elapsed_time = time.time() - start
                avril.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    avril.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    avril.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    avril.sendText(msg.to,"Succes BosQ")
                                except:
                                    avril.sendText(msg.to,"Success")
			    else:
				avril.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    avril.sendText(msg.to,"send contact")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +avril.getContact(mi_d).displayName + "\n"
                    avril.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                avril.sendText(msg.to,"Succes BosQ")
                            except:
                                avril.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    avril.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = avril.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            avril.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            avril.kickoutFromGroup(msg.to,[jj])
                        avril.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    avril.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = avril.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            avril.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                avril.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Bar" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("Bar","")
                    gs = avril.getGroup(msg.to)
                    h = avril.getContact(mid)
                    avril.sendText(msg.to,"──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅───────")
                    avril.sendText(msg.to,"🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n🄺🄸🄲🄺🄴🅁 🄰🅁🄴🄽🄰\n_______________________________ ")
                    avril.sendText(msg.to,"【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】")
                    #avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+h.pictureStatus)
                    #avril.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/0h4f8Us-i0a0kFLEezZY8UHjlpZSRyAm0BfU12fXV_PCwtTipPOxghe3IkPHshFS5Pakl0LXcuYi0h")
                    avril.sendText(msg.to,"⚠️⚠️__AWAS!!! __⚠️⚠️\n___TANPA PERMISI GW___\n🔥 BAKAR GRUP LO NYET!!🔥\n___JANGAN TANYA KENAPA___\n😎KARNA KAMI PUNYA PRINSIF 😎\n  KALO GAK RATA ZOOM MUKA KANG KIBAR\n\n\n──────┅═ই۝ई═┅──────\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n       ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n      line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────\n\n\nKAMI TAU APA!!?? KAMI HANYA NUMPANG KIBAR&PLAY\n\n\nDAH GITU AJA TQ\n\n\n(itu)JADI TANGKIS AJE BOSS (itu)\n\n\nGO!!  GO!!  GO!!  GO!!  GO!!\n\n\n________ (go)________ ")
                    avril.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u17a086ccff618e754588a1108335867f"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2552e86aab1b1426749dd0439b0f8c7f"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc67a847198ce188b412a058d86f10367"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u190afbb99dd1c28cc57642627f2aa1a2"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u12322ff2ca2b48474389f3d91b9ff385"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2beb70887d61c0e3abf3ac327b7b21d9"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub08e59948aaf244041d99091254e743c"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2c83fe9f836a2f74f7f9316e0c184f9d"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u02c62ba90a4f9ff95950d1a5ee9f2154"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u47b8e60143e0e1c6fdebe67e6a355ad2"}
                    avril.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u70489ca3e0d013e866a556665ee9d99b"}
                    avril.sendMessage(msg)
                    avril.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    avril.sendText(msg.to,"★_____TANGKIS NYETT_____★\n\nUDAH GITU  AJA YANG PENTING KIBAR\n\n🔥RATA KAMI SENANG GAK RATA BULY AJE KAMI  DISINI🔥\n\n\n__JADI TANGKIS AJA GO_GO_GO_!!!!!__\n\n______【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】______ ")
                    avril.sendText(msg.to,"──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅─────── ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Set Kibaran Succes Boss Quh ...Dah Gitu Aja...\nTQ")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[avril,]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                avril.sendText(msg,to,"Group cleanse")

            elif "BLACK ANGEL'S" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("BLACK ANGEL'S","")
                        gs = avril.getGroup(msg.to)
                        avril.sendText(msg.to,"ARE YOU READY....")
                        avril.sendText(msg.to,"GO..")
                        avril.sendText(msg.to,"GO..")
                        avril.sendText(msg.to,"GO..")
                        avril.sendText(msg.to,"GOOOO.............!!!!!!!!!")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            avril.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        avril.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        avril.sendText(msg.to,str(e))
			    #avril.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Restart","Reboot"]:
		if msg.from_ in Creator:
		    avril.sendText(msg.to, "Bot Restarted Loadings...ฺ")
		    avril.sendText(msg.to, "███████████▒99%")
		    avril.sendText(msg.to, "Succes Restarted Bot ✔")
		    restart_program()
		    print "@Restart"
		else:
		    avril.sendText(msg.to, "Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Code #13' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65'"}
                avril.sendMessage(msg)
                
            elif msg.text in ["Mylove"]:
              #if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u5f53c8be64a7264219e35aaeb4fc6ca2'}
                avril.sendText(msg.to,"❂•••••┅═ই💖💖💘💖💖ई═┅••••••❂")
                avril.sendText(msg.to,"_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██")
                avril.sendMessage(msg)
                avril.sendText(msg.to,". . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *")
                avril.sendText(msg.to,"❂•••••┅═ই💖💖💘💖💖ई═┅••••••❂")
                avril.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█")
                avril.sendText(msg.to, "😍😍😍😍😍\nPacarnya Avril Ini Mah....!!!! 😘😘😘😘😘")
                
            elif msg.text in ["Love"]:
              #if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ubd7b4dd119abd73ab3df542fb58a8a65'}
                avril.sendText(msg.to,"❂•••••┅═ই💖💖💘💖💖ई═┅••••••❂")
                avril.sendText(msg.to,"_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██")
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u5f53c8be64a7264219e35aaeb4fc6ca2'}
                avril.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█")
                avril.sendMessage(msg)
                avril.sendText(msg.to,"❂•••••┅═ই💖💖💘💖💖ई═┅••••••❂")
                avril.sendText(msg.to,"💘💘💘🌹😘🌹😘🌹💘💘💘")

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = avril.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       avril.sendText(msg.to, "Ok...")
                   else:
                       for target in targets:
                            try:
                               avril.CloneContactProfile(target)
                               avril.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    avril.updateDisplayPicture(backup1.pictureStatus)
                    avril.updateProfile(backup1)
                    avril.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    avril.sendText(msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						avril.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						avril.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						avril.sendAudioWithURL(msg.to,abc)
						avril.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        avril.sendText(msg.to, hasil)
                except Exception as wak:
                        avril.sendText(msg.to, str(wak))
                        
	    elif "Musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						avril.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						avril.sendAudioWithURL(msg.to,abc)
						avril.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						avril.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    avril.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = avril.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                avril.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                avril.sendText(msg.to,"Upload image success.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = avril.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                avril.sendText(msg.to,"Upload image success.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "avril.jpg"
                    avril.sendText(msg.to,"Update PP :")
                    avril.sendImage(msg.to,path)
                    avril.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = avril.getContact(target)
                                avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                avril.sendText(msg.to,"Upload image success.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = avril.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        avril.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = avril.getContact(target)
                                avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                avril.sendText(msg.to,"Upload image success.")

            elif msg.text in ["pap owner","pap creator"]:
                                h = avril.getContact(mid)
                                avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ h.pictureStatus)

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    avril.sendText(msg.to,"spam changed")
                else:
                    avril.sendText(msg.to,"Done")
 
            elif "Clone " in msg.text:
                  bctxt = msg.text.replace("Clone ", "")
                  t = 100
                  while(t):
                    avril.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = avril.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      avril.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = avril.getAllContactIds()
                  for manusia in orang:
                    avril.sendText(manusia, (broadcasttxt))
                   
            elif msg.text in ["Gspam on"]:
	          if msg.from_ in admin:
				wait["spammed "] = True
				avril.sendText(msg.to,"send contact")
#==============================================
            elif "Sp @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Sp @","")
                _nametarget = _name.rstrip(' ')
                gs = avril.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                        avril.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/AqTXMqygnD\n╚═────────┅═ই۝ई═┅─────────")
                    else:
                        pass
                        
            elif "Kelinci @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Kelinci @","")
                _nametarget = _name.rstrip(' ')
                gs = avril.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       avril.sendText(msg.to, "Success To Pm Target")
                       print " Spammed !"
                       
            elif "To @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("To @","")
                _nametarget = _name.rstrip(' ')
                gs = avril.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       avril.sendText(g.mid,"_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██")
                       avril.sendText(g.mid,". . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *")
                       avril.sendText(g.mid,"(¯`v´¯) Love Me\n`*.¸.*´ ?\n¸.•´¸.•*¨) ¸.•*¨)?\n(¸.•´ (¸.•´ .•´ ¸¸.•¨¯`•.\n(¯`v´¯)\n.`·.¸.·´ ?\n¸.·´¸.·´¨) ¸.·*¨)\n(¸.·´ (¸.·´ .·´ ¸")
                       avril.sendText(msg.to, "Succes To Pm Target")
                       print " Spammed !"
                       
            elif "S @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("S ","")
                _nametarget = _name.rstrip(' ')
                gs = avril.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       avril.sendText(msg.to, "Success To Spam Target.")
                       print " Spammed !"
                       
            elif "Mybots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Ud7c6e2f0fdd808d5305ec7525158f68e"}
                avril.sendMessage(msg)
                avril.sendText(msg.to,"Done..!!!")
 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    avril.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    avril.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	avril.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                avril.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                avril.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    avril.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    avril.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        avril.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        avril.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = avril.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hi","hy","halo","hallo","hay"]:
                    beb = "Hi Sayang 😘 Miss You " +avril.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    avril.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                avril.sendText(msg.to,"Sedang Mencari...")
                avril.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                avril.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = avril.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        avril.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = avril.getProfile()
                        profile.statusMessage = string
                        avril.updateProfile(profile)
                        avril.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = avril.getProfile()
                        profile.displayName = string
                        avril.updateProfile(profile)
                        avril.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +avril.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                avril.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                avril.sendText(msg.to,"❂•••••••┅═ই۝ई═┅••••••••❂")
                h = avril.getContact(mid)
                #avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                avril.sendText(msg.to,"❂•••••••••••✧•••••••••••❂")
                avril.sendMessage(msg)
                avril.sendMessage(msg)
                avril.sendText(msg.to,"❂•••••••••••✧•••••••••••❂")
                h = avril.getContact(mid)
                #avril.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                #avril.sendText(msg.to,"_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██")
                #avril.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█")
                avril.sendText(msg.to,"❂•••••••┅═ই۝ई═┅••••••••❂")
                avril.sendText(msg.to,"[Avrilia Ini Mahh...!!!]\nDah Gitu Aja\n[TQ]\n\n"+ datetime.now().strftime('%H:%M:%S'))

            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")   


            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                avril.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                avril.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                avril.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    avril.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        avril.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                avril.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                avril.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                avril.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                avril.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                avril.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                avril.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                avril.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = avril.getAllContactIds()
                kontak = avril.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                avril.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = avril.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                avril.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = avril.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    avril.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = avril.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            avril.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = avril.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                avril.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = avril.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                avril.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = avril.getContact(key1)
                cu = avril.channel.getCover(key1)
                try:
                    avril.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    avril.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = avril.getContact(key1)
                cu = avril.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    avril.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    avril.sendText(msg.to,"Profile Picture " + contact.displayName)
                    avril.sendImageWithURL(msg.to,image)
                    avril.sendText(msg.to,"Cover " + contact.displayName)
                    avril.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "You" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = avril.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                avril.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = avril.getContact(key1)
                cu = avril.channel.getCover(key1)
                try:
                    avril.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    avril.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = avril.getContact(key1)
                cu = avril.channel.getCover(key1)
                try:
                    avril.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    avril.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtimer':
                eltime = time.time() - mulai
                van = "===❍•••{☠ʙᴏᴛ\nsᴜᴅᴀʜ ʙᴇʀᴊᴀʟᴀɴ\nsᴇʟᴀᴍᴀ☠}•••❍=== :\n"+waktu(eltime)
                avril.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                avril.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                avril.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = avril.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                avril.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = avril.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                avril.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        avril.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        avril.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        avril.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        avril.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            avril.findAndAddContactsByMid(msg.from_)
                            avril.inviteIntoGroup(gid,[msg.from_])
                        except:
                            avril.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                avril.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = avril.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (avril.getGroup(i).name +" ~> ["+str(len(avril.getGroup(i).members))+"]")
                avril.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = avril.getGroupIdsJoined()
                kontak = avril.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                avril.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    avril.sendText(msg.to,"Sedang Mencari...")
                    avril.sendText(msg.to, "https://www.google.com/" + b)
                    avril.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        avril.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = avril.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            avril.sendText(msg.to,h)
                        except Exception as error:
                            avril.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = avril.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                avril.rejectGroupInvitation(i)
                            except:
                                avril.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        avril.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        avril.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = avril.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = avril.getGroup(i)
                            _list += gids.name
                            avril.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        avril.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        avril.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                avril.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        avril.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        avril.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        avril.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        avril.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            avril.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+avril.getContact(mi_d).displayName + "\n"
                            avril.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                avril.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                avril.sendText(msg.to,"Mimic change to target")
                            else:
                                avril.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        avril.sendText(msg.to,"Reply Message on")
                    else:
                        avril.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        avril.sendText(msg.to,"Reply Message off")
                    else:
                        avril.sendText(msg.to,"Sudah off")
#------------------------------------------------------------------
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = avril.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        avril.cancelGroupInvitation(msg.to,[_mid])
                    avril.sendText(msg.to,"Success vril...")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = avril.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            group.name = name
                            avril.updateGroup(group)
                    except:
                        avril.sendText(msg.to,"Success")
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = avril.fetchOps(avril.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(avril.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            avril.Poll.rev = max(avril.Poll.rev, Op.revision)
            bot(Op)

