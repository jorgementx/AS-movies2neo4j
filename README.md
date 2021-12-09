# AS-movies2neo4j

En caso de querer correr únicamente el docker de Neo4j:

> docker run -d --network todo-app --network-alias neo4j --publish=7474:7474 --publish=7687:7687  --env=NEO4J_AUTH=none   --volume=$HOME/neo4j/data:/data neo4j

