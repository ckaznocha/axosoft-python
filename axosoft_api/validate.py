"""
Validate.

Some functions to validate methods.
"""
from .config import RESOURCES


def validate_endpoint(endpoint, verb):
    """ Test if endpoint is valid. """
    endpoint_available = (endpoint in RESOURCES)

    if endpoint_available:
        resource = RESOURCES[endpoint]
    else:
        raise LookupError('Endpoint not found')

    can_use_verb = (verb in resource['verbs'])

    if can_use_verb:
        pass
    else:
        raise LookupError('Verb not valid')

    return resource


def validate_required_params(resource, payload):
    """ Make sure no required params were missed. """
    missed = [
        x for x in resource['required']
        if x not in payload.keys()
    ]
    if len(missed) > 0:
        missed = ', '.join(missed)
        raise ValueError(
            'Missing required params in payload: %s' % missed
        )


def validate_response(response, expected_code):
    """ Validate response. """
    success = (response.status_code == expected_code)
    valid_response = (
        response.headers['content-type'] == 'application/json; charset=utf-8'
    )
    if success & valid_response:
        return True
    else:
        data = response.json()
        raise ValueError(data['error_description'])
