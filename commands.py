import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ['yes', 'sure', 'affirmative', 'do it']
        self.cancel = ['no', 'negative', 'don\'t']

    def discover(self, text):
        if 'what' in text and 'your name' in text:
            if 'my' in text:
                self.respond('You haven\'t told me yet')
            else:
                self.respond('My name is PythonCommander')
        
        elif 'launch' or 'open' in text:
            app = text.split(' ', 1)[-1]
            self.respond('Opening ' + app)
            os.system('start ' + app)
        
        elif ['quit', 'exit', 'bye', 'goodbye'] in text:
            self.respond('Closing...')

    def respond(self, response):
        subprocess.call('echo ' + response, shell=True)