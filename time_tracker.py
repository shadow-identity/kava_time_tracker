#!/bin/python

import gtk
import wnck
import glib
import datetime


class WindowTitle(object):
    # time needed to check that we are start working
    needed_working_delta = 5
    # One title opens more than that time - we are sleeping
    max_working_title_delta = 10

    def __init__(self):
        self.title = None
        self.activation_time = datetime.datetime.now()
        self.delta = None
        self.working_delta = 0
        self.not_working_delta = 0
        self.is_new_title = True
        self.is_working = False
        self.working_titles = ['PyCharm', 'Product Collector']
        # glib.timeout_add(100, self.new_title)
        # glib.timeout_add(100, self.worker)
        self.worker()

    def new_title(self):

        window = wnck.screen_get_default().get_active_window()
        if not window:
            return True
        title = window.get_name()
        if self.title != title:
            self.title = title
            print self.title
            return True
        return True

    def worker(self):
        glib.timeout_add(100, self.new_title)


WindowTitle()
gtk.main()