import gconf

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



if __name__ == '__main__':
    try:
        save_original_settings()
        set_away_mode()
        while True:
            pass
    except:
        restore_original_settings()
        print("Original settings restored.")
