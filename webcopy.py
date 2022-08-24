# from pywebcopy import save_webpage
 
# kwargs = {'project_name': 'site folder'}
 
# save_webpage(
   
#     # url pf the website
#     url='https://www.geeksforgeeks.org/data-structures/linked-list/',
     
#     # folder where the copy will be saved
#     project_folder='F:/ro/geek',
#     **kwargs
# )
from pywebcopy import save_webpage
save_webpage(
      url="https://httpbin.org/",
      project_folder="E://savedpages//",
      project_name="my_site",
      bypass_robots=True,
      debug=True,
      open_in_browser=True,
      delay=None,
      threaded=False,
)