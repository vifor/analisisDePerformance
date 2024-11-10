# Trabajo Practico BD

## Autores

- **Verena Olsowy** 
- **Victoria Pocladova** 

## Contenedores Docker
Este proyecto utiliza Docker para administrar los ambientes. 
A continuacion se presentan las especificaciones utilizadas para cada base de datos que formó parte del estudio comparativo


### MySQL

``````python
cd mysql
docker-compose up --build
``````

Una vez levantado se puede ver desde consola el listado de contenedores
docker ps

Identificado el contenedor que contiene mysql se puede conectar a el usando
``````
docker exec -it 2b91c2c bash
``````
donde 2b91c2c tiene que ser reemplazado por el id del contenedor

Desde el contenedor se puede conectar a mysql
mysql -h localhost -P 3306 -u test_user -p
