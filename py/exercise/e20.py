import json
with open('data.json', 'rb') as infile:
    data = json.load(infile)

# print(type(data))
# print(data.keys())
# print()
data_list = data['events_data']
# print(len(data_list))
# print(type(data_list))
#
categories = []
for item in data_list:
    category = item['category']
    categories.append(category)
# print (categories)

import collections
c = collections.Counter()
for category in categories:
    c[category] += 1

# print (c)

table_clients = []
for item in data_list:
    client_id = item['client_id']
    # category = item['category']
    # if category == 'table':
    table_clients.append(client_id)
# print (table_clients)

c = collections.Counter()
for table_client in table_clients:
    c[table_client] += 1
# print(c)
print (len(c.keys()))
print(c[60459])

table_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'page':
      table_clients.append(client_id)
c = collections.Counter()
for table_client in table_clients:
    c[table_client] += 1
print(c[62602])

table_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'report':
      table_clients.append(client_id)
c = collections.Counter()
for table_client in table_clients:
    c[table_client] += 1
print (len(c.keys()))
print(c.keys())
