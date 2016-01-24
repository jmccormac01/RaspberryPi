# script to prepare Jessie on an RPi SD card

import os,sys
import argparse as ap

junk=['.Spotlight-V100','.fseventsd','.Trashes','._.Trashes']

def argParse():
	description="""
		Script for preparing an SD card for a Raspberry Pi. Disk utility SD card IDs are limited to 2, 3 and 4 in an attempt to stop catastrophic dd errors on disk IDs 0 and 1. They are normally the backup partition and main Mac HD)
		"""
	parser=ap.ArgumentParser(description=description)
	parser.add_argument("sdcard",help="Path to SD card (e.g. /Volumes/UNTILTLED)")
	parser.add_argument("sdid",type=int,help="Diskutil SD card ID (e.g. 2)",choices=[2,3,4])
	parser.add_argument("imgfile",help="Path to image fiel (e.g. Downloads/Jessie.img)")
	return parser.parse_args()

args=argParse()

if os.path.exists(args.sdcard) == False:
	print('No such SD card %s' % (args.sdid))
	sys.exit(1)
if os.path.exists(args.imgfile) == False:
	print('No such image file %s' % (args.imgfile))
	sys.exit(1)

# remove mac junk from card
cwd=os.getcwd()
os.chdir(args.sdcard)
for i in junk:
	os.system('rm -rf %s' % (i))
os.chdir(cwd)

# dump the image onto the card
power=raw_input("Proceed with caution!\nHave you entered the correct disk/image information?\nIf not you might render your computer useless!\nTo continue type: 'do it': ")
if power == 'do it':
	print('Ok, let\'s go!')
	print('Unmounting /dev/disk%d' % (args.sdid))
	res1=os.popen('diskutil unmountDisk /dev/disk%d' % (args.sdid)).readlines()
	if 'Unmount of all volumes on disk%d was successful\n' % (args.sdid) not in res1[0]:
		print('Error unmounting /dev/disk%d, exiting...' % (args.sdid))
		sys.exit(1)
	print('Using dd to copy %s --> /dev/disk%s' % (args.imgfile,args.sdid))
	print('This may take some time')
	print('Enter the root password\n')
	res2=os.popen('sudo dd bs=1m if=%s of=/dev/disk%d' % (args.imgfile,args.sdid)).readlines()
	print('Ejecting /dev/disk%d' % (args.sdid))
	res3=os.popen('diskutil eject /dev/disk%d' % (args.sdid)).readlines()
	if 'Disk /dev/disk%d ejected' % (args.sdid) not in res3[0]:
		print("Problem ejecting /dev/disk%d, exiting..." % (args.sdid))
		sys.exit(1)
	print('Disk has been cloned and ejected, please remove and test the new SD card')
else:
	print("You have chickened out, exiting...")
	sys.exit(1)


