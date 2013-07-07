# coding: utf-8
import json

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from live.models import Raw
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        Raw(data=json.dumps(data)).save()

    def on_error(self, status_code, data):
        print status_code, data

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

class Command(BaseCommand):

    help = 'Save all tweets in raw'

    def handle(self, *args, **options):

        # from twython import Twython
        # twitter = Twython(
        #     'kwrTvQNoRilTw7l8UlMkWw',
        #     'OHm7IgQwQ7p3sJCJVLCbJyK44lIrXdPGHOnm6Mrwslc',
        #     '99312703-2sp7C9DFug9QGc0YJnW01qxrSRQc2eelAWpxefzYE',
        #     'mKaUo2fx8tRSvUkiSJME6XCjeCEqYHDKeNocGD2o'
        # )
        # print twitter.show_user(screen_name='navalny')
        # return

        stream = MyStreamer(
            'kwrTvQNoRilTw7l8UlMkWw',
            'OHm7IgQwQ7p3sJCJVLCbJyK44lIrXdPGHOnm6Mrwslc',
            '99312703-2sp7C9DFug9QGc0YJnW01qxrSRQc2eelAWpxefzYE',
            'mKaUo2fx8tRSvUkiSJME6XCjeCEqYHDKeNocGD2o'
        )

        stream.statuses.filter(track='навальный,@navalny', follow='82299300')
