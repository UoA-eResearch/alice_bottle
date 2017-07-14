#!/usr/bin/env python
import aiml
from bottle import get, run, default_app
import os

here = os.path.dirname(__file__)

# Create a Kernel object. No string encoding (all I/O is unicode)
kern = aiml.Kernel()
kern.setTextEncoding( None )
kern.bootstrap(brainFile=os.path.join(here, "alice_brain"))

@get('/<query>')
def index(query):
  return kern.respond(query)

application = default_app()

if __name__ == "__main__":
  run(host='0.0.0.0', port=8080)

