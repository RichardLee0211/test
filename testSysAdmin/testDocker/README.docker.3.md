20220509
--------------------------------------------------------------------------------

reinstall vislab machine to Ubuntu 22.04 in order to use docker GPUs environment

from: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
Using the PyTorch NGC Container requires the host system to have the following installed:
- Docker Engine
- NVIDIA GPU Drivers
- NVIDIA Container Toolkit

```shell
    7  ubuntu-drivers devices
    8  sudo ubuntu-drivers autoinstall
    9  sudo reboot

   26  sudo snap install docker   ## this worked

   34  sudo apt update
   35  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

   ## get docker desktop app
   44  sudo apt install ./docker-desktop-4.8.1-amd64.deb

   56  distribution=$(. /etc/os-release;echo $ID$VERSION_ID)       && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg       && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list |             sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |             sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
   57  sudo apt-get update
   58  sudo apt-get install -y nvidia-docker2
   59  sudo systemctl restart docker
   60  sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
   61  sudo docker run --gpus all -it --rm nvcr.io/nvidia/pytorch:22.01-py3
```


####
install kubectl for using kubernetes cluster in Docker

from: https://linuxconfig.org/how-to-install-kubernetes-on-ubuntu-22-04-jammy-jellyfish-linux

sudo apt install apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt install kubeadm kubelet kubectl kubernetes-cni

kubectl config get-contexts
kubectl get nodes


kubernetes-master:~$ kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
kubernetes-master:~$ kubectl run --image=nginx nginx-server --port=80 --env="DOMAIN=cluster"
kubernetes-master:~$ kubectl expose deployment nginx-deployment --port=80 --name=nginx-http

kubectl get svc
