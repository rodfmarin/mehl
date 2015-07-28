#!/usr/bin/env python
import httplib

"""mehl http(s) routines"""
__author__      = "Rodrigo Marin"
__copyright__   = "Copyright 2015, Rodrigo Marin"
__credits__     = ["Rodrigo Marin"]
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Rodrigo Marin"
__email__       = "rodrigo.f.marin@gmail.com"
__status__      = "Development"


def connect(hostname, securely):
    """returns a connection object"""
    if securely:
        httpsconnection = httplib.HTTPSConnection(hostname)
        return httpsconnection
    else:
        httpconnection = httplib.HTTPConnection(hostname)
        return httpconnection


def getresponse(connection, uri):
    """returns the server response from a GET with the provided URI"""
    if (isinstance(connection, httplib.HTTPSConnection) or isinstance(connection, httplib.HTTPConnection)):
        request = connection.request("GET",uri)
        return connection.getresponse()
    else:
        raise TypeError('Must Provide an instance of HTTP or HTTPS Connection Type')




