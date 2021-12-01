#!/usr/bin/env python
import json
import time
import string

"""mehl data routines"""
__author__ = "Rodrigo Marin"
__copyright__ = "Copyright 2015, Rodrigo Marin"
__credits__ = ["Rodrigo Marin"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Rodrigo Marin"
__email__ = "rodrigo.f.marin@gmail.com"
__status__ = "Development"


def encode_to_html(jsondata):
    """
    encodes meh.com json data into html for email, sample provided in json-response-example.json
    """
    data = json.loads(jsondata)
    date = time.strftime("%m/%d/%Y")
    template = open("./markuptemplate.html")
    template = string.Template(template.read())

    templatedate = date
    templatebackgroundcolor = data["deal"]["theme"]["backgroundColor"]
    templatetitle = data["deal"]["title"]
    templatefeatures = data["deal"]["features"]
    templatephoto = data["deal"]["photos"][0]
    templatestory = data["deal"]["story"]["title"]
    templatebody = data["deal"]["story"]["body"]
    templatespecifications = data["deal"]["specifications"]
    templateprice = data["deal"]["items"][0]["price"]
    templateurl = data["deal"]["url"]

    final_output = template.safe_substitute(
        date=templatedate,
        dealbackgroundcolor=templatebackgroundcolor,
        dealtitle=templatetitle,
        dealfeatures=templatefeatures,
        dealphoto=templatephoto,
        dealstorytitle=templatetitle,
        dealstorybody=templatebody,
        dealspecifications=templatespecifications,
        dealprice=templateprice,
        dealurl=templateurl
    )

    return final_output
