FROM mysql
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/


