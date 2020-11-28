from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.framework import React
from diagrams.onprem.client import Users
from diagrams.onprem.queue import Rabbitmq
from diagrams.programming.language import Java
from diagrams.programming.language import Go
from urllib.request import urlretrieve
from diagrams.custom import Custom

with Diagram("Architecture", show=False) as diagram:
    users = Users("Users")
    with Cluster("Zones"):
        zone = Server("Zone")
    with Cluster("System context"):
        react = React("Front")
        master = PostgreSQL("Stats DB")
        graphql_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/1200px-GraphQL_Logo.svg.png"
        graphql_icon = "graphql.png"
        urlretrieve(graphql_url, graphql_icon)
        graphql = Custom("Hasura", graphql_icon)
        adaptor = Java("Stats adaptor")
        with Cluster("Txs processors"):
            processor = Go("Processor")
        mq = Rabbitmq("Message queue")
        processor << mq
        with Cluster("Txs Watchers"):
            watcher = Go("Watcher")
    watcher >> mq
    react >> graphql
    graphql >> master
    master >> adaptor >> master
    master >> processor >> master
    users >> react
    zone >> watcher
diagram