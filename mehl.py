#!/usr/bin/env python
import argparse
import sys
import mehldata
import mehlhttp
import mehlsmtp

"""Main mehl module called from command line with arguments"""
__author__ = "Rodrigo Marin"
__copyright__ = "Copyright 2015, Rodrigo Marin"
__credits__ = ["Rodrigo Marin"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Rodrigo Marin"
__email__ = "rodrigo.f.marin@gmail.com"
__status__ = "Development"


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-k", "--key", type=str, help="your meh.com API Key read from stdin")
	parser.add_argument("-s", "--smtphost", type=str, help="the smtphost to send messages to")
	parser.add_argument("-f", "--fromaddress", type=str, help="the sender of the message")
	parser.add_argument("-t", "--to", type=str, help="the recipient to send the message to")
	parser.add_argument("-u", "--username", type=str, help="the smtp username to use", default=None)
	parser.add_argument("-p", "--password", type=str, help="the smtp password to use", default=None)
	args = parser.parse_args()

	if args.key:
		try:
			connection = mehlhttp.connect('api.meh.com', True)
			response = mehlhttp.getresponse(connection, ('/1/current.json?apikey={}').format(args.key))
			jsondata = response.read()
			htmldata = mehldata.encode_to_html(jsondata)
			htmldata = htmldata.encode('utf-8')
			# sending your deal (yay!)
			mehlsmtp.send_message(args.smtphost, args.fromaddress, args.to, htmldata, args.username, args.password)
			print("deal sent!")
			sys.exit(0)

		except Exception as e:
			print("exception caught in main()")
			print(e)

	else:
		print("please provide API Key, Exiting...")
		sys.exit(1)


if __name__ == '__main__':
	main()
