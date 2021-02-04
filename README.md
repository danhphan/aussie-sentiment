# From Social Sentiment Dash Application
Live-streaming sentiment analysis application created with Python and Dash, Sentdex

## Quick start

- Clone repo
- install `requirements.txt` using `pip install -r requirements.txt`
- Fill in your Twitter App credentials to `twitter_stream.py`. Go to [**apps.twitter.com**](https://apps.twitter.com/) to set that up if you need to.
- Run `twitter_stream.py` to build database
- If you're using this locally, you can run the application with the `dev_server.py` script. If you want to deploy this to a webserver, see my [**deploying Dash application tutorial**](https://pythonprogramming.net/deploy-vps-dash-data-visualization/)
- You might need the latest version of sqlite. 
```
sudo add-apt-repository ppa:jonathonf/backports
sudo apt-get update && sudo apt-get install sqlite3
```
- Consider running the `db-truncate.py` from time to time (or via a cronjob), to keep the database reasonably sized. In its current state, the database really doesn't need to store more than 2-3 days of data most likely. 

### Tips for Running on Server
- You can use Gunicorn to run the server
```
gunicorn dash_mess:server -b 0.0.0.0:80 -w 4
```