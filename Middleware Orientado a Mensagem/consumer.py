import rabbitpy


def consumer():
    connection = rabbitpy.Connection()
    channel = connection.channel()

    queue = rabbitpy.Queue(channel, 'example1')

    while len(queue) > 0:
        message = queue.get()
        print('Message Q1: %s' % message.body.decode())
        message.ack()

    queue = rabbitpy.Queue(channel, 'example2')

    while len(queue) > 0:
        message = queue.get()
        print('Message Q2: %s' % message.body.decode())
        message.ack()
