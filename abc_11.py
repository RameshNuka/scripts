import json,requests
from datetime import datetime
from elasticsearch import Elasticsearch


def connectingto_esclient(host_ip,port,username,password):
    logging.info(" create elasticsearch client object ")
    es_instance = Elasticsearch([{'host': host_ip, 'port': port}],http_auth=('elastic', 'elastic'))
    print (es_instance.info())
    return es_instance

es = connectingto_esclient(host_ip,port,username,password)
print(es)
url=["https://jsonplaceholder.typicode.com/todos/1","www.dilip.com","www.abc.com"]
for u in url:
    response = requests.get(url)
    data = response.json()
    print(data)

    print(data["regDate"])
    today = datetime.now()
    date_string = today.strftime('%Y-%m-%d')
    print(date_string)

    if date_string==data["regDate"]:
        data_to_push = {
            "url": url,
            "datematched": 'matched'
        }

    es.index( index='indexname',document=data_to_push)



