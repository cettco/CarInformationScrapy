import json
f=open('scraped_id_data.json','r')
jsonT=json.loads(f.read())
a=[]
f.close()
for item in jsonT:
    ids=item['id']
    for mId in ids:
        a.append(mId[1:])
print len(a)
