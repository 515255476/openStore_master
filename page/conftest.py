#coding:utf-8
import pytest


# @pytest.fixture(scope='session')
# def product_para(request):
#     # print(request.param)
#     prodata=request.param
#     return prodata


# @pytest.mark.parametrize('product_para',product_data)
# def prodata(product_para):
#     # print(product_para)
#     return product_para

# from time import sleep
#
# import pytest
# from selenium import webdriver
#
# #
# @pytest.fixture(scope='session')
# def driver(request):
# #     driver = webdriver.Chrome()
# #     driver.implicitly_wait(10)
# #     sleep(2)
#     def closedriver():
#         driver.quit()
#     request.addfinalizer(closedriver)
#     return driver


