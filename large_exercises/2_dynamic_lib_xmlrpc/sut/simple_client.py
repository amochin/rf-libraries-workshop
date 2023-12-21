"""
The client is needed only to check if the XMLRPC SUT is running,
it's not required for the Robot Framework library
"""
import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8270")
print(s.run_script("large_exercises/2_dynamic_lib_xmlrpc/libs/scripts/create_employee.script", "some_value"))
print(s.system.listMethods())