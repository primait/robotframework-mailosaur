from rfmailosaur.keywords import keywords
from rfmailosaur.version import VERSION
from rfmailosaur.server_management_keywords import ServerManagementKeywords
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria


class rfmailosaur(keywords, ServerManagementKeywords):
    __version__ = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, API_KEY, server_id=None, server_domain=None) -> None:
        """
        The library needs a few arguments in order to work properly:

        - API_KEY which you can retrieve from your mailosaur dashboard

        - (optional) server_id which you can retrieve from your mailosaur dashboard

        - (optional) server_domain which you can retrieve from your mailosaur dashboard

        Set these arguments when importing the library in the .robot file or set a __init__.robot file with the import and parameters.


        If you want to use dynamic servers you can use server management keywords such as "create server" and "delete server".

        In case dynamic server generation is used, then "server id" and "server domain" are automatically set during server creation 
        with the keyword "create server": in addition you will need to pass the global api key as "API_KEY" parameter to the library.
        """
        self.mailosaur = MailosaurClient(API_KEY)
        self.server_id = server_id
        self.server_domain = server_domain
        self.criteria = SearchCriteria()
