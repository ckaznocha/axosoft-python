axosoft-python
================================
[![Build Status](http://img.shields.io/travis/ckaznocha/axosoft-python.svg?style=flat)](https://travis-ci.org/ckaznocha/axosoft-python)
[![Coverage Status](https://img.shields.io/coveralls/ckaznocha/axosoft-python.svg?style=flat)](https://coveralls.io/r/ckaznocha/axosoft-python)
[![Release](http://img.shields.io/github/release/ckaznocha/axosoft-python.svg?style=flat)](https://github.com/ckaznocha/axosoft-python/releases/latest)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat)](http://ckaznocha.mit-license.org)

An unofficial Python module for the Axosoft (formerly OnTime) API.

## Usage
1. Import the module into your project
    ```python
    from axosoft_api import Axosoft
    ```

1. Create a new `Axosoft` instance
    
    The constructor accepts 4 arguments
    1. The client ID provided to you by Axosoft
    1. The client secret provide to you by Axosoft
    1. The domain you use to access Axosoft with out the protocol
        - i.e. if your domain is `https://foo.axosoft.com` you would use `foo.axosoft.com`
    1. Optionally a token form a previous session if you wont need to authenticate again
    ```python
    axosoft_client = Axosoft(
            'Your client ID',
            'Your client secret',
            'Your Axosoft domain'
        )
    ```

1. Authenticate
    
    The authentication method returns the token so it can be used for future sessions
    ```python
        token = axosoft_client.authenticate_by_password(
            axosoft_user,
            axosoft_password
        )
    ```

    If you need to confirm that the your are successfully authenticated you may use the `is_authenticated` method
    ```python
        if axosoft_client.is_authenticated:
            pass
    ````

1. Start interacting with your Axosoft API resources
    ```python
        # These examples arbitrarily use the release endpoint

        """
        Create a new release.

        The first argument is the resource type your creating
        The second argument is the payload which should be a dictionary containing at minimum the required fields for the resource type
        """
        r = axosoft_client.create('releases', payload={'name': 'testRelease', 'release_type': {'id': 1}})
        
        """
        Get the content of a release

        The first argument is the resource type you want to get
        The second argument is optionally the id of a specific resource
        The third argument is optionally a dictionary of parameters
        """
        r = axosoft_client.get('releases', r['id'])
        
        """
        Update a release

        The first argument is the resource type you want to update
        The second argument is the id of the resource you are updating
        The third arguments is a dictionary containing all the fields of you resource
        """
        r = axosoft_client.update('releases', r['id'], payload={'name': 'testRelease', 'release_type': {'id': 1}})
        
        """
        Delete a release

        The first argument is the resource type you want to delete
        The second argument is the id of the resource you want to delete
        Returns true if the delete was successful
        """
        r = self.axosoft_client.delete('releases', r['id'])

    ````


##To Do
- Implement code grant type authentication.
- Figure out a nice way child resources.
    - e.g. `/features/{id}/emails`
- Handle binary attachments.

##Contributing
See the `CONTRIBUTING` file.

##License
See the `LICENSE` file.

This project and its contributers are in no way affiliated with Axosoft. Axosoft and the Axosoft API are the copyright of Axosoft, LLC