import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, socket, threading
from port_scan import scan
class T(unittest.TestCase):
    def test_open_and_closed(self):
        srv = socket.socket(); srv.bind(("127.0.0.1", 0)); srv.listen(1)
        port = srv.getsockname()[1]
        try:
            self.assertIn(port, scan("127.0.0.1", [port]))
            self.assertNotIn(port + 1 if port < 65535 else port - 1, scan("127.0.0.1", [port]))
        finally: srv.close()
if __name__ == "__main__": unittest.main()
