I'm Away
========

Are you stepping away from you computer but need to run it anyway? Are you
concerned about the power consumption? Are you bothered by turning all the
monitors off manually?

We have a solution!

You run the I'm Away tool and all your displays will automaticaly turn off a
minute later. If something wakes them up while you're away, they'll get turned
off again.

Once you get back, you press the "I'm back" button and you're done! Your power
settings will get restored to the way they were before you started the app.


Requirements
------------
* Python2
* PyGTK


Installation
------------
Put the `away.py` file to the directory for the installed apps (probably
/usr/bin/).

    $ sudo cp ~/code/away/away.py /usr/bin/

Put the `away.desktop` file to the directory for the apps' shortcuts (probably
/usr/share/applications/).

    $ sudo cp ~/code/away/away.desktop /usr/share/applications/

Edit the `away.desktop` file and replace the `$PREFIX` part in the `Exec`
field with the path to the `away.py` file (probably `/usr/bin/away.py`).

    $ sudo sed -e "s/\$PREFIX/\/usr\/bin/" --in-place /usr/share/applications/away.desktop

Make sure you have the `python2` executable working. If not, replace the
"python2" part in the `away.desktop` file with whatever is your Python 2
executable.


Roadmap
-------
* automate the installation
* dim the window surroundings when the app is running
    - this will make it stand out. It'll save users from forgetting to close
      the program and then be annoyed when the display turns off.


License
-------
Copyright (C) 2010 Tomas Sedovic <tomas@sedovic.cz>

The "I'm Away" program is distributed under the Version 3 of the GPL or any
later version. See the included COPYING file for the full text of the license.
