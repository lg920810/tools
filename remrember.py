# 输入法两个图标的时候删除一个
sudo apt-get remove fcitx-ui-qimpanel

# cv中的颜色格式存储为bgr，但其他软件都有rgb，所以cv和Qt这样的软件交互时，要转成rgb
img_show = cv2.cvtColor(CAMImg, cv2.COLOR_BGR2RGB)

# pytroch cpu版本 
pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp35-cp35m-linux_x86_64.whl

# 离线安装，忽略依赖
pip install tensorflow --no-deps
# 清空swap
swapoff -a && swapon -a

# 远程免密登录 
ssh-keygen -t rsa
scp ~/.ssh/id_rsa.pub root@14.116.177.62:/root/.ssh/authorized_keys

# 远程服务器
ssh root@14.116.177.62     ssh -L 16006:127.0.0.1:6006 root@14.116.177.62

ssh root@10.8.33.13
xZsnerly#0

ssh root@10.8.33.14
ECCWIAZO#0

ssh root@10.8.33.15
pLuHJPEU#0

# 别人家的服务器
ssh root@14.166.177.64
qMPcHbV3#0

# 组内服务器
192.168.8.64

# scp远程到本地
scp -r root@14.116.177.62:/root/.torch/models/ /home/legal/.torch/models/

# sliver密码
5HkMNAvei2kI0TO

# 安装tk
sudo apt-get install python3-tk

# 查看正在运行的python进程路径
ps -aux|grep python

# 查看文件大小
du -h --max-depth=0

# 查看文件个数
ls -l | grep "^-" | wc -l

# keras 强制使用CPU
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"  

# 查看显卡上的进程
fuser -v /dev/nvidia*

export WORKON_HOME=~/Envs
source /home/legal/.local/bin/virtualenvwrapper.sh

https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels.h5

https://s3.amazonaws.com/img-datasets/mnist.npz

# 服务器挂载硬盘方法
1、service portmap start    #先启动portmap
2、showmount -e 100.68.84.4 #检查nfs服务器端是否有目录共享
3、mkdir /data  #创建本地挂载路径
4、mount -t nfs 100.68.84.4:/csp_efs_15182_id015182_vol1014_prd /data -o rw,soft,intr,rsize=32768,wsize=32768,tcp,timeo=300  #挂载硬盘到本地路径
5、mount -l # 查看是否挂载成功


# cuda的版本信息
cat  /usr/local/cuda/version.txt 

同理，cudnn的信息在其头文件里

cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2  即可查询












