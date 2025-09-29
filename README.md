# Simple IoT Gateway

## 项目概述
这是一个简单的 IoT 网关服务器，用于处理来自客户端的请求，并随机生成响应。该服务器使用 Python 的 socket 编程创建，能够同时处理多个客户端连接。也是一个胡说八道生成器:)

## 功能简介
- 监听客户端请求。
- 随机使用 `fortune` 命令与 `ponysay` 或 `pokemonsay` 生成幽默响应。
- 支持多线程处理，实现同时处理多个客户端。

## 环境要求
- Python 3.8+
- 安装必要的库
  
## RDK安装依赖
- 确保您在RDK中安装了fortune; ponysay; 以及pokemonsay
  - Fortune的安装
  
```bash

```
  - Ponysay的安装

```bash
sudo apt install snapd
sudo snap install ponysay
```
  - Pokemonsay的安装
  
```bash
pip install -r requirements.txt
```

## 安装依赖
首先，确保您在环境中安装了 Python 3。然后，您可以使用以下命令安装必要的依赖：

```bash
pip install -r requirements.txt


