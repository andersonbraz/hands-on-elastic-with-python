from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    "author": "kimchy",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now(),
}
res = es.index(index="inter-sample", id=1, document=doc)
print(res["result"])

res = es.get(index="inter-sample", id=1)
print(res["_source"])

es.indices.refresh(index="inter-sample")

res = es.search(index="inter-sample", query={"match_all": {}})
print("Got %d Hits:" % res["hits"]["total"]["value"])
for hit in res["hits"]["hits"]:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
