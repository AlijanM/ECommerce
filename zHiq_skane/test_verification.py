from selenium import webdriver
from zHiq_skane.testfile import CvDataBase
import pytest


class CvDataBaseTest():

    def verifySearch(self):
        cvdb = CvDataBase()
        cvdb.test_listOfCompetences("alijan.momeni@hiq.se", "Hiq2020?", "Python")

# cdbt = CvDataBaseTest()
# cdbt.verifySearch()