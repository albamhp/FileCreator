import configparser
Config = configparser.ConfigParser()

# lets create that config file for next time...
cfgfile = open("configure/config.ini", 'w')

# add the settings to the structure of the file, and lets write it out...
Config.add_section('Section1')
Config.set('Section1', 'raspberry', 'True')

Config.add_section('Section2')
Config.set('Section2', 'rows', '8')
Config.set('Section2', 'cols', '8')

Config.write(cfgfile)
cfgfile.close()
