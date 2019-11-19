## GenPodcastFrom

If you want to listen to interviews, conferences or other content from videos as a podcast.
GenPodcastFrom is for you. 

GenPodcastFrom currently supports YouTube and allows you get RSS feed from any YouTube channel, playlist. 
Generate RSS XML file.

App base on [Youtube-dl](https://github.com/ytdl-org/youtube-dl) and [Flask](https://github.com/pallets/flask). 


## Install

It requires the Python interpreter, version 3.2+. 

    $ git clone https://github.com/mmaciejow/GenPodcastFrom
    $ cd GenPodcastFrom 

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ deactive

## Run

    $ venv/bin/python GenPodcastFrom.py

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

Check app/Config.py file to customize the application.

**WARNING: This is a development app. Do not use it in a production deployment.**

## Contributing

I made this app for improve my programming skills (Python). 
So bug reports and pull requests are welcome on GitHub at https://github.com/mmaciejow/GenPodcastFrom. 


## License

GenPodcastFrom is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
ChecK LICENSE file.
