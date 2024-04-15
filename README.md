# 聊天记录查询系统 🤖
Real-time Chat系统为开发者和研究者提供一种深入查看聊天内容的解决方案，允许用户在特定条件下获取特定群组或私聊的聊天记录，并通过我们提供的API进行控制。

### 核心特性：
- **聊天记录查询** - 在微信环境下，重现群组或个人聊天的内容
- **API访问** - 我们提供灵活且易用的RESTful API接口以方便开发者和研究者进行深度利用。
- **可扩展性设计** ： 未来可扩展的能力包括但不仅限于：
    - 允许未付费用户访问付费群的聊天记录以体验系统功能
    - 利用AI技术对聊天内容进行分析以追踪热门话题和动态。
    - 轻松将聊天内容上报至云端。


### 隐私政策及个人隐私：
- 高度重视用户隐私，严格遵守所有相关的隐私法律和规定，绝不会公开任何个人或敏感信息，一切聊天记录查询分析与展示都将在满足所有相关规定的前提下进行
用途限制：
- 本系统的初始设计意图是为了合法查询和研究工作，请遵守法律规定，严禁用于任何非法用途。每行代码，每个算法的创建都是为了推动聊天内容研究的发展及对社区的贡献。
- 项目的使用只供个人开发，绝不泄露任何信息，我们高度尊重每一位用户的隐私及源于此的数据。
- 总体来说，设计的核心是面向开发者友好的API接口和可扩展性，在秘密保护用户隐私及数据的同时，依然保证易用性和便利性

## 安装 🔧

### 微信启动

- [API启动器来源](https://wechatsdk.com)

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
--data-raw "{\"userName\":\"xxxxx@chatroom\",\"accessKey\":\"WeChatAPIs/wechatSDK\"}"
```
## 依赖 📦

项目依赖于 [wechatAPI](https://wechatsdk.com)。请确保安装所有必要的依赖。


## 如何贡献 🤝

欢迎通过Pull Requests来贡献代码。请确保您的代码符合项目的编码标准并通过所有测试。

## 效果展示 🖼️

![img.png](img%2Fimg.png)
![img.png](img%2Fimg_2.png)
![img.png](img%2Fimg_1.png)
