from elasticsearch import Elasticsearch
from user_data import get_user
import json

es = Elasticsearch()


def main():
    print("Running sender...")
    for x in range(999):
        execute_sender()
    print("Terminate.")


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def cursor_total():
    res = es.search(index="inter-sample", query={"match_all": {}})
    total = int(res["hits"]["total"]["value"])
    return total


def execute_sender():

    user = get_user()
    doc = json_serializer(user)
    offset = cursor_total() + 1

    res = es.index(index="inter-sample", id=offset, document=doc)
    print(res["result"])
    print(doc)


if __name__ == "__main__":
    main()
