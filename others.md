
# <h4> What is Jboss or JBoss EAP (Enterprise application platform)?
=====================

JBoss is an application server platform used for hosting highly transactional Java applications.


Both JBoss and Tomcat are Java servlet application servers, but JBoss is a whole lot more. 
Tomcat is much more limited. 

One way to think of it is that JBoss is a JEE stack that includes a servlet container and web server, whereas Tomcat, for the most part, is a servlet container and web server.



JBoss EAP provides two operating modes for JBoss EAP instances: standalone server or managed domain. 
The standalone server operating mode represents running JBoss EAP as a single server instance. 
The managed domain operating mode allows for the management of multiple JBoss EAP instances from a single control point.

The management console and management command-line interface (CLI) make editing XML configuration files unnecessary and add the ability to script and automate tasks. 
While you can still edit the XML files manually it’s not suggested to do so.



Difference between web server and app server?
=====================


# <h4> What is artifactory?
=====================
Artifactory is a product by JFrog that serves as a binary repository manager. 

(That said very often one will use a 'artifactory' as a synonym of the more general binary repository, much like many people use Frigidaire or fridge to denote the refrigerator regardless if it is a Frigidaire brand or not)


The binary repository is a natural extension to the source code repository, in that it will store the outcome of your build process, often denoted as artifacts. Most of the times one would not use the binary repository directly but through a package manager that comes with the chosen technology.


# <h4> What is Elasticsearch?
===================== 
Fully distributed enterprise search and analytics engine.
Used to create own search engine or to analyze the data and extract useful information.

It's a document database 
we can query documents and run analysis and aggregations on search results.


Backend repository for logging and monitoring infrastructure.


Apache lucene is used as core search library to provide search functionality.

Popular enterprise search engine.



ElasticSearch Features
=====================
Distributed and Scalable Horizontally

High Availability because of multiple copies of data

RESTful API to perform operations creating retrieving updating and deleting via simple JSON based HTTP calls

Powerful Query DSL - Express complex queries simply with JSON

Schemaless - (Index data without an explicit schema). Need not follow specific schema or datatypes or specific field names beforing indexing and parsing documents.


Examples - 
Ecommerce site to index product catalog, inventory, provide autocomplete for users

Video hosting site to index video clips, tags etc

E learning site to index courses, authors, topics covered





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




# <h2> What is REST api?

REST - or Representational State Transfer 
(can be used over nearly any protocol, when used for web APIs it typically takes advantage of HTTP)

A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. 
REST leverages less bandwidth, making it more suitable for internet usage


(which is why REST technology is generally preferred to the more robust Simple Object Access Protocol (SOAP) technology)
