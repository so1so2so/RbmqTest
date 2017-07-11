#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pika
user = 'admin'
pwd = 'admin123'
user_pwd = pika.PlainCredentials(user, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '192.168.1.9', credentials=user_pwd))
# 声明一个管道,开了一条路,路上有车
channel = connection.channel()
# 声明一个queue,这个就等于是车
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',  # 路上的
                      routing_key='hello',   # queue名称
                      body='这个世界真好')  # 消息内容
print(" [x] Sent 'Hello World!'")
# 关闭队列
connection.close()