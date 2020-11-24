import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget, QTextEdit
from PyQt5.QtCore import QDate, Qt
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.calDate  = []
        self.calTime  = []
        self.calEvent = []
        self.initUI()


    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        self.calText = QTextEdit()
        self.calText.setText("")

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.calText)

        self.setLayout(vbox)
        self.readGoogleCal()
        self.verify()

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())
        self.calText.setText("")
        for i in range(len(self.calDate)):
            temp = self.calDate[i]
            if temp == date.toString(Qt.ISODate):
                text = self.calText.toPlainText()
                #print(text)
                self.calText.setText(text +'\n' + self.calDate[i] + ' ' + self.calTime[i] + ' ' + self.calEvent[i])


    def readGoogleCal(self):

        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))

            dateVar, timeVar = start.split('T')
            eventVar = event['summary']

            self.calDate.append(dateVar)
            self.calTime.append(timeVar)
            self.calEvent.append(eventVar)
            #print(calDate[count]+' ' + calTime[count] + ' ' +calEvent[count])

    def verify(self):
        for i in range(len(self.calDate)):
            print(self.calDate[i] + ' ' + self.calTime[i] + ' ' +self.calEvent[i])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())