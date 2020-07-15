#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试代码
import allure
import pytest
import sys

sys.path.append('..')

from pythoncode.calc import Calculator


# 文件的名字要以test_开头
# 类名要以Test开头 首字母大写， 方法名要以test_开头
class TestCalc:
    # setup_class 是类级别的
    def setup_class(self):
        print("TestCalc 在整个类的前执行setup_class")
        self.calc = Calculator()

    def teardown_class(self):
        print("TestCalc在整个类的后执行teardown_class")

    # setup 是方法级别的
    def setup(self):
        print("测试用例执行之前执行setup")
        self.calc = Calculator()

    def teardown(self):
        print("测试用例执行之后执行teardown")

    @pytest.mark.parametrize('a,b,c', [
        (1, 1, 2),
        (0.1, 0.1, 0.2),
        (-1, -1, -2),
        (100, 100, 200),
        (100, -100, 150),
        (1, 0.1, 1.1)
    ])
    def test_add(self, a, b, c):
        # calc = Calculator()
        allure.attach("这是一个相加的测试用例", name='这是文本型',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(
            '<img src="https://ceshiren.com/uploads/default/original/2X/c/c49051f32076a3903e1a56a0bde6199bddd5f07b.jpeg" width="100%">',
            name='html类型',
            attachment_type=allure.attachment_type.HTML)
        assert c == self.calc.add(a, b)

    def test_add1(self):
        datalist = [
            (1, 1, 2),
            (0.1, 0.1, 0.2),
            (-1, -1, -2),
            (100, 100, 200),
            (100, -100, 150),
            (10000, 10000, 20000)
        ]
        for data in datalist:
            # calc = Calculator()
            assert data[2] == self.calc.add(data[0], data[1])

    # def test_add2(self):
    #     calc = Calculator()
    #     assert -2 == calc.add(-1,-1)

    def test_div(self):
        # calc = Calculator()
        assert 1 == self.calc.div(1, 1)

    def test_image(self):
        allure.attach.file('/Users/juanxu/Documents/霍格沃兹培训/公开课/基础公开课活码/gkkxx.png',
                           name='图片', attachment_type=allure.attachment_type.PNG)
        allure.attach.file('/Users/juanxu/Documents/霍格沃兹培训/02录播课程/python/python第三方库/python第三方库.mp4',
                           name='视频', attachment_type=allure.attachment_type.MP4)


class TestCalcDemo:
    def setup_class(self):
        print("TestCalcDemo 在整个类的前执行setup_class")
        self.calc = Calculator()

    def teardown_class(self):
        print("TestCalcDemo 在整个类的后执行teardown_class")

    def test_add1(self):
        print("测试相加")

    def div(self):
        print("测试相除")


class TestCalcDemo:
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_add1(self):
        print("测试相加")

    def div(self):
        print("测试相除")
