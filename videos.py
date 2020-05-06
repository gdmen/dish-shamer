import argparse
import os
import pexpect
import sys

parser = argparse.ArgumentParser(description='Fetch all videos corresponding to the specified thumbnail images.')
parser.add_argument('ip', metavar='IP', type=str, help='IP address of the pi')
parser.add_argument('user', metavar='user', type=str, help='user of the pi')
parser.add_argument('password', metavar='password', type=str, help='password of the pi')

args = parser.parse_args()

videos = []
for f in os.listdir("./debug/selected_thumbs"):
    if f.endswith(".jpg"):
        videos.append("./videos/%s.mp4" % f[:f.rfind('-')])

host = "%s@%s" % (args.user, args.ip)
cmd = 'scp -T %s:%s %s' % (host, '"%s"' % ' '.join(videos), './debug/videos')

child = pexpect.spawn(cmd, timeout=None, encoding='utf-8')
child.logfile_read = sys.stdout
child.expect('.*assword:')
child.sendline(args.password)
child.expect(pexpect.EOF)
