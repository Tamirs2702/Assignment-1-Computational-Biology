import eel
eel.init('web')
eel.start('main.html')

my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('main.html', options=my_options)
