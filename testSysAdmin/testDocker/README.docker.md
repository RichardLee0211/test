docker run --name repo alpine/git clone \
  https://github.com/docker/getting-started.git
docker cp repo:/git/getting-started/ .       # so easy to copy files to host OS

cd getting-started
docker build -t docker101tutorial .

docker run -d -p 80:80 \
  --name docker-tutorial docker101tutorial

docker tage docker101tutorial richardlee0211/docker101tutorial
docker push richardlee0211/docker101tutorial

from: http://localhost/tutorial/our-application/
------

```Dockerfile
	FROM node:12-alpine
	RUN apk add --no-cache python g++ make
	WORKDIR /app
	COPY . .
	RUN yarn install --production
	CMD ["node", "src/index.js"]
```

docker build -t getting-started .

docker run -dp 3000:3000 getting-started

docker ps
docker ps -a

http://localhost:3000

docker stop <containerID>
docker rm <containerID>
# or do it as one step
# docker rm -f <containerID>

docker image ls

docker login -u richardlee0211  # weird, build-in login module in this tool

docker tag getting-started richardlee0211/getting-started

```shell
	(base) ➜  app docker image ls
	REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
	getting-started                    latest    a2d03742f804   14 minutes ago   383MB
	richardlee0211/getting-started     latest    a2d03742f804   14 minutes ago   383MB
	...
	# two repository names, the same image ID
```

docker push richardlee0211/getting-started

# on the remote machine, docker would download the image first
docker run -dp 3000:3000 richardlee0211/getting-started

### persisting our DB

docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"
# the second command only to keep this container running

docker exec <containerID> cat /data.txt

docker image ls # for repositories existing in the harddrive
docker ps       # for container/prosess now running
docker rm -f <containerID>   # for container

```shell
	[node1] (local) root@192.168.0.13 ~
	$ docker image ls
	REPOSITORY                       TAG       IMAGE ID       CREATED          SIZE
	richardlee0211/getting-started   latest    a2d03742f804   45 minutes ago   383MB
	ubuntu                           latest    c29284518f49   6 days ago       72.8MB
	[node1] (local) root@192.168.0.13 ~
	$ docker run -it ubuntu ls /
	bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
	boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
```

docker volume create todo-db
docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started

docker volume inspect todo-db
```shell
	(base) ➜  app docker volume inspect todo-db

	[
			{
					"CreatedAt": "2021-07-20T01:27:00Z",
					"Driver": "local",
					"Labels": {},
					"Mountpoint": "/var/lib/docker/volumes/todo-db/_data",
					"Name": "todo-db",
					"Options": {},
					"Scope": "local"
			}
	]
```

### using bind mounts
docker run -dp 3000:3000 \
    -w /app -v "$(pwd):/app" \
    node:12-alpine \
    sh -c "yarn install && yarn run dev"

docker logs -f <containerID>

### multi-container apps
```shell
	docker network create todo-app

	docker run -d \
			--network todo-app --network-alias mysql \
			-v todo-mysql-data:/var/lib/mysql \
			-e MYSQL_ROOT_PASSWORD=secret \
			-e MYSQL_DATABASE=todos \
			mysql:5.7

	docker exec -it 413a6101347a mysql -p

	docker run -it --network todo-app nicolaka/netshoot
# read the article for review

	docker run -dp 3000:3000 \
		-w /app -v "$(pwd):/app" \
		--network todo-app \
		-e MYSQL_HOST=mysql \
		-e MYSQL_USER=root \
		-e MYSQL_PASSWORD=secret \
		-e MYSQL_DB=todos \
		node:12-alpine \
		sh -c "yarn install && yarn run dev"
```

###using docker compose
docker-compose version

```docker-compose.yml
version: "3.7"

services:
  app:
    image: node:12-alpine
    command: sh -c "yarn install && yarn run dev"
    ports:
      - 3000:3000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos

  mysql:
    image: mysql:5.7
    volumes:
      - todo-mysql-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: todos

volumes:
  todo-mysql-data:
```

docker-compose up -d
docker-compose down

intro to microservices, Docker, and Kubernetes
--------------------------------------------------------------------------------
from: https://www.youtube.com/watch?v=1xo-0gCVhTU&ab_channel=JamesQuigley

docker ps
docker kill <containerID>

minikube start
kubectl get pods
kubectl get deployments
minikube dashboard

deployment.yml
kubectl create -f deployment.yml
kubectl get pods
kubectl ip

How to get started with Docker
--------------------------------------------------------------------------------
from: https://www.youtube.com/watch?v=iqqDU2crIEQ&t=30s&ab_channel=Docker

need to lauch docker deamon by lauch the GUI docker app in MacOS
```Dockerfile
	FROM node:12.16.3
	WORKDIR /code
	ENV PORT 80
	COPY package.json /code/package.json
	RUN npm install
	COPY . /code
	CMD [ "node", "src/server.js" ]

```

docker build --tag hello-world .
docker images
docker run hello-world
docker ps
docker ps -a
docker start <NAME>
docker stop <NAME>
docker rm <NAME>
docker run -p 8080:80 --name hello -d hello-world
docker logs hello

dockerhub.com

docker tag hello-world pmckee/hello-world
docker push pmckee/hello-world
docker rmi pmckee/hello-world
docker pull pmckee/hello-world

```docker-compose.yml
version: '2'
services:
	web:
			build:
				context:
				dockerfile: Dockerfile
			container_name: web
			ports:
				- "8080:80"

	db:
		image: mongo:3.6.1
		container_name: db
		volumes:
			- mongodb:/data/db
			- mongodb_config:/data/configdb
		ports:
			- 27017:27017
		command: mongod

	volumes:
		mongodb:
		mongodb_config:
```

docker-compose up -d
docker-compose down

Containers From Scratch.Liz Rice, GOTO 2018
--------------------------------------------------------------------------------
from: https://www.youtube.com/watch?v=8fi7uSYlOdc&ab_channel=GOTOConferences

hostname <newHostName>



learning.edx.org
================================================================================
from: https://learning.edx.org/course/course-v1:RedHat+DO081x+2T2017/block-v1:RedHat+DO081x+2T2017+type@sequential+block@a9a30e15abc9490aaa821ce2df1becc0/block-v1:RedHat+DO081x+2T2017+type@vertical+block@6d32f4cba2144e58b9d93045c6286e05

something
---------------------

install minishift on macOS:
https://access.redhat.com/documentation/en-us/red_hat_container_development_kit/3.9/html-single/getting_started_guide/index#installing-minishift
CDK: container development environment
first start log
```shell
	➜  _openshift ./minishift start --vm-driver=virtualbox
	-- Starting profile 'minishift'
	-- Check if deprecated options are used ... OK
	-- Checking if https://mirror.openshift.com is reachable ... OK
	-- Checking if requested OpenShift version 'v3.11.346' is valid ... OK
	-- Checking if requested OpenShift version 'v3.11.346' is supported ... OK
	-- Checking if requested hypervisor 'virtualbox' is supported on this platform ... OK
	-- Checking if VirtualBox is installed ... OK
	-- Checking the ISO URL ... OK
	-- Checking if provided oc flags are supported ... OK
	-- Starting the OpenShift cluster using 'virtualbox' hypervisor ...
	-- Minishift VM will be configured with ...
		 Memory:    4 GB
		 vCPUs :    2
		 Disk size: 20 GB
	-- Starting Minishift VM ................................ OK
	-- Registering machine using subscription-manager
		 Login to registry.redhat.io in progress . FAIL
		 Registration in progress .......... OK [20s]
	-- Checking for IP address ... OK
	-- Checking for nameservers ... OK
	-- Checking if external host is reachable from the Minishift VM ...
		 Pinging 8.8.8.8 ... OK
	-- Checking HTTP connectivity from the VM ...
		 Retrieving http://minishift.io/index.html ... FAIL
		 VM cannot connect to external URL with HTTP
	-- Checking if persistent storage volume is mounted ... OK
	-- Checking available disk space ... 1% used OK
	-- Writing current configuration for static assignment of IP address ... OK
		 Importing 'registry.access.redhat.com/openshift3/ose-control-plane:v3.11.346' . CACHE MISS
		 Importing 'registry.access.redhat.com/openshift3/ose-docker-registry:v3.11.346' . CACHE MISS
		 Importing 'registry.access.redhat.com/openshift3/ose-haproxy-router:v3.11.346' . CACHE MISS
	-- OpenShift cluster will be configured with ...
		 Version: v3.11.346
	-- Pulling the OpenShift Container Image .............. OK
	-- Copying oc binary from the OpenShift container image to VM ... OK
	-- Starting OpenShift cluster ........................................................
	Getting a Docker client ...
	Checking if image registry.access.redhat.com/openshift3/ose-control-plane:v3.11.346 is available ...
	Pulling image registry.access.redhat.com/openshift3/ose-cli:v3.11.346
	Image pull complete
	Pulling image registry.access.redhat.com/openshift3/ose-node:v3.11.346
	Pulled 6/7 layers, 91% complete
	Pulled 7/7 layers, 100% complete
	Extracting
	Image pull complete
	Checking type of volume mount ...
	Determining server IP ...
	Using public hostname IP 192.168.99.101 as the host IP
	Checking if OpenShift is already running ...
	Checking for supported Docker version (=>1.22) ...
	Checking if insecured registry is configured properly in Docker ...
	Checking if required ports are available ...
	Checking if OpenShift client is configured properly ...
	Checking if image registry.access.redhat.com/openshift3/ose-control-plane:v3.11.346 is available ...
	Starting OpenShift using registry.access.redhat.com/openshift3/ose-control-plane:v3.11.346 ...
	I0906 14:21:20.748166    2790 config.go:40] Running "create-master-config"
	I0906 14:21:23.475715    2790 config.go:46] Running "create-node-config"
	I0906 14:21:24.491726    2790 flags.go:30] Running "create-kubelet-flags"
	I0906 14:21:24.866918    2790 run_kubelet.go:49] Running "start-kubelet"
	I0906 14:21:25.039497    2790 run_self_hosted.go:181] Waiting for the kube-apiserver to be ready ...
	I0906 14:22:04.056797    2790 interface.go:26] Installing "kube-proxy" ...
	I0906 14:22:04.057775    2790 interface.go:26] Installing "kube-dns" ...
	I0906 14:22:04.057784    2790 interface.go:26] Installing "openshift-service-cert-signer-operator" ...
	I0906 14:22:04.057788    2790 interface.go:26] Installing "openshift-apiserver" ...
	I0906 14:22:04.057816    2790 apply_template.go:81] Installing "openshift-apiserver"
	I0906 14:22:04.058470    2790 apply_template.go:81] Installing "kube-proxy"
	I0906 14:22:04.060145    2790 apply_template.go:81] Installing "kube-dns"
	I0906 14:22:04.060318    2790 apply_template.go:81] Installing "openshift-service-cert-signer-operator"
	I0906 14:22:09.753730    2790 interface.go:41] Finished installing "kube-proxy" "kube-dns" "openshift-service-cert-signer-operator" "openshift-apiserver"
	I0906 14:24:09.836415    2790 run_self_hosted.go:242] openshift-apiserver available
	I0906 14:24:09.837449    2790 interface.go:26] Installing "openshift-controller-manager" ...
	I0906 14:24:09.837483    2790 apply_template.go:81] Installing "openshift-controller-manager"
	I0906 14:24:12.545253    2790 interface.go:41] Finished installing "openshift-controller-manager"
	Adding default OAuthClient redirect URIs ...
	Adding rhel-imagestreams ...
	Adding persistent-volumes ...
	Adding web-console ...
	Adding registry ...
	Adding router ...
	Adding sample-templates ...
	I0906 14:24:12.562876    2790 interface.go:26] Installing "rhel-imagestreams" ...
	I0906 14:24:12.562886    2790 interface.go:26] Installing "persistent-volumes" ...
	I0906 14:24:12.562893    2790 interface.go:26] Installing "openshift-web-console-operator" ...
	I0906 14:24:12.562897    2790 interface.go:26] Installing "openshift-image-registry" ...
	I0906 14:24:12.562901    2790 interface.go:26] Installing "openshift-router" ...
	I0906 14:24:12.562905    2790 interface.go:26] Installing "sample-templates" ...
	I0906 14:24:12.562960    2790 interface.go:26] Installing "sample-templates/dancer quickstart" ...
	I0906 14:24:12.562967    2790 interface.go:26] Installing "sample-templates/sample pipeline" ...
	I0906 14:24:12.562971    2790 interface.go:26] Installing "sample-templates/mongodb" ...
	I0906 14:24:12.562975    2790 interface.go:26] Installing "sample-templates/mysql" ...
	I0906 14:24:12.562981    2790 interface.go:26] Installing "sample-templates/postgresql" ...
	I0906 14:24:12.562985    2790 interface.go:26] Installing "sample-templates/cakephp quickstart" ...
	I0906 14:24:12.562989    2790 interface.go:26] Installing "sample-templates/jenkins pipeline ephemeral" ...
	I0906 14:24:12.562993    2790 interface.go:26] Installing "sample-templates/mariadb" ...
	I0906 14:24:12.562997    2790 interface.go:26] Installing "sample-templates/django quickstart" ...
	I0906 14:24:12.563002    2790 interface.go:26] Installing "sample-templates/nodejs quickstart" ...
	I0906 14:24:12.563006    2790 interface.go:26] Installing "sample-templates/rails quickstart" ...
	I0906 14:24:12.563057    2790 apply_list.go:67] Installing "sample-templates/rails quickstart"
	I0906 14:24:12.563925    2790 create_secret.go:82] Installing "imagestreamsecret"
	I0906 14:24:12.564725    2790 apply_template.go:81] Installing "openshift-web-console-operator"
	I0906 14:24:12.565522    2790 apply_list.go:67] Installing "sample-templates/dancer quickstart"
	I0906 14:24:12.565695    2790 apply_list.go:67] Installing "sample-templates/sample pipeline"
	I0906 14:24:12.565786    2790 apply_list.go:67] Installing "sample-templates/mongodb"
	I0906 14:24:12.565874    2790 apply_list.go:67] Installing "sample-templates/mysql"
	I0906 14:24:12.565957    2790 apply_list.go:67] Installing "sample-templates/postgresql"
	I0906 14:24:12.566039    2790 apply_list.go:67] Installing "sample-templates/cakephp quickstart"
	I0906 14:24:12.566184    2790 apply_list.go:67] Installing "sample-templates/jenkins pipeline ephemeral"
	I0906 14:24:12.566268    2790 apply_list.go:67] Installing "sample-templates/mariadb"
	I0906 14:24:12.566345    2790 apply_list.go:67] Installing "sample-templates/django quickstart"
	I0906 14:24:12.566443    2790 apply_list.go:67] Installing "sample-templates/nodejs quickstart"
	I0906 14:24:25.083143    2790 apply_list.go:67] Installing "rhel-imagestreams"
	I0906 14:24:25.857358    2790 interface.go:41] Finished installing "sample-templates/dancer quickstart" "sample-templates/sample pipeline" "sample-templates/mongodb" "sample-templates/mysql" "sample-templates/postgresql" "sample-templates/cakephp quickstart" "sample-templates/jenkins pipeline ephemeral" "sample-templates/mariadb" "sample-templates/django quickstart" "sample-templates/nodejs quickstart" "sample-templates/rails quickstart"
	I0906 14:25:01.024948    2790 interface.go:41] Finished installing "rhel-imagestreams" "persistent-volumes" "openshift-web-console-operator" "openshift-image-registry" "openshift-router" "sample-templates"
	Login to server ...
	Creating initial project "myproject" ...
	Server Information ...
	OpenShift server started.

	The server is accessible via web console at:
			https://192.168.99.101:8443/console

	You are logged in as:
			User:     developer
			Password: <any value>

	To login as administrator:
			oc login -u system:admin


	-- Applying addon 'xpaas':..
	XPaaS imagestream and templates for OpenShift installed
	See https://github.com/openshift/openshift-ansible/tree/release-3.11/roles/openshift_examples/files/examples
	-- Applying addon 'admin-user':..
	-- Applying addon 'anyuid':.
	 Add-on 'anyuid' changed the default security context constraints to allow pods to run as any user.
	 Per default OpenShift runs containers using an arbitrarily assigned user ID.
	 Refer to https://docs.okd.io/latest/architecture/additional_concepts/authorization.html#security-context-constraints and
	 https://docs.okd.io/latest/creating_images/guidelines.html#openshift-origin-specific-guidelines for more information.
	-- Exporting of OpenShift images is occuring in background process with pid 46849.
```

some concepts: docker pods kubenet and openshift

minishift setup-cdk
minishift status
minishift config view

echo $MINISHIFT_USERNAME # check runtime environment set up
minishift start
oc version
oc login -u system:admin
oc get pods -n default
minishift ssh
docker ps | grep openshift   # inside the minishift VM
exit
minishift stop

inside minishift ssh, I can run docker command

docker run --name mysql-basic \
 -e MYSQL_USER=user1 -e MYSQL_PASSWORD=mypa55 \
 -e MYSQL_DATABASE=items -e MYSQL_ROOT_PASSWORD=r00tpa55 \
 -d mysql:5.6

docker pull mysql
docker images

docker run --name mysql-custom \
  -e MYSQL_USER=redhat -e MYSQL_PASSWORD=r3dh4t \
  -d mysql:5.5


docker run --name demo-container-02 -d rhel7.3 dd if=/dev/zero of=/dev/null
docker run --name demo-container-04 -it rhel7.3 /bin/bash
docker stop demo-container-04
docker rm demo-container-04

docker run --name demo-container -d rhscl/httpd-24-rhel7
docker inspect -f '{{ .NetworkSetting.IPAddress }}' demo-1-httpd
docker exec -it demo-1-httpd /bin/bash
docker rm $(docker ps -aq)

[docker@minishift ~]$ docker inspect -f '{{ .NetworkSettings.IPAddress }}' mysql-2nd
172.17.0.10

docker iamge registries: place to share Docker images
- docker.io
- registry.access.redhat.com

docker save -o mysql.tar registry.access.redhat.com/rhscl/mysql-56-rhel7
docker load -i mysql.tar
docker tag nginx nginx
docker push nginx
docker rmi $(docker images -q)

docker diff mysql-basic
docker commit mysql-basic mysql-custom

docker run -d --name official-httpd -p 8180:80 centos/httpd
docker exec -it official-httpd /bin/hash
# change some files
docker stop official-httpd
docker commit -a 'author name' -m 'changed some file' official-httpd
docker images
docker tag 05b78342c586 do180/custom-httpd
docker tage do180/custom-httpd infrastrure.lab.example.com:5000/do180/custom-httpd:v1.0
docker push infrastrue.lab.example.com:5000/do180/custom-httpd:v1.0
docker-registry-clki infrastructure.lab.example.com:5000 search custom-httpd

DONE:
/usr/bin/docker-current: read /etc/containers/policy.json: input/output error.
reinstalled the minishift

### creating custom containers

```Dockerfile
	# This is a comment line
	FROM rhel7.3
	LABEL description="This is a custom httpd container image"
	MAINTAINER John Doe <jdoe@xyz.com>
	RUN yum install -y httpd
	EXPOSE 80
	ENV LogLevel "info"
	ADD http://someserver.com/filename.pdf /var/www/html
	COPY ./src/ /var/www/html/
	USER apache
	ENTRYPOINT ["/usr/sbin/httpd"]
	CMD ["-D", "FOREGROUND"]
```

```Dockerfile02
	FROM rhel7.3

	MAINTAINER Your Name <youremail>
	LABEL description="A basic Apache HTTP server container on RHEL 7"

	RUN yum -y update && \
			yum install -y httpd && \
			yum clean all

	EXPOSE 80

	ENTRYPOINT ["httpd"]
	CMD  ["-D", "FOREGROUND"]
```

```shell
	docker build -t do081x/httpd2 httpd-image
	docker images | grep -v openshift
	docker run --name my-httpd \
			-d -p 10080:80 do081x/httpd2
	docker ps | grep -v openshift
	curl 127.0.0.1:10080 | grep 'Test Page'
	docker stop my-httpd
	docker rm my-httpd
	docker rmi do081x/httpd2
	exit
```

oc login -u developer -p developer
oc new-project database
oc new-app --name=mysql \
    --docker-image=registry.access.redhat.com/rhscl/mysql-56-rhel7 \
    -e MYSQL_USER=user1 -e MYSQL_PASSWORD=mypa55 -e MYSQL_DATABASE=testdb \
    -e MYSQL_ROOT_PASSWORD=r00tpa55
oc status
oc get pods
oc describe pod mysql-1-wgbjs
oc get svc
oc describe svc mysql   # describe service
oc describe dc mysql    # deployment configuration
oc rsh mysql-1-d0jr9
oc delete project database

```shell
	➜  _openshift $oc new-app --name=mysql \
			--docker-image=registry.access.redhat.com/rhscl/mysql-56-rhel7 \
			-e MYSQL_USER=user1 -e MYSQL_PASSWORD=mypa55 -e MYSQL_DATABASE=testdb \
			-e MYSQL_ROOT_PASSWORD=r00tpa55

	--> Found Docker image 63d6bb0 (3 years old) from registry.access.redhat.com for "registry.access.redhat.com/rhscl/mysql-56-rhel7"

			MySQL 5.6
			---------
			MySQL is a multi-user, multi-threaded SQL database server. The container image provides a containerized packaging of the MySQL mysqld daemon and client application. The mysqld server daemon accepts connections from clients and provides access to content from MySQL databases on behalf of the clients.

			Tags: database, mysql, mysql56, rh-mysql56

			* An image stream tag will be created as "mysql:latest" that will track this image
			* This image will be deployed in deployment config "mysql"
			* Port 3306/tcp will be load balanced by service "mysql"
				* Other containers can access this service through the hostname "mysql"
			* This image declares volumes and will default to use non-persistent, host-local storage.
				You can add persistent volumes later by running 'volume dc/mysql --add ...'

	--> Creating resources ...
			imagestream.image.openshift.io "mysql" created
			deploymentconfig.apps.openshift.io "mysql" created
			service "mysql" created
	--> Success
			Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
			 'oc expose svc/mysql'
			Run 'oc status' to view your app.
	➜  _openshift $oc status
	In project database on server https://192.168.99.101:8443

	svc/mysql - 172.30.182.250:3306
		dc/mysql deploys istag/mysql:latest
			deployment #1 deployed about a minute ago - 1 pod


	2 infos identified, use 'oc status --suggest' to see details.
```

```shell
	➜  _openshift $oc describe pod mysql-1-wgbjs
	Name:               mysql-1-wgbjs
	Namespace:          database
	Priority:           0
	PriorityClassName:  <none>
	Node:               localhost/10.0.2.15
	Start Time:         Mon, 06 Sep 2021 15:21:52 -0400
	Labels:             app=mysql
											deployment=mysql-1
											deploymentconfig=mysql
	Annotations:        openshift.io/deployment-config.latest-version=1
											openshift.io/deployment-config.name=mysql
											openshift.io/deployment.name=mysql-1
											openshift.io/generated-by=OpenShiftNewApp
											openshift.io/scc=anyuid
	Status:             Running
	IP:                 172.17.0.10
	Controlled By:      ReplicationController/mysql-1
	Containers:
		mysql:
			Container ID:   docker://e89a678421f5e0132cb4f74aadca7f7be42a21f232b6622700f30efd90433c40
			Image:          registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:2c5483929f95892100c2f8ff45ee405cea0ca2380ddce2cbf5409e9c5240204f
			Image ID:       docker-pullable://registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:2c5483929f95892100c2f8ff45ee405cea0ca2380ddce2cbf5409e9c5240204f
			Port:           3306/TCP
			Host Port:      0/TCP
			State:          Running
				Started:      Mon, 06 Sep 2021 15:22:07 -0400
			Ready:          True
			Restart Count:  0
			Environment:
				MYSQL_DATABASE:       testdb
				MYSQL_PASSWORD:       mypa55
				MYSQL_ROOT_PASSWORD:  r00tpa55
				MYSQL_USER:           user1
			Mounts:
				/var/lib/mysql/data from mysql-volume-1 (rw)
				/var/run/secrets/kubernetes.io/serviceaccount from default-token-8cwpc (ro)
	Conditions:
		Type              Status
		Initialized       True
		Ready             True
		ContainersReady   True
		PodScheduled      True
	Volumes:
		mysql-volume-1:
			Type:    EmptyDir (a temporary directory that shares a pod's lifetime)
			Medium:
		default-token-8cwpc:
			Type:        Secret (a volume populated by a Secret)
			SecretName:  default-token-8cwpc
			Optional:    false
	QoS Class:       BestEffort
	Node-Selectors:  <none>
	Tolerations:     <none>
	Events:
		Type    Reason     Age   From                Message
		----    ------     ----  ----                -------
		Normal  Scheduled  3m    default-scheduler   Successfully assigned database/mysql-1-wgbjs to localhost
		Normal  Pulling    3m    kubelet, localhost  pulling image "registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:2c5483929f95892100c2f8ff45ee405cea0ca2380ddce2cbf5409e9c5240204f"
		Normal  Pulled     2m    kubelet, localhost  Successfully pulled image "registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:2c5483929f95892100c2f8ff45ee405cea0ca2380ddce2cbf5409e9c5240204f"
		Normal  Created    2m    kubelet, localhost  Created container
		Normal  Started    2m    kubelet, localhost  Started container
```

```shell
	➜  _openshift $oc export svc mysql > mysql-svc.yml
	Command "export" is deprecated, use the oc get --export
	➜  _openshift ls
	minishift                 mysql-svc.yml             openshift.local.clusterup
	➜  _openshift more mysql-svc.yml
	apiVersion: v1
	kind: Service
	metadata:
		annotations:
			openshift.io/generated-by: OpenShiftNewApp
		creationTimestamp: null
		labels:
			app: mysql
		name: mysql
	spec:
		ports:
		- name: 3306-tcp
			port: 3306
			protocol: TCP
			targetPort: 3306
		selector:
			app: mysql
			deploymentconfig: mysql
		sessionAffinity: None
		type: ClusterIP
	status:
		loadBalancer: {}
```


Manage Docker as a non-root user
--------------------------------------------------------------------------------
from: https://docs.docker.com/engine/install/linux-postinstall/
```shell
sudo groupadd docker
sudo usermod -aG docker $USER
## logout and login or reboot the machine
newgrp docker    # login to a new group
groups           # comfirm $USER is in docker group
docker run hello-world
```

log
--------------------------------------------------------------------------------
nvidia -a
nvidia-container-cli -k -d /dev/tty info
dmesg               # print kernel ring buffer, device message ?

lshw -C display     # check GPU model

#### docker
docker image ls
docker ps -a
docker run -it --rm --gpus all ubuntu nvidia-smi        # access GPU power, !!
## mount current directory, using container environment
docker  run  -v `pwd`:`pwd` -w `pwd` -i -t  ubuntu bash
docker  run  -v /host/dir:/container/dir -w /container/dir -i -t  ubuntu bash
