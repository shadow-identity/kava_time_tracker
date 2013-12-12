#!/bin/python

import gtk
import wnck
import glib
import datetime
import time


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
        glib.timeout_add(100, self.new_title)
        # glib.timeout_add(100, self.worker)
        # self.worker()

    def new_title(self):
        window = False
        while not window:
            window = wnck.screen_get_default().get_active_window()
            time.sleep(1)
        title = window.title()
        if self.title != title:
            self.title = title
            print self.title
            return True
        return True


        # try:
        #     title = wnck.screen_get_default().get_active_window().get_name()
        #     if self.title != title:
        #         self.title = title
        #         print self.title
        #         return True
        #         # self.is_new_title = True
        #     # self.is_new_title = False
        #     return True
        # except AttributeError:
        #     pass
        # return False

    def current_delta(self):
        return self.activation_time - datetime.datetime.now()

    def is_working_title(self):
        for work_title in self.working_titles:
            if self.title in work_title:
                return True
            else:
                return False

    def worker(self):
        while not self.new_title():
            time.sleep(1)
        # Working title or any title opened for less of 30 seconds
        if self.is_working_title() or self.current_delta() < self.needed_working_delta:
            self.working_delta += self.current_delta()
            # We are about to start working
            if self.working_delta > self.needed_working_delta and not self.is_working:
                self.set_eta_job()
            # We are sleeping
            if self.working_delta > self.max_working_title_delta and self.is_working:
                self.set_eta_done()
        else:
            self.working_delta = 0
            if self.is_working:
                self.set_eta_done()
        return True

    def set_eta_done(self):
        self.is_working = False
        print('we goes online because window {title} opened {delta} seconds'.format(
            title=self.title, delta=self.delta))

    def set_eta_job(self):
        self.is_working = True
        print('we goes offline because window {title} opened {delta} seconds'.format(
            title=self.title, delta=self.delta))

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



WindowTitle()
gtk.main()