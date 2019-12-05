import subprocess
import time
location = 'umami burger'
while True:
    p = subprocess.Popen(
    ["instagram-scraper", "--search-location", location],
     stdout=subprocess.PIPE)
    output, err = p.communicate()
    if output != "":
        print( output)
    # time.sleep(20)
