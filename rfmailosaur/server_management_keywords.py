from mailosaur.models import ServerCreateOptions, MailosaurException

class ServerManagementKeywords(object):
    
    def delete_server(self, server_id: str):
        """
        Deletes the given server by server_id.
        """
        try:
            self.mailosaur.servers.delete(server_id)
        except MailosaurException as e:
            raise(e)

    def retrieve_server(self, server_id: str):
        """
        Retrieve a server by server_id, the retrieved server object is accessible with the following attributes:

        - id
        - name
        - users
        - messages
        - retention
        - domain
        - restricted
        """
        try:
            self.mailosaur.servers.get(server_id)
        except MailosaurException as e:
            raise(e)
            
    def create_server(self, server_name):
        """
        Creates a server with specified server name.

        This keyword returns the created server object which is accessible with the following attributes:

        - id
        - name
        - users
        - messages
        - retention
        - domain
        - restricted
        """
        options = ServerCreateOptions(server_name)
        created_server = self.mailosaur.servers.create(options)
        self.server_id = created_server.id
        self.server_domain = created_server.id + ".mailosaur.net"
        return created_server

    def get_servers_list(self):
        """
        Returns a list of all the available servers
        """
        servers_list = self.mailosaur.servers.list()
        if len(servers_list.items) > 1:
            return servers_list.items