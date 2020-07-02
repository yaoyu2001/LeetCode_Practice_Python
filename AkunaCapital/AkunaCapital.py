import collections
from datetime import datetime
# class HashTable:
#     def __init__(self, rawEvents):
#         """ Build a HashTable from a list of raw pipe-delimited DML Events """
#         self.raw_events = collections.defaultdict()  # TODO
#         for item in rawEvents:
#             temp_array = item.split("|")
#             if len(temp_array) == 3:
#
#
#     @property
#     def table(self):
#         """ Retrieve the current state of the HashTable
#
#         Returns
#         -------
#         dict(str, str): the key-value pairs
#         """
#         pass  # TODO
#
#     @property
#     def high_watermark(self):
#         """ Retrieve the high-watermark of the system  -- the UTC epoch millisecond timestamp of the latest
#         event read as a datetime or datetime.datetime.utcfromtimestamp(0) (Epoch 0) if no event occurred
#
#         Returns
#         -------
#         datetime.datetime: the high-watermark
#         """
#         pass  # TODO

date = 1563454984.003
print(datetime.fromtimestamp(date))

# str = '1563454984003'
# bytes = bytes(0000016c052dcf41)
# print(bytes.decode(bytes))

a='1563454984003'
b=bytes(a,encoding='utf-8')
print(b)