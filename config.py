#!/usr/bin/env python
# -*- coding: utf-8 -*-

ShouldBotLog = True  # If False bot will not create and keep bot.log file
BLACKLIST = ['']  # You can add words to the blacklist. If a post contains a blacklisted word, the post will be skipped
# BLACKLIST = ['ExAmPlE', 'etc', '123456789'] <== That's an example. But be careful. Do not add just one symbol to the list.

tgChannel = '@vlad_pidar'  # link to channel in telegram !!! you must add bot to this channel as an administrator
tgBotToken = '1685470996:AAGor6HbmRb48O22sARVCV3q784kkA6b378'  # your token from t.me/BotFather
vkToken = 'a095d7eba095d7eba095d7eb50a0e38500aa095a095d7ebc0b58a64345ea0681db19ba1'  # your token from https://vk.com/dev/authcode_flow_user
vkDomain = 'club202440551'  # domain of vk channel (vk.com/>>>>aaaaaaaa<<<<)

tgLogChannel = '@test_c_anal'  # link to another channel in telegram if you want to get bot's log message
                        # !!! you must add bot to this channel as an administrator
                        # yes, you can use the same bot as for the main task
tgBotForLogToken = ''   # set token here if you want vktgbot to use another bot for logging
                        # leave the variable empty if you want use first bot (tgBotToken) for logging 
                        # !!! you must add this bot to tgLogChannel as administrator 

reqVer = 5.126       # version of VK API [wall.get method]
reqCount = 3         # number of posts to return (2 - 100)
reqFilter = 'owner'  # Filter to apply: owner — posts by the wall owner; others — posts by someone else;
                     # all — posts by the wall owner and others (default)
                     # postponed — timed posts (only available for calls with an access_token)
                     # suggests — suggested posts on a community wall

singleStart = False
timeSleep = 20  # time in seconds
isPinned = False
skipAdsPosts = True
skipPostsWithCopyright = False

proxyEnable = False     # Set True if telegram is not available in your country
proxyLogin = "bot"      # Login for Socks5 proxy
proxyPass = "12345"     # Password for Socks5 proxy
proxyIp = "myproxy.com" # Socks5 proxy ip
proxyPort = "1234"      # Socks5 proxy port
