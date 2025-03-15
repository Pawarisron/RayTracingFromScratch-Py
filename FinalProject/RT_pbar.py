import progressbar
import time
 
 
# Function to create 
def start_animated_marker(maxbar):
    widgets = [
        'Rendering: ', 
        progressbar.Bar('='),
        ' (',
        progressbar.ETA(),
        progressbar.Percentage(),
        ')'
    ]
    bar = progressbar.ProgressBar(max_value=maxbar, widgets=widgets).start()
     
    return bar
         
