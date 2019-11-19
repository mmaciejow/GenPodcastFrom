from .. import db


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.String(64), index=True, unique=True)
    avatar = db.Column(db.String())

    def __init__(self, channel_id, avatar):
        self.channel_id = channel_id
        self.avatar = avatar

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(64), index=True, unique=True)
    audio_url = db.Column(db.String())
    duration = db.Column(db.String())

    def __init__(self, video_id, audio_url,duration):
        self.video_id = video_id
        self.audio_url = audio_url
        self.duration = duration
