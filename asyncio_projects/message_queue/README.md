# Message Queue Practice

Run below command in terminal:

```python
# Terminal 1
python mq_server.py

# Running client sender
# Terminal 2
python mq_client_sender.py --channel /queue/blah

# Running client listener
# Terminal 3
python mq_client_listen.py --listen /queue/blah

# Terminal 4
python mq_client_listen.py --listen /queue/blah

```
