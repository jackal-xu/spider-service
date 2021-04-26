#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: jaxon
@Time: 2020-12-24 15:58
"""

import urllib
import sys
import typing

from mitmproxy import http

# command: mitmdump -s write_cookie.py -w cookie.txt mp.weixin.qq.com/mp/getappmsgext

class WriterCookie():
    """
    mitmproxy的监听脚本，写入cookie和url到文件
    """

    def __init__(self, path: str) -> None:
        self.f = open(path, 'w')
        

    def response(self, flow: http.HTTPFlow) -> None:
        """
        完整的response响应
        :param flow: flow实例，
        """
        # 获取url
        url = urllib.parse.unquote(flow.request.url)
        # 将url和cookie写入文件
        if "mp.weixin.qq.com/mp/getappmsgext" in url:
            print(url)
            self.f.write(str(flow.request.cookies))
            self.f.close()
            # 退出
            exit()
        
# 第四个命令中的参数
addons = [WriterCookie(sys.argv[4])]

