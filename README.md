# moodleCal
### What does this?
The python script logs into Moodle every 2h and downloads the calendar in the ical format.
And the nginx hosts this file under port 8888.

### But why?
Since the last update the calendar only works with login which is bad because no client supports it.
Maybe it is just a config fail in the RUB-Moodle.

### Use it
Change these to your own credentials in `getcal.py` under `main()`

```python
loginURL = 'Your Moodle Login Url'   #e.g.: 'https://moodle.ruhr-uni-bochum.de/m/login/index.php'
calURL = 'Your calendar URL' #e.g.: 'https://moodle.ruhr-uni-bochum.de/m/calendar/export_execute.php?userid=42&authtoken=deadbeefcafebabe&preset_what=all&preset_time=recentupcoming''
username = 'Your Moodle username'
password = 'Your Moodle password'
```
You get the calendar URL in your Moodle under `calendar > export calendar > set preferences and click get calendar URL`

Install docker and docker-compose if you haven't already and do `docker-compose up -d`
You find the logs under `docker-compose logs`

Then you can set the URL in your calendar sync application to `http://<your hostname or ip adress>:8888/moodle.ical`

