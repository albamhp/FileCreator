import configparser

Config = configparser.ConfigParser()

Config.read("configure/config.ini")

raspberry = Config.getboolean("Section1", "raspberry")


rows = Config.getint("Section2", "rows")
cols = Config.getint("Section2", "cols")

