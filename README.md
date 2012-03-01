sccms-nonrel
============

_A port of [Simple-Comic-CMS](https://github.com/thomasgilgenast/Simple-Comic-CMS) to django-nonrel and django-filetransfers for Google App Engine deployment._

<img src="http://sccms.gilgi.org/img/sccms.png" alt="Simple-Comic-CMS" title="Simple-Comic-CMS" height="250px" width="250px"/>

Introduction
------------

If you're looking for an easy way to deploy Simple-Comic-CMS to the Google App Engine, you've come to the right place. With sccms-nonrel, you can have your own webcomic up and running in no time!

Prerequisites
-------------

- [Python 2.x](http://python.org/)
- [Django 1.x](https://www.djangoproject.com/)

Installation
------------

Make sure you have the prerequisites listed above installed. Next, [download the latest version of sccms-nonrel](https://github.com/thomasgilgenast/sccms-nonrel/zipball/master). Unzip the archive to any directory on your file system.

Alternatively, you can clone the git repository by executing

    git clone git://github.com/thomasgilgenast/sccms-nonrel.git

Feel free to fork the repository and develop your own tweaks and features under the conditions of the license (see below).


Quick-Start (in Eight Easy Steps)
--------------------------------

1. Go to [appengine.google.com](http://appengine.google.com), log in with your Google Account, and follow the instructions to enable Google App Engine for your account (if you haven't done so already).
2. Create a new app, and remember your app's application identifier.
3. In `app.yaml`, replace `myapp` with the application identifier for your app.
4. In `comicms/settings.py`, change `SITE_TITLE` from 'My Awesome Webcomic' to whatever you actually want to call your site.
5. Run `python manage.py deploy` and authenticate with your Google Account when prompted.
6. Run `python manage.py remote createsuperuser` to create a superuser for yourself.
7. Point your browser to <http://your_application_identifier.appspot.com/admin/>
8. Click on "Comics" and then "Add comic". Fill out all the fields, upload your image, and click "Save".

It's that simple! Point your browser to <http://your_application_identifier.appspot.com> to see your comic!

Notes
-----

### Comic Numbering

Make sure your comic numbering is consistent. Presently, sccms-nonrel does not check to make sure that your numbering is correct. Numbering your comics incorrectly will result in broken navigation links.

Next Steps
----------

### Domain Setup

If you have a domain you'd like to host your webcomic on, you can add a domain to your app by going to the Application Settings page on your Google App Engine dashboard.

### Site Themes

The templates directory contains a bare-bones example template (`comic.html`) that you should feel free to modify and style however you like. If you want to add CSS, Javascript, or other static files, remember to add the appropriate file or directory handlers in `app.yaml`.

### Need Help?

For more information visit <http://sccms.gilgi.org>. Direct all questions, comments, and bug reports to <sccms@gilgi.org>.

License Information
-------------------

SCCMS is released under the terms of the GNU General Public License. For details, please visit <http://www.gnu.org/licenses/gpl.html>.

Modules from the django-nonrel project are redistributed under the terms of the license found in `LICENSE`.

sccms-nonrel utilizes and is distributed with Aaron Madison's improved django-filetransfers module, which is redistributed under the terms of the same license.