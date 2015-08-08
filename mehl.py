#!/usr/bin/env python
import argparse
import sys
import mehldata
import mehlhttp
import mehlsmtp

"""Main mehl module called from command line with arguments"""
__author__      = "Rodrigo Marin"
__copyright__   = "Copyright 2015, Rodrigo Marin"
__credits__     = ["Rodrigo Marin"]
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Rodrigo Marin"
__email__       = "rodrigo.f.marin@gmail.com"
__status__      = "Development"


def main():
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", type=string, help="your meh.com API Key read from stdin", action="store_true", required=True)
parser.add_argument("-s", "--smtphost",  type=string, help="the smtphost to send messages to, is localhost if not specified", default="localhost")
parser.add_argument("-f", "--from", type=string, help="the sender of the message")
parser.add_argument("-t", "--to", type=string, help="the recipient to send the message to")
args = parser.parse_args()

if args.key:
	try:
		connection = mehlhttp.connect('api.meh.com', True)
		response = mehlhttp.getresponse(connection, ('/1/current.json?apikey={}').format(args.key))
		jsondata = response.read()
		htmldata = mehldata.encodetohtml(jsondata)

		#sending your deal (yay!)
		mehlsmtp.sendmessage(args.smtphost, args.from, args.to, htmldata)
		print "deal sent!"
		sys.exit(0)

	except Exception as e:
		print "exception caught in main()"
		print e



else:
	print "please provide API Key, Exiting..."
	sys.exit(1)


if __name__ == '__main__':
	main()


	