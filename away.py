import gconf
import pygtk
pygtk.require('2.0')
import gtk

AWAY_SETTINGS = {
    "/apps/gnome-power-manager/timeout/sleep_display_ac": 60,
}
ORIGINAL_SETTINGS = {}

def set(key, value):
    client = gconf.client_get_default()
    return client.set_int(key, value)

def get(key):
    client = gconf.client_get_default()
    return client.get_int(key)

def save_original_settings():
    """ Save the original settings so that they can be restored later. """
    for key in AWAY_SETTINGS:
        ORIGINAL_SETTINGS[key] = get(key)

def set_away_mode():
    client = gconf.client_get_default()
    for key, value in AWAY_SETTINGS.items():
        set(key, value)

def restore_original_settings():
    for key, value in ORIGINAL_SETTINGS.items():
        set(key, value)

def restore_and_quit(*args):
    restore_original_settings()
    gtk.main_quit()


if __name__ == '__main__':
    window = gtk.Window()
    vbox = gtk.VBox()
    label = gtk.Label("Away: the screen will turn off in a minute.")
    button = gtk.Button("I'm back.")

    window.add(vbox)
    vbox.add(label)
    vbox.add(button)
    window.connect("delete-event", restore_and_quit)
    button.connect("clicked", restore_and_quit)

    save_original_settings()
    set_away_mode()
    window.show_all()
    gtk.main()
