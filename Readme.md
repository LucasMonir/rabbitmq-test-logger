**How to use this simple code**
# Simple RabbitMQ app in python

----------
## You'll need:
* Python
* Pika lib
* ... 5 minutes of your time

## How to use it
* run the consumer, specifying the type of log you want it to receive (info, error, warning)
* then, run the producer, which will randomly select a message and a type to be sent
* well that's it

### Based
[Example 5 from RabbitMQ's tutorial section](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)