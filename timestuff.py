import datetime
import pytz


# print(datetime.now())

LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
print(LOCAL_TIMEZONE)

tz = pytz.timezone(LOCAL_TIMEZONE)
print(datetime.datetime.now(tz))