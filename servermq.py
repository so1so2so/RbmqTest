#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pika
user = 'admin'
pwd = 'admin123'
user_pwd = pika.PlainCredentials(user, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '192.168.1.9', credentials=user_pwd))
channel = connection.channel()

# 这个队列收消息
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print ch, method, properties, body
    # ch 管道内存地址
    # method que发送什么 发给谁
    # body 收到的内容
    print(" [x] Received %r" % body)
# 开始收消息
channel.basic_consume(callback,  # 如果收到消息,就调用callback函数来处理消息
                      queue='hello',  # 重那个队列收消息
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始收消息
channel.start_consuming()