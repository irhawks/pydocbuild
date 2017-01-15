#!/usr/bin/env python3

from .basic import *

#from selenium import webdriver

__doc__ = """
我们设计的Retriever具有链式的功能，也就是可以不断地持续为用Filter。但是最终有一个获取内容的Retriever，负责东西的出栈
这个过滤器只负责取出元素的内容
"""

class SelectSelenium (Filter) :

    def __init__(self, pattern, method="id") :
        """ 缺省是根据id进行过滤 """
        self._method = method
        self._pattern = pattern

    def select_element(self, element) :

        """ 为了统一，一致返回元素的列表 """

        if (self._method == 'id')    : 
            return element.find_element_by_id(self._pattern)
        if (self._method == 'class') : 
            return element.find_elements_by_class_name(self._pattern)[0]
        if (self._method == 'css')   : 
            return element.find_elements_by_css_selector(self._pattern)[0]
        if (self._method == 'xpath')   : 
            return element.find_elements_by_xpath(self._pattern)[0]
        return None

    def select_content(self, element) :
        e = select_element(element)
        if e : 
            return e.get_attribute('innerHTML')
        else :
            return None
