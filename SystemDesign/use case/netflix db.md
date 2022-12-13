[Business logic](https://www.geeksforgeeks.org/system-design-netflix-a-complete-architecture/) [🔗](#business-logic)

[Ram and SSD](https://netflixtechblog.com/evolution-of-application-data-caching-from-ram-to-ssd-a33d6fa7a690) [🔗](#ram-and-ssd)

# Business logic

Like/share/subscribe 

Watch time

Video title/labels/categories

Freshness

#  Database
## Billing

MySQL (for ACID compliance)
2 master - "Synchronous replication protocol” : 
- both primary and remote master confirm on write

- read replica are located in multiple node: local and cross-region

![png](../pics/netflix-2master-SQL.jpg)


## Viewing history

NoSQL (Cassandra):

viewing history
shard based on recency:
= Live Viewing History : small number of recent viewing historical data of users with frequent updates


Compressed Viewing History: A large amount of older viewing records


# Logging and Event search
Elastic Search: data visualization, customer support, and for some error detection in the system

# Data Processing 
1) Apache Chukwe = batch processing: Chukwe writes the event in the Hadoop file sequence format (S3).  then writes Hive in Parquet data format. 

2) Kafka: upload online events to S3, Elasticsearch, and secondary Kafka. 


# Recommendation model + ranking
#### model:
- content-based filtering:  classification-based or item-item collaborative filtering
- Collaborative filtering: user-user collaborative filtering

#### ranking: use offline + online 
- offline:  calculate similar users/videos are also running regularly 

- online: based on the user profile and his actions

combine and do ranking on the fly

# RAM and SSD
