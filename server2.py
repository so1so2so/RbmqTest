#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pika
user = 'admin'
pwd = 'admin123'
user_pwd = pika.PlainCredentials(user, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '192.168.1.11', credentials=user_pwd))
channel = connection.channel()

# 这个队列收消息
channel.queue_declare(queue='hello2', durable=True)


def callback(ch, method, properties, body):
    print "开始处理消息"
    # print ch, method, properties, body
    # ch 管道内存地址
    # method que发送什么 发给谁
    # body 收到的内容
    import time
    time.sleep(5)
    print(" [x] Received %r" % body)
    # 确认消息是否处理完毕
    ch.basic_ack(delivery_tag=method.delivery_tag)
# 开始收消息
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,  # 如果收到消息,就调用callback函数来处理消息
                      queue='hello2',  # 重那个队列收消息
                      # no_ack=True
                      )
# no_ack=True 不确认消息是否处理完成
print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始收消息
channel.start_consuming()