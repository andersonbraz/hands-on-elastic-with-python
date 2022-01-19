from elasticsearch import Elasticsearch
from user_data import generate_user
import json
import time

es = Elasticsearch()


def main():
    print("Running sender...")
    for x in range(9):
        execute_sender()
    print("Terminate.")


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def cursor_total():
    res = es.search(index="inter-sample", query={"match_all": {}})
    total = int(res["hits"]["total"]["value"])
    return total


def execute_sender():

    offset = cursor_total() + 1
    user = generate_user(offset)
    doc = json_serializer(user)

    time.sleep(5)

    res = es.index(index="inter-sample", id=offset, document=doc)
    print(res["result"])
    print(doc)


if __name__ == "__main__":
    main()
