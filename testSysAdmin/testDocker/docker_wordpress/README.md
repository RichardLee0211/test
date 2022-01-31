from: https://docs.docker.com/samples/wordpress/

```docker-compose.yml
version: "3.9"

services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    volumes:
      - wordpress_data:/var/www/html
    ports:
      - "8000:80"
    restart: always
    enrironment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
volumes:
  db_data: {}
  wordpress_data: {}

```

```shell
## open docker for mac Desktop app
docker-compose up -d  # it does spin up every quickly
docker container ls # get containerID
docker exec -it <wordexpressContainerID> bash
docker volume ls       # get the volume name
docker volume inspect <volumeName>

(base) ➜  docker_wordpress docker volume inspect docker_wordpress_wordpress_data
[
    {
        "CreatedAt": "2021-11-05T14:24:24Z",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.project": "docker_wordpress",
            "com.docker.compose.version": "1.29.2",
            "com.docker.compose.volume": "wordpress_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/docker_wordpress_wordpress_data/_data",
        "Name": "docker_wordpress_wordpress_data",
        "Options": null,
        "Scope": "local"
    }
]
```

does not have this directory??
  "Mountpoint": "/var/lib/docker/volumes/docker_wordpress_wordpress_data/_data",


### try it on Linux@lab machine
#### install docker-compose in Linux
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

I can find the /var/lib/docker diretionary
but need be root to edit it

put the volume within my home directory
docker container inspect <containerID>   # for mounting point
docker container stop <containerID>
docker container rm -f <containerID>
docker volume prune   # rm previous volume directory from HOST
docker-composer up -d # spin up containers again

mkdir ./wordpress_data  ./db_data
then use this in docker-compose.yml
    volumes:
      - ./db_data:/var/lib/mysql
    volumes:
      - ./wordpress_data:/var/www/html

DONE: how to back up da_data and wordpress_data
use Borg

#### something about wordpress

html is not raw reading friendly

wp-admin/install.php
wordpress_data/wp-config-sample.php

TODO: how to post WP post within markdown

- edit via web GUI
- block widgets
-
