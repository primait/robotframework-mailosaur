import re

class keywords(object):

    def email_subject_should_match(self, regex: str, message=None):
        """
        Checks the email subject of the last email received on the current server_domain matches the given regular expression.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(self.server_id, self.criteria)
        if message is not None:
            last_email = message
        check = bool(re.match(r'{}'.format(regex), last_email.subject))
        if check is False:
            raise Exception(
                "The regexp does not match {}".format(last_email.subject))

    def email_subject_should_contain(self, matcher: str, message=None):
        """
        Checks the email subject of the last email received on the current server_domain contains the matcher.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(self.server_id, self.criteria)
        if message is not None:
            last_email = message
        try:
            assert matcher in last_email.subject
        except AssertionError as e:
            raise Exception("AssertionError: '{0}' does not contain '{1}'".format(
                last_email.subject, matcher))

    def delete_all_emails(self):
        """
        deletes all emails contained in the currently selected server domain.
        """
        self.criteria.sent_to = self.server_domain
        try:
            self.mailosaur.messages.delete_all(self.server_id)
        except Exception as e:
            raise e

    def email_should_have_links(self, links_number: int, message=None):
        """
        Checks the last email contains X number of links where X == links_number.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        links = len(last_email.html.links)
        try:
            assert links == links_number
        except AssertionError as e:
            raise Exception("AssertionError: {0} does not equal {1}".format(
                links, links_number))

    def email_should_have_attachments(self, attachments_number: int, message=None):
        """
        Checks the last email contains X number of attachments where X == attachments_number.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        attachments = len(last_email.attachments)
        try:
            assert attachments == attachments_number
        except AssertionError as e:
            raise Exception("AssertionError: {0} does not equal {1}".format(
                attachments, attachments_number))

    def email_body_should_contain(self, matcher, case_insensitive: bool, message=None):
        """
        Checks the last email's body contains a specific string (matcher).

        If case_insensitive is set to True, then case is not checked in the substring.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        text = last_email.text.body
        if case_insensitive is True:
            text = text.lower()
            matcher = matcher.lower()
        try:
            assert matcher in text
        except AssertionError as e:
            raise Exception("AssertionError: {0} is not contained {1}".format(
                matcher, text))

    def email_links_should_contain_text(self, text: str, message=None):
        """
        Checks if atleast one of the links contained in the last email contains text.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        links = [link.text for link in last_email.text.links]
        assert any(map(lambda link: text in link, links))

    def email_sender_should_be(self, matcher: str, message=None):
        """
        Checks that last email sender matches the given matcher.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        sender = last_email.sender[0].email
        try:
            assert sender == matcher
        except AssertionError as e:
            raise Exception("AssertionError: '{0}' does not match sender '{1}'".format(
                matcher, sender))

    def html_content_should_contain_text(self, matcher: str, case_insensitive, message=None):
        """
        Checks that last email's HTML content contains sub-string
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        if message is not None:
            last_email = message
        html = last_email.html.body
        if case_insensitive is True:
            html = html.lower()
            matcher = matcher.lower()
        try:
            assert matcher in html
        except AssertionError as e:
            raise Exception("AssertionError: '{0}' is not contained in '{1}'".format(
                matcher, html))

    def list_emails(self):
        """
        Returns a list of all email messages
        """
        self.criteria.sent_to = self.server_domain
        results = self.mailosaur.messages.list(self.server_id)
        return results.items

    def get_last_email(self):
        """
        Returns last email message.

        Note: this keyword returns a 'MessageSummary' object which does not include several properties. 
        To get a more complete message, please use 'get email' keywords.
        """
        self.criteria.sent_to = self.server_domain
        results = self.mailosaur.messages.list(self.server_id)
        last_email = results.items[0]
        return last_email

    def get_email_by_sender(self, sender, timeout=10000):
        """
        Waits for a message to be found. Returns as soon as a message matching the specified search criteria is found.
        timeout: Specify how long to wait for a matching result (in milliseconds, default value is 10 seconds).
        """
        self.criteria.sent_from = sender
        message = self.mailosaur.messages.get(
            self.server_id, self.criteria, timeout=timeout)
        return message

    def get_email_by_subject(self, subject, timeout=10000):
        """
        Waits for a message to be found. Returns as soon as a message matching the specified search criteria is found.
        timeout: Specify how long to wait for a matching result (in milliseconds, default value is 10 seconds).
        """
        self.criteria.subject = subject
        message = self.mailosaur.messages.get(
            self.server_id, self.criteria, timeout=timeout)
        return message

    def get_email_by_body(self, body, timeout=10000):
        """
        Waits for a message to be found. Returns as soon as a message matching the specified search criteria is found.
        timeout: Specify how long to wait for a matching result (in milliseconds, default value is 10 seconds).
        """
        self.criteria.body = body
        message = self.mailosaur.messages.get(
            self.server_id, self.criteria, timeout=timeout)
        return message
