# robotframework-mailosaur

[![Upload Python Package](https://github.com/primait/robotframework-mailosaur/actions/workflows/publish.yml/badge.svg?branch=master)](https://github.com/primait/robotframework-mailosaur/actions/workflows/publish.yml)
[![Downloads](https://pepy.tech/badge/robotframework-mailosaur)](https://pepy.tech/project/robotframework-mailosaur)
[![Downloads](https://pepy.tech/badge/robotframework-mailosaur/month)](https://pepy.tech/project/robotframework-mailosaur)
[![Downloads](https://pepy.tech/badge/robotframework-mailosaur/week)](https://pepy.tech/project/robotframework-mailosaur)

robotframework-mailosaur is a library wrapper that helps robotframework users to test emails in a more stable and easy way.

robotframework-mailosaur is a wrapper for mailosaur, which means that to use this library you must have a [mailosaur working account](https://mailosaur.com/).

## Install robotframework-mailosaur

Install robotframework-mailosaur:

```bash
pip install robotframework-mailosaur
```

## How to use 

Once installed, create a new robotframework file and include the library with its necessary parameters:

```robotframework
Library           rfmailosaur    API_KEY=${api_key}    server_id=${server_id}    server_domain=${server_domain}
```

You're ready to go! 🎉

## Examples

you can find more extensive examples inside the `examples` folder.

```
Find email by body and test html text content
    ${email}=    Get email by body    body=Welcome
    html content should contain text    matcher=User    case_insensitive=${TRUE}    message=${email}
```

```
Test email subject with regex
    email subject should match    regex=[a-zA-Z0-9]
```

## Keyword documentation

robotframework-mailosaur has a keyword documentation which can be found inside the `docs` folder.
