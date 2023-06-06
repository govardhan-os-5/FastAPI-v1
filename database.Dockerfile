FROM mysql:8.0

ENV MYSQL_DATABASE=employee_application
ENV MYSQL_PASSWORD=govardhan
ENV MYSQL_ROOT_PASSWORD=govardhan

COPY dbtablesv1/ /docker-entrypoint-initdb.d/
EXPOSE 3306
CMD ["mysqld"]
