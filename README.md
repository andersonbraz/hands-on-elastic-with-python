# HandsOn Elastic with Python

### Criar Diretório Colabs

```shell
mkdir -p ~/Colabs
```
### Clonar Projeto

```shell
git clone git@gitlabssh.sharedservices.local:BI004609/hands-on-elastic-with-python.git ~/Colabs
```

ou

```shell
git clone https://gitlab.sharedservices.local/BI004609/hands-on-elastic-with-python.git
```
### Abrir o Projeto

```shell
code hands-on-elastic-with-python
```

### Criar Ambiente Python do Projeto

```shell
python3 -m venv .venv
```

### Ativar Ambiente Python do Projeto

```shell
. .venv/bin/activate
```
### Atualizar Ambiente Python do Projeto

```shell
python3 -m pip install --upgrade pip
```

### Instalar Dependências Necessárias

```shell
pip install Elasticsearch
pip install Faker
```

### Executar Projeto

```shell
python src/main.py
```
### Instalação do Connector Elastic Source

```shell
confluent-hub install dariobalinzo/kafka-connect-elasticsearch-source:1.5.0
```

### Instalação Connector FileStreamSink

```shell
cd ~/Apps/confluent-7.0.0/
cp ./share/filestream-connectors/connect-file-7.0.0-ce.jar share/java
```
### Adicionar Connector Elastic Source 

```shell
curl -X POST -H "Content-Type:application/json" --data '{"name":"elastic-source","config":{"connector.class":"com.github.dariobalinzo.ElasticSourceConnector","tasks.max":"1","es.host":"localhost","es.port":"9200","index.prefix":"inter-sample","topic.prefix":"es_","incrementing.field.name":"id", "topics":"es_inter-sample","key.converter":"io.confluent.connect.avro.AvroConverter", "key.converter.schema.registry.url":"http://localhost:8082","value.converter":"io.confluent.connect.avro.AvroConverter","value.converter.schema.registry.url":"http://localhost:8082"}}' http://localhost:8083/connectors
```

### Adicionar Connector FileStreamSink

```shell
curl -X PUT -H "Content-Type: application/json" --data '{"connector.class":"FileStreamSink","tasks.max":1,"file":"/Users/bi004609/Apps/confluent-7.0.0/es_inter-sample.txt", "topics":"es_inter-sample"}' localhost:8083/connectors/file-stream-sink/config
```
### Adicionar Connector S3-Sink

```shell
curl -X PUT -H "Content-Type: application/json" --data '{"name": "s3-sink","connector.class": "io.confluent.connect.s3.S3SinkConnector","topics": "es_inter-sample","flush.size": "1","s3.bucket.name": "mktd-dev-test-inter-sample","s3.region": "us-east-1","storage.class": "io.confluent.connect.s3.storage.S3Storage","format.class": "io.confluent.connect.s3.format.avro.AvroFormat"}' localhost:8083/connectors/s3-sink/config
```

```shell
curl -X PUT -H "Content-Type: application/json" --data '{"name": "s3-sink","connector.class": "io.confluent.connect.s3.S3SinkConnector","topics": "es_inter-sample","flush.size": "1","s3.bucket.name": "mktd-dev-test-inter-sample","s3.region": "us-east-1","storage.class": "io.confluent.connect.s3.storage.S3Storage","format.class": "io.confluent.connect.s3.format.avro.AvroFormat","locale":"pt-BR","timezone":"America/Sao_Paulo"}' localhost:8083/connectors/s3-sink/config
```

### Utils

[Download Insomnia](https://insomnia.res/download)



