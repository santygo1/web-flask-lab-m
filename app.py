from flask import Flask

app = Flask(__name__)

from controller import index
from controller import subject