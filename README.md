# LINK CUTTER
## Yet another service to make short urls from long ones which has written on Python 3
**********************************
First of create python virtual environment and install all Python 3 requirements:
```bash
cd link_cutter
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt

```
Now we can start service:  
```bash
link_cutter/.env/bin/python link_cutter/link_cutter.py -d
```

link_cutter.py has serveral options:
* -d  Drop all tables if exsits and create new
* -t  Generate test data in database
* -v  Turn on debug for flask app
