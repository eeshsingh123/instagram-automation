from instapy import InstaPy

from config import INSTA_USERNAME, INSTA_PASSWORD

session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
session.login()