bitcoin
=======

bitcoin candlestick  
Installation on Ubuntu12.04  
1.node.js  
sudo apt-get install python-software-properties python g++ make  
sudo add-apt-repository ppa:chris-lea/node.js  
sudo apt-get update  
sudo apt-get install nodejs  
2.socket.io  
npm install socket.io  
3. numpy and scipy  
sudo apt-get install python-numpy  
sudo apt-get install python-scipy  
sudo apt-get install python-matplotlib  
4. Pandas  
apt-get install python-pandas (only 0.7.0)  
sudo pip install --upgrade pandas (will upgrade to 0.12.0)  
5. MySQLDB  
http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python(Win7)  


How to run django celery tasks:  
cd to bitcoin directory  
manage.py celery worker  
manage.py celery beat -lDEBUG -S djcelery.schedulers.DatabaseScheduler  

How to install numpy  
http://www.scipy.org/install.html  

1.IP  
redis  
socket.io server can't set to localhost  
market.html  
