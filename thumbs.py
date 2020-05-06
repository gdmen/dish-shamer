import argparse
import os
import pexpect
import sys

parser = argparse.ArgumentParser(description='Fetch all thumbnail images.')
parser.add_argument('ip', metavar='IP', type=str, help='IP address of the pi')
parser.add_argument('user', metavar='user', type=str, help='user of the pi')
parser.add_argument('password', metavar='password', type=str, help='password of the pi')

args = parser.parse_args()

host = "%s@%s" % (args.user, args.ip)
cmd = 'scp %s:%s %s' % (host, './videos/*.jpg', './debug/thumbs')

child = pexpect.spawn(cmd, timeout=None, encoding='utf-8')
child.logfile_read = sys.stdout
child.expect('.*assword:')
child.sendline(args.password)
child.expect(pexpect.EOF)
