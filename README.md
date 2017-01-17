[mrt] motion setup notes
.ssh/addkey pi@192.168.1.90
install missing dependencies `sudo apt-get install lua`
follow instructions here: http://wiki.raspberrytorte.com/index.php?title=Motion_MMAL

ln -s /etc/motion/motion.conf /etc/motion.conf
ln -s /etc/motion.conf ~/motion.conf

activated motion script in /etc/init.d/motion (from apt-get install motion?)

To prevent wifi module from sleeping, add to crontab:
* * * * * ping -c 59 192.168.1.1 > /dev/null

To prevent images from filling disk memory, add to crontab:
* * * * * python ~/cull_images.py | sudo tee -a /var/log/messages > /dev/null

see /etc/motion.conf for config
motion files are saved to /tmp/motion
webcam is at http://192.168.1.90:8081/
logging is to /var/log/messages
