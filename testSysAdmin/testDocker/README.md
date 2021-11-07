NVIDIA Container Toolkit
================================================================================

arch Overview
--------------------------------------------------------------------------------
from: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/arch-overview.html

```shell
	├─ nvidia-docker2
	│    ├─ docker-ce (>= 18.06.0~ce~3-0~ubuntu)
	│    ├─ docker-ee (>= 18.06.0~ce~3-0~ubuntu)
	│    ├─ docker.io (>= 18.06.0)
	│    └─ nvidia-container-runtime (>= 3.3.0)

	├─ nvidia-container-runtime
	│    └─ nvidia-container-toolkit (<< 2.0.0)

	├─ nvidia-container-toolkit
	│    └─ libnvidia-container-tools (<< 2.0.0)

	├─ libnvidia-container-tools
	│    └─ libnvidia-container1 (>= 1.2.0~rc.3)
	└─ libnvidia-container1
```

install
--------------------------------------------------------------------------------
from: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#install-guide

#### platform requirements
- GNU/Linux x86_64 with kernel version > 3.10
uname -a
- Docker >= 19.03 (recommended, but some distributions may include older versions of Docker. The minimum supported version is 1.12)
docker --version
- NVIDIA GPU with Architecture >= Kepler (or compute capability 3.0)
look it up online
from: https://en.wikipedia.org/wiki/Volta_(microarchitecture)
- NVIDIA Linux drivers >= 418.81.07 (Note that older driver releases or branches are unsupported.)
nvidia-smi

#### setting up Docker

curl https://get.docker.com | sh \
  && sudo systemctl --now enable docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
  && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
  && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
sudo apt-get install -y nvidia-docker2

sudo systemctl restart docker

sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi


step 1: install containerd
--------------------------------------------------------------------------------

```shell
sudo modprobe overlay \
    && sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

sudo apt-get update \
    && sudo apt-get install -y containerd.io

sudo mkdir -p /etc/containerd \
    && sudo containerd config default | sudo tee /etc/containerd/config.toml


cat <<EOF > containerd-config.patch
--- config.toml.orig    2020-12-18 18:21:41.884984894 +0000
+++ /etc/containerd/config.toml 2020-12-18 18:23:38.137796223 +0000
@@ -94,6 +94,15 @@
        privileged_without_host_devices = false
        base_runtime_spec = ""
        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
+            SystemdCgroup = true
+       [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia]
+          privileged_without_host_devices = false
+          runtime_engine = ""
+          runtime_root = ""
+          runtime_type = "io.containerd.runc.v1"
+          [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia.options]
+            BinaryName = "/usr/bin/nvidia-container-runtime"
+            SystemdCgroup = true
    [plugins."io.containerd.grpc.v1.cri".cni]
    bin_dir = "/opt/cni/bin"
    conf_dir = "/etc/cni/net.d"
EOF

sudo systemctl restart containerd

sudo ctr image pull docker.io/library/hello-world:latest \
    && sudo ctr run --rm -t docker.io/library/hello-world:latest hello-world

```

step 2: install NVIDA Container Toolkit
--------------------------------------------------------------------------------

```shell
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
    && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
    && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update \
    && sudo apt-get install -y nvidia-container-runtime

sudo ctr image pull docker.io/nvidia/cuda:11.0-base
sudo ctr run --rm --gpus 0 -t docker.io/nvidia/cuda:11.0-base cuda-11.0-base nvidia-smi

```

install Podman
================================================================================
from: https://podman.io/getting-started/installation

. /etc/os-release
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/Release.key" | sudo apt-key add -
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install podman



Log
================================================================================

#### Using patch
diff -u working_slang.c latest_slang.c > slang.patch
patch -u -b working_slang.c -i slang.patch
