from pyforms.basewidget import BaseWidget
from confapp import conf

class SiteCrawlApp(BaseWidget):

    UID                  = 'site-crawl-app'
    TITLE                = 'Site crawl'

    ORQUESTRA_MENU       = 'left'
    ORQUESTRA_MENU_ICON  = 'browser'
    ORQUESTRA_MENU_ORDER = 0