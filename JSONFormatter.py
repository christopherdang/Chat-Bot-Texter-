import json

#with open('sms.json', encoding="utf8") as f:
#    data = json.load(f)

#for contact in data['smses']['sms']:
#    del contact['@date']
#    del contact['@date_sent']
#    del contact['@locked']
#    del contact['@protocol']
#    del contact['@read']
#    del contact['@readable_date']
#    del contact['@sc_toa']
#    del contact['@service_center']
#    del contact['@status']
#    del contact['@sub_id']
#    del contact['@subject']
#    del contact['@toa']
#    del contact['@type']
#    print(contact)

#with open('new_sms.json', 'w') as f:
#    json.dump(data, f, indent=2)

counter = 0

with open('Dj_intents2.json') as f:
    data = json.load(f)

for message in data['intents']:
    message['tag'] = counter
    message['responses'] = message['responses'][0]
    message['patterns'] = message['patterns'][0]
    counter = counter + 1

print(data)

with open('new_file.json', 'w') as f:
    json.dump(data, f, indent=2)