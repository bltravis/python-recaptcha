#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools(version='0.6c3')

from setuptools import setup, find_packages

setup(name='recaptcha-client',
      version='1.0.1',
      url = "http://recaptcha.net/",
      author = "Ben Maurer",
      author_email = "support@recaptcha.net",
      description = "A plugin for reCAPTCHA and reCAPTCHA Mailhide",
      long_description = "Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require any imaging libraries because the CAPTCHA is served directly from reCAPTCHA. Also allows you to securely obfuscate emails with Mailhide. This functionality requires pycrypto. This library requires two types of API keys. If you'd like to use the CAPTCHA, you'll need a key from http://recaptcha.net/api/getkey. For Mailhide, you'll need a key from http://mailhide.recaptcha.net/apikey",

      license = "MIT/X11",
      classifiers = [
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        ],


      packages = find_packages(),

      extras_require = {
        'mailhide' : ['pycrypto'],
        },
      namespace_packages = ['recaptcha'],
      )

