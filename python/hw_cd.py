import fcntl
import os


fd = os.open("/dev/sr0", os.O_RDONLY | os.O_NONBLOCK)
fp = os.fdopen(fd)
fcntl.ioctl(fp, ioctl.CDROMEJECT)
fp.close()
