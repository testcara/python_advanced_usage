def consumer():
    print("---> [Start] Consumer ...")
    result = 0
    while True:
        data = yield result
        print("---> [Consumer] Consume the producer: %s" % data)
        result = data * data


def producer(c):
    print("---> [Start] Producer ...")
    # active the consumer
    c.send(None)
    for i in [1, 2, 3]:
        print("---> [Producer] Produce: %s" % i)
        result = c.send(i)
        print("---> [Producer] Got the result from the consumer: %s" % result)


c = consumer()
producer(c)
