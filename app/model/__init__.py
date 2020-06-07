import os

HOME_PATH = os.path.join(os.environ['HOME'], ".tdl")
if not os.path.exists(HOME_PATH):
    os.mkdir(HOME_PATH)

DATABASE_PATH = HOME_PATH + "td_list.db"
