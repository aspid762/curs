#!/bin/bash

SQLITE_VERSION='3420000'
PYTHON_VERSION='3.11.6'
PYTHON_VER = '3.11'
PIP='pip3.10'
OPENSSL_VERSION='1.1.1u'

DIR=''
DELDIRIF(){
  DIR=$1
  if [ -d ${DIR} ]; then
    echo "Delete DIR ${DIR}"
    sleep 2
    rm -rd ${DIR}
  fi
}


if [[ $1 == 'ssl' ]]; then
  echo '========== INSTALL OpenSSL =========================='
  if [ ! -f openssl-1.1.1u.tar.gz ]; then
    wget https://ftp.openssl.org/source/openssl-1.1.1u.tar.gz --no-check-certificate
  fi  
  DELDIRIF "openssl-${OPENSSL_VERSION}"
  tar -xzvf openssl-${OPENSSL_VERSION}.tar.gz
  cd openssl-${OPENSSL_VERSION}
  ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
  make
  # make test
  make install
  openssl version
  which openssl
fi 


if [[ $1 == 'python' ]]; then
  echo '========== INSTALL Python 3.10 =========================='
  if [ ! -f Python-${PYTHON_VERSION}.tgz ] 
  then
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
  fi
  DELDIRIF "Python-${PYTHON_VERSION}"
  yum install -y openssl-devel bzip2-devel libffi-devel zlib-devel
  yum install -y bison byacc cscope ctags cvs diffstat doxygen flex gcc gcc-c++ gcc-gfortran gettext git indent intltool libtool patch patchutils rcs redhat-rpm-config rpm-build subversion swig systemtap

  tar -xzf Python-${PYTHON_VERSION}.tgz
  cd Python-${PYTHON_VERSION}
#  ./configure --enable-optimizations --with-openssl=/usr --enable-loadable-sqlite-extensions
#  make altinstall
# C_INCLUDE_PATH=/usr/local/include CPLUS_INCLUDE_PATH=/usr/local/include LD_RUN_PATH=/usr/local/lib ./configure --enable-optimizations
# C_INCLUDE_PATH=/usr/local/include CPLUS_INCLUDE_PATH=/usr/local/include LD_RUN_PATH=/usr/local/lib make
# C_INCLUDE_PATH=/usr/local/include CPLUS_INCLUDE_PATH=/usr/local/include LD_RUN_PATH=/usr/local/lib make install
LD_RUN_PATH=/usr/local/lib ./configure --enable-optimizations --with-openssl=/usr
LD_RUN_PATH=/usr/local/lib make altinstall
$PIP install certifi
$PIP install --upgrade pip
fi

if [[ $1 == 'sqlite' ]]
then
  if [ ! -f sqlite-autoconf-${SQLITE_VERSION}.tar.gz ] 
  then
    wget https://www.sqlite.org/2023/sqlite-autoconf-${SQLITE_VERSION}.tar.gz
  fi
  DELDIRIF "sqlite-autoconf-${SQLITE_VERSION}"
  tar xvfz sqlite-autoconf-${SQLITE_VERSION}.tar.gz
  cd sqlite-autoconf-${SQLITE_VERSION}
  ./configure
  make
  make install
  
  #/usr/local/lib
  # https://code.djangoproject.com/ticket/30313
  cp -v .libs/libsqlite3.so.0.8.6 /usr/local/lib64/
  echo "/usr/local/lib64" > /etc/ld.so.conf.d/sqlite-x68_64.conf

  mv /usr/bin/sqlite3  /usr/bin/sqlite3_old2
  ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
  echo "/usr/local/lib/" > /etc/ld.so.conf.d/sqlite3.con
  ldconfig
  sqlite3 -version
fi

if [[ $1 == 'django' ]]
then
  cd ..
  deactivate
  python${PYTHON_VER} -m venv venv
  #echo "LD_LIBRARY_PATH='/opt/atomicorp/atomic/root/usr/lib64/'" >> venv/bin/activate
  source venv/bin/activate
  pip install Django==4.2
  django-admin startproject backend
  cd backend
  python -m django --version
  sleep 4
  python manage.py runserver  
fi
