from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Changed from calendar/quickstart/quickstart.py downloaded from Google Calendar API
# Google Calendar API
# Author: Zihao Zhao

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def call_calendar():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    # 'Z' indicates UTC time
    prev = now.rfind("-")+1
    num = "%02d" % (max(0, int(now[prev:prev+2])-5))
    now = now[0:prev]+num+now[prev+2:]

    print('Getting the events 10 events from last 5 days')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print(events_result)
    result = []
    if not events:
        result.append('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start + ' ' + event['summary'])
        result.append(' ' + start + ' ' + event['summary'])

    return result
