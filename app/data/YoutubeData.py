import requests
import bs4 as bs
import youtube_dl
import feedparser

from .. import Config
from .. import db
from ..models.YouTube import Channel, Video


class YoutubeData:

    def getDate(self, id):
        try:
            if id.startswith('UC', 0, 2):
                url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + id
            elif id.startswith('PL', 0, 2):
                url = "https://www.youtube.com/feeds/videos.xml?playlist_id=" + id
            else:
                url = "https://www.youtube.com/feeds/videos.xml?user=" + id

            parser = feedparser.parse(url)

            info_channel = {'channelTitle': parser.feed.title,
                            'channelLink': parser.feed.url,
                            'channelAvatar': self.__getAvatarFromChannel(parser.feed.yt_channelid),
                            }

            items_list = []
            for content in parser.entries:
                audio = self.__getAudioInfo(content['yt_videoid'])
                item = {
                    'title': content['title'],
                    'published': content['published'],
                    'link': content['link'],
                    'description': content['summary'],
                    'linkAudio': audio.audio_url,
                    'duration': audio.duration

                }
                items_list.append(item)

            data = {
                "infoChannel": info_channel,
                'items': items_list
            }
            return data
        except:
            return

    def __getAvatarFromChannel(self, channel_id):
        try:
            channel = Channel.query.filter_by(channel_id=channel_id).first()
            if channel is None:
                url = "http://www.youtube.com/channel/" + channel_id
                res = requests.get(url)
                content = res.text
                soup = bs.BeautifulSoup(content)
                hrefs = soup.find_all('img', {'class': "channel-header-profile-image"})
                avatar_url = hrefs[0]['src']
                # if you need a larger size - uncomment bellow line uncomment the following line
                # avatar_url = avatar_url.replace('s100', 's288')
                channel = Channel(channel_id, avatar_url)
                db.session.add(channel)
                db.session.commit()
                return avatar_url
            else:
                return channel.avatar
        except:
            return

    def __getAvatarFromPlaylist(self, id):
        try:
            url = "https://www.youtube.com/playlist?list=" + id
            res = requests.get(url)
            content = res.text
            soup = bs.BeautifulSoup(content)
            for div in soup.find_all('div', class_='pl-header-thumb'):
                for img in div.find_all('img'):
                    if 'no_thumbnail' in img['src']:
                        return 'https://www.youtube.com/about/static/svgs/icons/brand-resources/YouTube_icon_full-color.svg'
                    else:
                        return img['src']
        except:
            return

    def __getAudioInfo(self, video_id):
        try:
            video = Video.query.filter_by(video_id=video_id).first()
            if video is None:
                url = "https://www.youtube.com/watch?v=" + video_id
                ydl_opts = {'format': 'bestaudio[ext=m4a]',
                            'youtube_include_dash_manifest': False,
                            'quiet': True
                            }
                ydl = youtube_dl.YoutubeDL(ydl_opts)

                with ydl:
                    result = ydl.extract_info(
                        url,
                        download=False,  # We just want to extract the info
                    )
                    video = Video(video_id, result['url'], result['duration'])
                    db.session.add(video)
                    db.session.commit()
                    return video
            else:
                return video
        except:
            return
