# 实时微信聊天记录查询系统 🤖

实时微信聊天记录查询系统是一个面向开发者和研究人员的工具，旨在提供一个实时监控和查询微信聊天内容的解决方案。通过本系统，用户可以实时获取特定微信群或私聊的聊天记录，并通过提供的API进行访问。

### 主要功能
- **实时聊天记录查询**：支持实时监控微信聊天内容，包括群聊和私聊。
- **API访问**：提供RESTful API接口，方便开发者和研究人员集成和使用。
- **可扩展性**：设计上考虑到未来可能的扩展，包括但不限于以下几点：
  - 将付费群的聊天记录公开展示，供未付费客户围观。
  - 利用AI技术分析聊天内容，总结热门话题和趋势。

## 安装 🔧

### 微信启动

- [API启动器来源](https://github.com/kawika-git/wechatAPI)

### 启动程序

1. 打开cmd，并进入 `WechatMsgHistory_real` 目录，运行 `python -m venv venv` 并开启虚拟环境 `venv/Scripts/activate`。
2. 运行 `pip install -r requirements.txt` 安装所有依赖。
3. 修改内容
    - 修改 `server/ChatHistory.py` 中的 `baseUrl` 字段为你的启动器的地址。
    - 修改 `server/HttpServer.py` 中的 `accessKey` 为你的接口秘钥。
4. 运行 `python httpMain.py` 启动服务。
5. 请求API
```
curl --location --request POST "http://127.0.0.1:18000/historyMsgData" ^
--header "Content-Type: application/json" ^
--data-raw "{\"userName\":\"xxxxx@chatroom\",\"accessKey\":\"kawika-git/wechatSDK\"}"
```
## 依赖 📦

项目依赖于 [wechatAPI](https://github.com/kawika-git/wechatAPI)。请确保安装所有必要的依赖。


## 如何贡献 🤝

欢迎通过Pull Requests来贡献代码。请确保您的代码符合项目的编码标准并通过所有测试。

## 效果展示 🖼️

![img.png](img%2Fimg.png)
![img.png](img%2Fimg_2.png)
![img.png](img%2Fimg_1.png)
