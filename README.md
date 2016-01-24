## Synopsis

A repository for all things Raspberry Pi related

## Code Example

SdCardPrep.py is used to dump a bootable image onto an SD card in preparation for building a new OS. 

```
usage: SdCardPrep.py [-h] sdcard {2,3,4} imgfile

Script for preparing an SD card for a Raspberry Pi. Disk utility SD card IDs
are limited to 2, 3 and 4 in an attempt to stop catastrophic dd errors on disk
IDs 0 and 1. They are normally the backup partition and main Mac HD)

positional arguments:
  sdcard      Path to SD card (e.g. /Volumes/UNTILTLED)
  {2,3,4}     Diskutil SD card ID (e.g. 2)
  imgfile     Path to image fiel (e.g. Downloads/Jessie.img)

optional arguments:
  -h, --help  show this help message and exit
```

## Motivation

Setting up many Raspberry Pis by hand takes a long time. The goal is to speed this up.

## Installation

Clone the repositiory using:
```
git clone git@github.com:jmccormac01/RaspberryPi.git
```
and voila. Run any of the scripts with the -h option to see the usage menu and description. 

## API Reference

N/A

## Tests

Example run preparing an SD card with Jessie using SdCardPrep.py:

```
▶ python SdCardPrep.py /Volumes/UNTITLED 2 /Users/James/Downloads/2015-11-21-raspbian-jessie.img
Proceed with caution!
Have you entered the correct disk/image information?
If not you might render your computer useless!
To continue type: 'do it': do it
Ok, let's go!
Unmounting /dev/disk2
Using dd to copy /Users/James/Downloads/2015-11-21-raspbian-jessie.img --> /dev/disk2
This may take some time...
Password:
3752+0 records in
3752+0 records out
3934257152 bytes transferred in 1538.355005 secs (2557444 bytes/sec)
Ejecting /dev/disk2
Disk has been cloned and ejected, please remove and test the new SD card
```

## Contributors

James McCormac

## License

_Update_