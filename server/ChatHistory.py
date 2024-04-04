import requests

from server import DataSouceUtils

baseUrl = "http://127.0.0.1:8888/api/"


def req_oriHistory(userName, startTime):
    return requests.post(baseUrl, json={
        "type": 10058,
        "dbName": "MSG0.db",
        "sql": f"select strftime('%Y-%m-%d %H:%M:%S', datetime(CreateTime, 'unixepoch', 'localtime')) as CreateTime,Type,MsgSvrID,SubType,IsSender,Status,StrTalker,StrContent,CompressContent,BytesExtra from MSG  where StrTalker = '{userName}' AND datetime(CreateTime, 'unixepoch', 'localtime') > '{startTime}' order by CreateTime limit 500"
    }).json()


def req_UserData(userNameIds):
    jso = {
        "type": 10058,
        "dbName": "MicroMsg.db",
        "sql": "select c.UserName,c.NickName,ci.smallHeadImgUrl from Contact c  left join ContactHeadImgUrl ci on c.UserName=ci.usrName where c.UserName in('" + '\',\''.join(
            userNameIds) + "')"
    }

    return requests.post(baseUrl, json=jso).json()


def getUsername(bytes_extra):
    if bytes_extra:
        try:
            matched_string = bytes_extra['3'][0]['2'].decode('utf-8', errors='ignore')
            if len(matched_string) > 30:
                print(2)
            return matched_string
        except:
            return "-"
    return "-"


def getHistory(userName, startFileName):
    """
        获取聊天记录
        :param userName: 用户名ID、群id
        :param startFileName: 查询开始时间文件
        :return: 历史消息

        todo:当前版本仅仅测试了群聊内容，未测试个人聊天内容
        todo:当前版本中仅解析了部分类型消息，未解析的消息类型会显示【暂未解析】，欢迎提交PR贡献代码（本人愿奉上红包打赏）

    """
    try:
        with open(startFileName, "r") as file:
            startTime = file.read()
    except FileNotFoundError:
        startTime = "2021-01-01 00:00:00"
    data = req_oriHistory(userName, startTime)
    msgContentArr = []
    for mesItem in data['data']['data']:
        Type = int(mesItem['Type'])
        SubType = int(mesItem['SubType'])
        CompressContent1 = DataSouceUtils.decompress_CompressContent(mesItem['CompressContent']) \
            .replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        CompressContent = DataSouceUtils.parse_xml_string(CompressContent1)
        StrContent = mesItem['StrContent']
        if Type == 10000:
            StrContent = "【系统消息】：暂未解析"
            mesItem['BytesExtra'] = ""
        if Type == 47 and SubType == 0:  # 动画表情
            StrContent = "【表情包】：暂未解析"
        # 卡片消息
        if Type == 49 and SubType == 5:
            try:
                StrContent = f"【卡片消息】\n标题{CompressContent['appmsg']['title']}\n链接：{CompressContent['appmsg']['url']}"
            except:
                StrContent = "【卡片消息】，解析出错，暂未修复"
        # 文件
        if Type == 49 and SubType == 6:
            StrContent = "【文件】：暂未解析"
        # gif
        if Type == 49 and SubType == 8:
            StrContent = "【gif图】：暂未解析"
        # 带有引用的文本消息
        if Type == 49 and SubType == 57:
            try:
                StrContent = "【带有引用的文本消息】：" + CompressContent['appmsg']['title']
            except:
                StrContent = "【带有引用的文本消息】：解析出错，暂未修复"
        # 合并转发消息
        if Type == 49 and SubType == 19:
            StrContent = "【合并转发消息】：暂未解析"
        # 视频号直播或直播回放等
        if Type == 49 and SubType == 63:
            StrContent = f"【视频号直播或直播回放】：视频号名称：{CompressContent['appmsg']['finderLive']['nickname']},描述：{CompressContent['appmsg']['finderLive']['desc']}"
        # 群公告
        if Type == 49 and SubType == 87:
            StrContent = "【群公告】：暂未解析"
        # 视频号直播或直播回放等
        if Type == 49 and SubType == 88:
            StrContent = f"【视频号直播或直播回放】：暂未解析"
        # 分享的小程序
        if Type == 49 and (SubType == 33 or SubType == 36):
            StrContent = f"【视频号直播或直播回放】：暂未解析"
        if Type == 3:
            StrContent = f"【图片消息】：暂未解析"
        if Type == 34:
            StrContent = f"【语音消息】：暂未解析"
        if Type == 43:
            StrContent = f"【视频消息】：暂未解析"
        BytesExtraXML = DataSouceUtils.read_BytesExtra(mesItem['BytesExtra'])
        mesItem['userName'] = getUsername(BytesExtraXML)
        mesItem['StrContent'] = StrContent
        mesItem.pop('BytesExtra')
        mesItem.pop('CompressContent')
        msgContentArr.append(mesItem)
    if len(msgContentArr) >= 1:
        maxTime = msgContentArr[-1]['CreateTime']
        with open(startFileName, "w") as file:
            file.write(maxTime)
    return msgContentArr


def getFinHistory(userName, startFileName):
    msg_content_arr = getHistory(userName, startFileName)
    if not msg_content_arr:
        return []
    user_name_ids = list({obj['userName'] for obj in msg_content_arr})
    user_data = req_UserData(user_name_ids)['data']['data']
    id_to_item_map = {item['UserName']: item for item in user_data}
    res = []
    for item in msg_content_arr:
        userid = item['userName']
        if userid in id_to_item_map:
            item['userName'] = id_to_item_map[userid]['NickName']
            item['img'] = id_to_item_map[userid]['smallHeadImgUrl']
        else:
            item['userName'] = '-'
            item['img'] = '-'
        res.append(item)
    return res
