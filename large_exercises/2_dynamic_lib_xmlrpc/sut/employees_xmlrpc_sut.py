"""
This is a simple SUT for excercising creating a dynamic library for Robot Framework.
Technically, it emulates a tool similar to Eggplant - capable performing some magic
based on some .script files written in it's own language.

From the business logic, the SUT is similar to an emloyees database.
There are some .script files prepared, which allow some basic operations with it's records.

The excercise idea is to create a dynamic library, which discovers all .script files
and exposes them as keywords.

It is basically an XML RPC server with a single function _run_script_,
which takes a path to a .script file as argument.

Launching this python script emulates running the SUT
and allows execution of the Dynamic Library API function _run_keyword_.
"""
import os
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    """
    Standard path for XML RPC requests
    """
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8270),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def run_script(file_path, args):
        """
        Just check if the script file exists and return it's name and args
        """
        if os.path.isfile(file_path):
            return f"Running script file '{os.path.basename(file_path)}' with args: {args}"
        raise FileNotFoundError(f"Script not found: {file_path}")

    server.register_function(run_script, 'run_script')

    # Run the server's main loop
    server.serve_forever()
