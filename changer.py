#! /usr/bin/python

import os
from datetime import date

from gi.repository import Gio


class BackgroundChanger(object):

    SCHEMA = 'org.gnome.desktop.background'
    KEY = 'picture-uri'

    def __init__(self):
        self.gsettings = Gio.Settings.new(self.SCHEMA)

    def get_current_wallpaper(self):
        year, month, day = map(str, date.today().timetuple()[:3])

        current_path = os.path.dirname(os.path.abspath(__file__))

        wallpaper_path = os.path.join(
            current_path,
            'wallpapers',
            year,
            month,
            "{}.png".format(day)
        )

        return wallpaper_path

    def set_wallpaper(self, path):
        self.gsettings.set_string(self.KEY, "file://" + path)


background = BackgroundChanger()
background.set_wallpaper(background.get_current_wallpaper())
