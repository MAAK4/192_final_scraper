import logging, sys
from io import StringIO

logging.basicConfig( format='%(asctime)s %(name)-12s %(levelname)-8s \n%(message)s\n\n', datefmt='%m-%d %H:%M')

log = logging.getLogger(__name__)
log.setLevel("INFO")
sio = StringIO()
console = logging.StreamHandler(sio)
log.addHandler(console)
log.addHandler(logging.StreamHandler(sys.stdout))