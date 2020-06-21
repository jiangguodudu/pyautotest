#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : baidu_page
# @Author: Jiang Guo
# @Date  : 2020/6/20 0020
# @Desc  :

from poium import Page, NewPageElement, PageElements


class BaiduPage(Page):
    search_input = NewPageElement(id_="kw", describe="搜索框")
    search_button = NewPageElement(id_="su", describe="搜索按钮")
    # settings =