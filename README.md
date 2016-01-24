## Synopsis

A repository for all things Raspberry Pi related

## Motivation

Setting up a Raspberry Pi is fun, but not trival for everyone. These scripts are meant as a quick introduction to some things I found interesting when setting up and playing with the boards. 

## Code Description

**gpio_test.py** is a simple program with no command line options. It is simply to demonstrate how to set up and read the state of 2 GPIO pins on a Raspberry Pi. You can change the pin numbers and modify this code to read any number of pins. This example was written using a Hall effect sensor which was trigger by moving a magnet in front of it. Hence the print statements, _Tiggered_ and _Not Triggered_ .

**SdCardPrep.py** is used to dump a bootable image onto an SD card in preparation for building a new OS. This has been written and tested using Mac OSX Yosemite. 

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

Insert the SD and use the disk utility to determine its disk number, e.g. /dev/disk2. In this case we would enter 2 as the second command line option. See below for an example run.  

## Installation

Clone the repositiory using:
```
git clone git@github.com:jmccormac01/RaspberryPi.git
```
and voila. Run any of the scripts with the -h option (if it takes command line arguments) to see the usage menu and description. 

## API Reference

N/A

## Tests

Example run preparing an SD card with Jessie using SdCardPrep.py. Before running SdCardPrep.py I used disk utility to determine that my SD card was /dev/disk2. Therefore I used 2 as the second command line option. When inserted my SD card mounts as /Volumes/UNTITLED and the image I want to dump onto the SD card is 2015-11-21-raspbian-jessie.img, which is located in /Users/James/Downloads/. 

```
▶ python SdCardPrep.py /Volumes/UNTITLED 2 /Users/James/Downloads/2015-11-21-raspbian-jessie.img
Proceed with caution!
Have you entered the correct disk/image information?
If not you might render your computer useless!
To continue type: 'do it': do it
Ok, let's go!
Unmounting /dev/disk2
Using dd to copy /Users/James/Downloads/2015-11-21-raspbian-jessie.img --> /dev/disk2
This may take some time
Enter the root password
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