FROM mysql:5.7

COPY webappdb.sql /mysql/webappdb.sql
ADD webappdb.sql /docker-entrypoint-initdb.d
