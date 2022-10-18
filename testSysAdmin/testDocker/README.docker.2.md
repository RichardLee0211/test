more on docker

from: https://project-awesome.org/veggiemonk/awesome-docker#where-to-start



Docker?!?! But I'm a SysAdmin
--------------------------------------------------------------------------------
from: https://www.youtube.com/watch?v=S3iKweF41Cc&ab_channel=Docker
good presentation

#### hello-world
from: https://training.play-with-docker.com/ops-s1-hello/
docker image pull alpine
docker image ls
docker container run alpine ls -al
docker container run -it alpine /bash/sh
docker container ls -a

docker container ls -a
docker container start <Container ID>
docker container ls
docker container exec <container ID> ls
docker image inspect alpine

#### security
from: https://training.play-with-docker.com/security-seccomp/
seccomp: firewall for system calls
docker info | grep seccomp
TODO: later

#### network

##### bridge network
```shell
    docker network ls
    # docker network inspect <network>
    docker network inspect bridge

    apt install bridge-utils
    brctl show
    ip a

    docker run -dt ubuntu sleep infinity    # put it in docker0 bridge network by default
	# ...
    # docker netowkr inspect bridge
    #     "Containers": {
    #         "2602c823e8a7287ca2b54b55bd4fe309774f46e9659bc81e7a7e771ce4979a3b": {
    #             "Name": "lucid_kirch",
    #             "EndpointID": "8595f5864a816f73ba97d392612b14f6338a16c8d5304d7b3e7c35988e03ce5d",
    #             "MacAddress": "02:42:ac:11:00:02",
    #             "IPv4Address": "172.17.0.2/16",
    #             "IPv6Address": ""
    #         }
    #     },
	# ...
	ping -c5 172.17.0.2

	docker exec -it <containerID> /bin/bash
	apt update && apt install -y iputils-ping
	ping -c5 www.github.com
	exit

	docker stop <containerID>

	docker run --name web1 -d -p 8080:80 nginx   # -p <hostPort>:<containerID>
	docker ps
	curl localhost:8080

```

##### overlay networking
```shell

	## on manager node
	docker swarm init --advertise-addr $(hostname -i)
	docker node ls

	## on worker node
	## on another machine in the same network
	docker swarm join --token SWMTKN-1-61vj2k7xs4oiax59rfgcgtnnihmm4gyiykgeeyyi55aolp6ynw-2r4780zp5weyou1oaeq1i7t5z 127.0.1.1:2377

	## on manager node
	docker network create -d overlay overnet
	docker network ls
	docker inspect overnet

	docker serveice create  --name myservice \
		--network overnet \
		--replicas 2 \
		ubuntu sleep infinity
	docker service ls
	docker service ps myservice

	## now overnet is expand to worknode
	docker network ls
	docker network inspect overnet

	## on manager node
	docker ps
	docker exec -it <containerID> /bin/bash
	cat /etc/resolv.conf			# every container come with an embedded DNS server
	apt update && apt install iputils-ping
	ping myservice
	exit
	docker service rm myservice
	docker kill <containerID1> <constainerID2>
	docker swarm leave --force
	docker swarm leave --force		# on the worker node

```

### Orchestration
from: https://training.play-with-docker.com/orchestration-hol/

Docker Compose and Docker Swarm
# on node 1
docker run -dt ubuntu sleep infinity

docker swarm init --advertise-addr $(hostname -i)
docker swarm join-token worker    # to get the join command again

# on node 2 and 3
docker swarm join --token SWMTKN-1-5knxayma7cf11oj3zli9h0751pf02aekwzgdti0m7xlcfut95d-2y01ed0gokxob51njxupcwehd 192.168.0.18:2377

# on node 1
docker node ls
docker service create --name sleep-app ubuntu sleep infinity
docker service ls
docker service update --replicas 7 sleep-app      # scale on demande
docker service ps sleep-app

# drain a node and reschedule the containers
docker node ls  # on node 1
docker ps       # on every node to check the running containers

docker node update --availability drain oe4vj7mvmdxpb3fkgmw2oxjgq # using <nodeID>, on node 1
docker node ls   # check node status
docker service ps sleep-app # check service status

docker service rm sleep-app
docker ps
docker kill <containerID>     # kill sleep container
docker swarm leave --force    # exit swarm on each node

### customize Docker image
from: https://training.play-with-docker.com/ops-s1-images/
```shell
    docker container run -it ubuntu bash
    ## change something inside the image
    apt update && apt install -y figlet
    figlet "hello docker"    # ascii font art
    exit
    ## save changes
    docker ps -a # get the containerID
    docker container diff <containerID>  # show to differece
    docker container commit <conatinerID>  # write to image
    docker image ls
    docker image tag <imageID> ourfiglet   # give it a tag
    docker container run ourgitlet figlet hello  # run the image
```

build image from Dockerfile
```index.js
    var os = require("os");
    var hostname = os.hostname();
    console.log("hello from " + hostname);
```

```Dockerfile
    FROM alpine
    RUN apk update && apk add nodejs
    COPY . /app
    WORKDIR /app
    CMD ["node","index.js"]
```

```shell
    docker image build -t hello:v0.1 .
    docker image ls
    docker container run hello:v0.1
    docker image history <imageID>

    ## make changes to code
    $ echo "console.log(\"this is v0.2\");" >> index.js
    $ docker image build -t hello:v0.2 .


    docker image pull alpine
    docker image inspect alpine
    docker image inspect --format "{{ json .RootFS.Layers }}" alpine
    docker image inspect --format "{{ json .RootFS.Layers }}" <imageID>   # three layers: OS, package install, our code
```

### Swarm intro

```shell
    docker swarm init --advertise-addr $(hostname -i)
    docker swarm join --token <token> <hostIP:port>  # on worker node
    docker node ls

    git clone https://github.com/docker/example-voting-app
    cd example-voting-app

    ## Tasks(container) -> Service -> Stack
    ## container -> Swarm Orchestrator
    docker stack deploy --compose-file=docker-stack.yml voting_stack
    docker stack ls                             # check stack status
    docker stack services voting_stack          # check services in stack
    docker service scale voting_stack_vote=5
```

### Application Containerization and Microservice Orchestration
from: https://training.play-with-docker.com/microservice-orchestration/

Docker compose

```shell
    git clone https://github.com/ibnesayeed/linkextractor.git
    cd linkextractor
    git checkout demo

    ## old way, run it but need to deal with packages and environment
    git checkout step0
    tree

    ## with Dockerfile
    git checkout step1
    tree
    docker image build -t linkextractor:step1 .
    docker image ls
    docker container run -it --rm linkextractor:step1 http://example.com/

    ## update python script
    git checkout step2
    tree
    docker image build -t linkextractor:step2 .
    docker image ls
    docker container run -it --rm linkextractor:step2 https://training.play-with-docker.com/

    ## link extractor API service, add main.py and make linkextractor a python module
    git checkout step3
    tree
    docker image build -t linkextractor:step3 .
    docker container run -d -p 5000:5000 --name=linkextractor linkextractor:step3
    docker container ls
    curl -i http://localhost:5000/api/http://example.com/
    docker container logs linkextractor
    docker container rm -f linkextractor


    ## Link Extractor API and Web Front End Services, add a new php web server
    git checkout step4
    tree
    docker-compose up -d --build
    docker container ls
    curl -i http://localhost:5000/api/http://example.com/
    docker-compose down

    ## step 5: Redis Service for Caching
    git checkout step5
    tree
    ## I stopped here
    ## aim to integrate docker to my development workflow
```

DevOps culture
