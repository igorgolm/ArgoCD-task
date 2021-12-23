from flask import Flask, render_template
from os import environ
import socket
from time import gmtime, strftime
import distro

app = Flask(__name__)


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def get_time():
    return strftime("%a, %d %b %Y %H:%M:%S", gmtime())


def get_host():
    return distro.name()


@app.route('/')
def main():
    ip = get_ip()
    time = get_time()
    host = get_host()
    return render_template('index.html', ip=get_ip(), time=get_time(), host=get_host())