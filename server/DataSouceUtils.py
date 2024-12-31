import blackboxprotobuf
import lz4.block
import lxml.etree as ET

def parse_xml_string(xml_string):
    """
    解析 XML 字符串
    :param xml_string: 要解析的 XML 字符串
    :return: 解析结果，以字典形式返回
    """

    def parse_xml(element):
        """
        递归解析 XML 元素
        :param element: 要解析的 XML 元素
        :return: 解析结果，以字典形式返回
        """
        result = {}

        # 解析当前元素的属性
        if element is None or element.attrib is None:  # 有时可能会遇到没有属性，要处理下
            return result
        for key, value in element.attrib.items():
            result[key] = value

        # 解析当前元素的子元素
        for child in element:
            child_result = parse_xml(child)

            # 如果子元素的标签已经在结果中存在，则将其转换为列表
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result

        # 如果当前元素没有子元素，则将其文本内容作为值保存
        if not result and element.text:
            result = element.text

        return result

    if xml_string is None or not isinstance(xml_string, str):
        return None
    try:
        parser = ET.XMLParser(recover=True)  # 有时微信的聊天记录里面，会冒出来xml格式不对的情况，这里把parser设置成忽略错误
        root = ET.fromstring(xml_string, parser)
    except Exception as e:
        return xml_string
    return parse_xml(root)




def decompress_CompressContent(data):
    """
    解压缩Msg：CompressContent内容
    :param data:
    :return:
    """
    data = bytes.fromhex(data)
    if data is None or not isinstance(data, bytes):
        return None
    try:
        dst = lz4.block.decompress(data, uncompressed_size=len(data) << 8)
        dst = dst.replace(b'\x00', b'')  # 已经解码完成后，还含有0x00的部分，要删掉，要不后面ET识别的时候会报错
        uncompressed_data = dst.decode('utf-8', errors='ignore')
        return uncompressed_data
    except Exception as e:
        return data.decode('utf-8', errors='ignore')

def read_BytesExtra(BytesExtra):
    BytesExtra = bytes.fromhex(BytesExtra)
    if BytesExtra is None or not isinstance(BytesExtra, bytes):
        return None
    try:
        deserialize_data, message_type = blackboxprotobuf.decode_message(BytesExtra)
        return deserialize_data
    except Exception as e:
        return None
