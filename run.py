import re
import winapps
from winapps import list_installed
import psutil

apps_load = winapps.list_installed()
#listing and converting to string
listing_all_apps = [str(i) for i in apps_load]
regrex = r"name=['][\w\s]*[']"
apps = [
        app[6:-1]
        for detail in listing_all_apps
        for app in re.findall(regrex, detail)
        ]

print(apps)