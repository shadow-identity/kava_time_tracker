#!/bin/python

import gtk
import wnck
import glib
import datetime


class WindowTitle(object):
    def __init__(self):
        self.title = None
        self.activation_time = datetime.datetime.now()
        self.delta = None
        self.working_delta = 0
        self.not_working_delta = 0
        self.is_new_title = True
        self.working_titles = ['PyCharm', 'Product Collector']
        # glib.timeout_add(100, self.new_title)
        glib.timeout_add(100, self.worker)
        # self.worker()

    def new_title(self):
        try:
            title = wnck.screen_get_default().get_active_window().get_name()
            if self.title != title:
                self.title = title
                return True
                # self.is_new_title = True
            # self.is_new_title = False
            return False
        except AttributeError:
            pass
        return False

    def current_delta(self):
        return self.activation_time - datetime.datetime.now()

    def is_working_title(self):
        for work_title in self.working_titles:
            if self.title in work_title:
                return True
            else:
                return False

    def worker(self):
        if self.new_title() and not self.is_working_title():
            if self.working_delta < 30:
                self.working_delta = 0
                self.not_working_delta += self.current_delta()
            else:



        return True











                #
                # # if self.activation_time:
                # self.delta = (datetime.datetime.now() - self.activation_time).total_seconds()
                # print("{title} was shown {delta} seconds".format(title=self.title, delta=self.delta))
                # self.activation_time = datetime.datetime.now()
                #
                # # beginning of work
                # if self.title in self.working_titles and self.delta >= 30 and not self.is_working:
                #     self.set_eta_job()
                #
                # # work ends
                # if self.delta <= 30:
                #     self.set_eta_done()


    def set_eta_done(self):
        print('we goes online because window {title} opened {delta} seconds'.format(
            title=self.title, delta=self.delta))

    def set_eta_job(self):
        print('we goes offline because window {title} opened {delta} seconds'.format(
            title=self.title, delta=self.delta))

WindowTitle()
gtk.main()