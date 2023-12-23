import logging
from django.http import HttpResponse
from datetime import datetime


logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    html = '''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>Главная</title>
</head>
<body>
<h1>Это главная страница</h1>  
</body>
</html>
'''
    logger.info(f'Index page was visited at {datetime.now()}.')
    return HttpResponse(html)


def about(request):
    html = '''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>О себе</title>
</head>
<body>
<h1>Это страница обо мне...</h1>  
</body>
</html>
'''
    logger.info(f'About page was visited at {datetime.now()}.')
    return HttpResponse(html)
