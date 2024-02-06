"""
The XMLRPC Server should implement same methods as with the dynamic library API -
get_keyword_names, run_keyword etc.
Afterwards the exposed keywords can be called using the Remote Library 
RobotFrameworkUserGuide.html#remote-library-interface
"""

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    """
    Standard path for XML RPC requests
    """

    rpc_paths = ("/RPC2",)


with SimpleXMLRPCServer(("localhost", 8270), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    
    # Implement API methods here

    # Run the server's main loop
    server.serve_forever()
