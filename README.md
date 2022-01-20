# HandsOn Elastic with Python

## Create Folder Colabs

```shell
mkdir -p ~/Colabs
cd ~/Colabs
```
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
## Check 

```shell
curl http://127.0.0.1:8083/connectors/elastic-source/status
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

## Install Connector FileStreamSink

```shell
cd ~/Apps/confluent-7.0.0/
cp ./share/filestream-connectors/connect-file-7.0.0-ce.jar share/java
```
## Setting Connector Elastic Source 

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es_","incrementing.field.name":"id"}}' http://localhost:8083/connectors
```

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es_","incrementing.field.name":"id", "topics":"es_inter-sample","key.converter":"io.confluent.connect.avro.AvroConverter", "key.converter.schema.registry.url":"http://localhost:8082","value.converter":"io.confluent.connect.avro.AvroConverter","value.converter.schema.registry.url":"http://localhost:8082"}}' http://localhost:8083/connectors
```

## Setting Connector FileStreamSink

```shell
curl -X PUT -H "Content-Type: application/json" --data '{"connector.class":"FileStreamSink","tasks.max":1,"file":"/Users/bi004609/Apps/confluent-7.0.0/test.sink.txt", "topics":"es_inter-sample"}' localhost:8083/connectors/file-stream-sink/config
```


```shell
curl -X PUT -H "Content-Type: application/json" --data '{"connector.class":"FileStreamSink","tasks.max":1,"file":"/Users/bi004609/Apps/confluent-7.0.0/es_inter-sample.avro", "topics":"es_inter-sample","key.converter":"io.confluent.connect.avro.AvroConverter", "key.converter.schema.registry.url":"http://localhost:8082","value.converter":"io.confluent.connect.avro.AvroConverter","value.converter.schema.registry.url":"http://localhost:8082"}' localhost:8083/connectors/file-stream-sink/config
```

