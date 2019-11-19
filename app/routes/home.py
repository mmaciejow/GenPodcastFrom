from flask import render_template, request, flash, url_for
from werkzeug.utils import redirect

from . import routes


@routes.route('/', methods=["POST", "GET"])
def home():

    if request.method == 'POST':
        youtube_url = request.form['youtube_url']

        if youtube_url == '':
            flash('Url field is required!')

        try:
            if 'channel' in youtube_url:
                channel = youtube_url.split('/')
                channel = channel[4]
                return redirect(url_for('routes.youtube_channel_feed', id=channel))
            elif 'playlist' in youtube_url:
                playlist = youtube_url.split('=')
                playlist = playlist[1]
                return redirect(url_for('routes.youtube_playlist_feed', id=playlist))
            elif 'user' in youtube_url:
                user = youtube_url.split('/')
                user = user[4]
                return redirect(url_for('routes.youtube_user_feed', id=user))
            else:
                flash('Bad Youtube Url')
        except:
            flash('Bad Youtube Url')

    return render_template('home.html' )


