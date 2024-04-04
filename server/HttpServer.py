import logging
import traceback

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from server import ChatHistory

log = logging.getLogger(__name__)

app = FastAPI()
accessKey= "kawika-git/wechatSDK"

@app.get('/')
def index():
    return "Hello World"

@app.post('/historyMsgData')
async def hismsg(request: Request):
    req_json = await request.json()
    if req_json is None or 'userName' not in req_json:
        return {"code": 1001, "data": {"result": []}}
    # 验证accessKey 用于部署在服务器端被恶意请求
    if 'accessKey' not in req_json or req_json['accessKey'] != accessKey:
        return {"code": 1001, "data": {"result": []}}
    userName = req_json['userName']
    resData = ChatHistory.getFinHistory(userName, f".startTime_{userName}.txt")
    return {"code": "0", "data": {"result": resData}}


# 定义全局异常处理器
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    # 获取异常的堆栈信息
    exc_info = traceback.format_exc()
    # 记录错误日志
    logging.error(f"Unhandled Exception: {type(exc).__name__}: {exc}\n{exc_info}")
    # 返回错误响应
    return JSONResponse(status_code=500, content={"message": f"An error occurred: {exc}"})


def runHttpServer():
    host = "0.0.0.0"
    port = 18000
    uvicorn.run(app, host=host, port=port)
