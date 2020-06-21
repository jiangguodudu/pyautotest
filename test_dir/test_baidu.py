#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_baidu
# @Author: Jiang Guo
# @Date  : 2020/6/20 0020
# @Desc  :


import sys
import time
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.baidu_page import BaiduPage


class TestSearch:
    """测试百度搜索"""

    def test_baidu_search_case(self, browser, base_url):
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = "pytest"
        page.search_button.click()
        time.sleep(2)
        assert browser.title == "pyst_百度搜索"