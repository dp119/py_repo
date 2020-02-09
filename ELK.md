
# <h2> What is Elasticsearch?

Fully distributed enterprise search and analytics engine.
Used to create own search engine or to analyze the data and extract useful information.

It's a document database 
we can query documents and run analysis and aggregations on search results.


Backend repository for logging and monitoring infrastructure.


Apache lucene is used as core search library to provide search functionality.

Popular enterprise search engine.



# <h3> ElasticSearch Features

Distributed and Scalable Horizontally

High Availability because of multiple copies of data

RESTful API to perform operations creating retrieving updating and deleting via simple JSON based HTTP calls

Powerful Query DSL - Express complex queries simply with JSON

Schemaless - (Index data without an explicit schema). Need not follow specific schema or datatypes or specific field names beforing indexing and parsing documents.


Examples - 
Ecommerce site to index product catalog, inventory, provide autocomplete for users

Video hosting site to index video clips, tags etc

E learning site to index courses, authors, topics covered




# <h3> Elastic components
Kibana is a data visualization.

Logstash is a data processing pipeline
which can analyze data from multiple sources.



Document is the smallest unit of data stored in elasticsearch.

Index is the collection of similar documents.

Shards is logically dividing the Index (helps easily searchable)

Node is a machine where the shard is hosted

Cluster is the collection of shards

Replica are backup of shards and contain exact same information as shard


With added node the shards are rebalanced automatically by ES


# <h2> Logstash
