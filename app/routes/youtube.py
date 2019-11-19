import datetime

from flask import render_template, make_response

from . import routes
from ..data.YoutubeData import YoutubeData


# FIX for some applications that doesn't see see the duration of the audio correctly
@routes.app_template_filter()
def itunes_duration(duration):
    time = int(duration)
    return datetime.timedelta(seconds=time)


@routes.route('/youtube/channel/feed/<string:id>', methods=['GET'])
def youtube_channel_feed(id):
    return generateXML(id)

@routes.route('/youtube/playlist/feed/<string:id>', methods=['GET'])
def youtube_playlist_feed(id):
    return generateXML(id)

@routes.route('/youtube/user/feed/<string:id>', methods=['GET'])
def youtube_user_feed(id):
    return generateXML(id)

def generateXML(id):
    values = YoutubeData().getDate(id)
    if values is None:
        return "Oops! Something went wrong..."

    template = render_template('rss.xml', values=values)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response
