# AS-movies2neo4j
Proyecto desarrollado para la asignatura de Administración de Sistemas en relación a las técnologias de Docker, Kubernetes y Vagrant, donde hemos tenido que desarrollar una aplicación que complementara la imagen de docker que se nos hubiera asignado. En mi caso, esta ha sido la base de datos basada en grafos Neo4j.

- Para ejecutar la aplicación (en el mismo directorio donde se encuentre el docker-compose.yaml):
> docker-compose up

  Esto meterá datos en la base de datos por defecto (neo4j) del docker Neo4j después de correr el docker y conectarse a él.

- Para conectarnos a la web-app escribimos en el navegador:
>localhost:7474 (esto nos redirigira a localhost:7474/browser)

- En caso de querer correr únicamente el docker de Neo4j:
> docker run -d --network todo-app --network-alias neo4j --publish=7474:7474 --publish=7687:7687  --env=NEO4J_AUTH=none   --volume=$HOME/neo4j/data:/data neo4j

