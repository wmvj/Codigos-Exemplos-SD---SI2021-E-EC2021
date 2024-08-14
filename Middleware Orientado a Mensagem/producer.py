import rabbitpy


def producer():
    connection = rabbitpy.Connection()
    channel = connection.channel()

    exchange = rabbitpy.Exchange(channel, 'exchange')
    exchange.declare()

    queue1 = rabbitpy.Queue(channel, 'example1')
    queue1.declare()

    queue2 = rabbitpy.Queue(channel, 'example2')
    queue2.declare()

    queue1.bind(exchange, 'example-key')
    queue2.bind(exchange, 'example-key')

    message = rabbitpy.Message(channel, 'Test message')
    message.publish(exchange, 'example-key')
    exchange.delete()
