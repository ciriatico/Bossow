# Use the official MySQL image
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=senhabossow
ENV MYSQL_DATABASE=bossow

# Copy the SQL files and images into the container
COPY 01-init.sql /docker-entrypoint-initdb.d/
COPY 02-data_insertion.sql /docker-entrypoint-initdb.d/
COPY images/ /var/lib/mysql-files/

# Grant the required permissions to the files
RUN chmod -R 644 /var/lib/mysql-files/*

# Expose MySQL port
EXPOSE 3306
