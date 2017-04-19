# Install required packages
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y git-core python3-pip libpq-dev binutils libproj-dev gdal-bin
sudo apt-get install -y postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1 python-psycopg2

# Create database
sudo su - postgres << START
createdb geodjango
psql -c "CREATE ROLE geo WITH SUPERUSER LOGIN PASSWORD 'password';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE geodjango TO geo;"
START


# Get and install GIS libs
cd ~
mkdir GIS-libs
cd GIS-libs

# GEOS
wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
tar xjf geos-3.4.2.tar.bz2
cd geos-3.4.2
./configure
make
make install
ldconfig
cd ..

# PROJ.4
wget http://download.osgeo.org/proj/proj-4.9.1.tar.gz
wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz
tar xzf proj-4.9.1.tar.gz
cd proj-4.9.1/nad
tar xzf ../../proj-datumgrid-1.5.tar.gz
cd ..
./configure
make
make install
ldconfig
cd ..

# GDAL
wget http://download.osgeo.org/gdal/1.11.2/gdal-1.11.2.tar.gz
tar xzf gdal-1.11.2.tar.gz
cd gdal-1.11.2
./configure
make
make install
ldconfig


# Create virtualenv for PyCharm to use
cd ~
mkdir venv
cd venv
pip3 install virtualenv
virtualenv . -p /usr/bin/python3
source bin/activate
pip install django
pip install psycopg2
