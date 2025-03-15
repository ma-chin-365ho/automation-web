import os

from dotenv import load_dotenv

class PersonalInfo():

    def __init__(self):
        load_dotenv()

    @property
    def URL_MY_YMOBILE_LOGIN(self):
        return os.environ['URL_MY_YMOBILE_LOGIN']

    @property
    def ID_MY_YMOBILE(self):
        return os.environ['ID_MY_YMOBILE']

    @property
    def PW_MY_YMOBILE(self):
        return os.environ['PW_MY_YMOBILE']

    @property
    def PIN_MY_YMOBILE(self):
        return os.environ['PIN_MY_YMOBILE']

personal_info = PersonalInfo()