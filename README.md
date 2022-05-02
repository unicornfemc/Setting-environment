# Setting-environment
##目的：
局域网内通过本地PC配置VSCODE，通过Python连接威联通NAS数据库

##环境：
1.安装VScode
2.安装annaconda3,增加stockEn环境(python3.10),在stockEn环境下
3.conda切换环境
anaconda prompt下切换到stockEn环境
conda activate stockEn
4.安装金融库
pip install tushare
pip install baostock

##Nas安装数据库
1.威联通Nas安装MariaDB phpMyAdmin
2.VScode插件 SQLtool 连接 威联通Nas安装MariaDB

##连接测试
1.运行baostock测试程序,下载数据到本地
2.运行tushare测试程序
3.连接数据库下载测试
4.连接数据库上传测试



