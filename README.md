# AS-movies2neo4j

Para ejecutar la aplicación:
> docker-compose up

Esto meterá datos en la base de datos por defecto (neo4j) del docker Neo4j después de correr el docker y conectarse a él. para conectarnos a la web-app escribimos en el navegador:
>localhost:7474 (esto nos redirigira a localhost:7474/browser)

En caso de querer correr únicamente el docker de Neo4j:

> docker run -d --network todo-app --network-alias neo4j --publish=7474:7474 --publish=7687:7687  --env=NEO4J_AUTH=none   --volume=$HOME/neo4j/data:/data neo4j

