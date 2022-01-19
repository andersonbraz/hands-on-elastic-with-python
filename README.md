# HandsOn Elastic with Python


## Clone project

```shell
git clone https://github.com/andersonbraz/hands-on-elastic-with-python.git
```
## Open project

```shell
code hands-on-elastic-with-python
```

## Create Enviroment Pynton

```shell
python3 -m venv .venv
```

## Activate Enviroment Pynton

```shell
. .venv/bin/activate
```
## Update Enviroment Pynton

```shell
python3 -m pip install --upgrade pip
```

## Requirements

```shell
pip install Elasticsearch
pip install Faker
```

## Run project

```shell
python src/main.py
```

## References

[Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current)

[Guide How To Add Documents To An Index In Elasticsearch](https://kb.objectrocket.com/elasticsearch/guide-how-to-add-documents-to-an-index-in-elasticsearch)

[Python Elasticsearch Client](https://elasticsearch-py.readthedocs.io/en/v7.16.3/)

## Utils

[Download Insomnia](https://insomnia.res/download)

## Install Connector Elastic Source


```shell
confluent-hub install dariobalinzo/kafka-connect-elasticsearch-source:1.5.0
```

## Setting Connector Elastic Source

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es_","incrementing.field.name":"@timestamp"}}' http://localhost:8083/connectors
```

## Setting Connector Elastic Source using Id (type = Long)

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source1","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es1_","incrementing.field.name":"id"}}' http://localhost:8083/connectors
```
## Setting Connector Elastic Source using Created_at (type = Date)

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source2","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es2_","incrementing.field.name":"created_at"}}' http://localhost:8083/connectors
```

## Check 

```shell
curl http://127.0.0.1:8083/connectors/elastic-source/status
```