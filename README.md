# Robot Framework creating libraries workshop



# Workspace usage
This is a workspace for docs and code samples for the workshop about creating libraries for Robot Framework.
It can be used locally in [VS Code](https://code.visualstudio.com/) and in [Gitpod](https://www.gitpod.io).

#### The workspace contains some VS Code configuration
- List of recommended extensions
- Some common RF and Python and settings
- Launch config for [RF Language Server extension for VS Code](https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp)
  - It works after clicking on one of the code lense buttons _Run_ or _Debug_ above the test case name in _.robot_ files
  - It enables saving all RF output files in the _logs_ folder
  - It also sets the [RF log level](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#setting-log-level) to _DEBUG_ (with _INFO_ as visible by default) 

## Local usage
Please open the folder in [VS Code](https://code.visualstudio.com/) and install the recommended extensions, listed in _.vscode/extensions.json_

## Usage in Gitpod
### What is Gitpod?
[Gitpod](https://www.gitpod.io) is an IDE in the cloud.
- It opens VS Code in the browser without any local installation.
- You'll need only a GitHub account (free) which you can use to login to Gitpod.  
- Gitpod is free for individual usage up to 50h per month - see [pricing](https://www.gitpod.io/pricing).

### How to start
For this repository, you can use the prepared link:  
[**Open the workspace in Gitpod**](http://www.gitpod.io/#https://github.com/amochin/rf-libraries-workshop)  

Or you can create a Gitpod workspace from any GitHub repository just pasting it's link in the [New Workspace window](https://gitpod.io/new).

### Installing Robot Framework and libraries
Initially, the workspace has some common prerequisites installed, including **Python**, **Node.js**, **Java** and **Docker**. See the full list in the [Gitpod docs](https://www.gitpod.io/docs/configure/workspaces/workspace-image).

However, the workspace contains neither Robot Framework nor any libraries or Python modules installed. You can install them as usual:  
`pip install -r requirements.txt`
> After initial Robot Framework installation, you might need to call the **Reload window** command to get the VS Code RF Language Server extension working - use _Command Palette_ to find it.

### Check your workspace is set up successfully
Use the test suites in the _examples/0_check_installation_ folder - the tests should run without any errors.

### Gitpod workspace configuration
The _.gitpod.yml_ file contains some configuration which is used by Gitpod when creating a workspace from the repository.
- VS Code extensions to install
- Image selection and port configuration for [desktop interaction](#desktop-interaction)
- Starting a web server and port configuration for [Opening Robot Framework logs](#opening-robot-framework-logs)

### Desktop interaction
In case of GUI test automation (e.g. a web app with playwright / Browser Library), it might be helpful to access the GUI / Desktop. In Gitpod workspace, you should use **VNC** for this.  
The preconfigured image contains a VNC service running in the background on the port `6080`.  

#### The VNC client runs in the browser
- When the workspace was started, you'll see a _Simple Browser_ tab in VS Code with the VNC connection open.
- You can also open the VNC connection in an external browser window
> - It's **your** browser, the same one where you have the Gitpod workspace VS Code running.

### Opening Robot Framework logs
Robot Framework log and report output are HTML files, so they require a browser to be opened.  
For whatever reason, the included browser of Gitpod workspace throws an error.  

As a workaround, the workspace launches a simple web server running on the port `8080`, serving the entire workspace directory.  
So when you see a notification from VS Code, telling the port is open, click **Open Browser** - it opens a new browser window with all the files listed.  

Simply navigate to the required folder (e.g. _logs_) and open the RF output files as usual.
> - It's **your** browser, the same one where you have the Gitpod workspace VS Code running.
> - You can also use a _Simple Browser_ in VS Code for viewing RF logs, but you can't have two tabs of it - so either VNC or logs. 

# Workshop summary
1. Introduction - why create your own library?
2. Basic topics
    1. Static libraries
        - Module based libraries in Python (import as file)
            - Function --> keyword
            - Arguments
                - Positional args
                - Default values
                - *varargs and **kwargs
                - Argument conversion
                    - manual
                    - based on default value
                    - type hints / function annotations
                    - decorators
            - Returning values
                - Scalar values
                - Objects, lists, dictionaries
            - Failing / assertions (incl. [RF own exceptions](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#exceptions-provided-by-robot-framework) like ContinuableFailure)
            - Logging - use RF API or Python standard API
            - Library metadata ([Scope](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#toc-entry-566), Version, Docs)
            - Select which functions become keywords
                - Naming
                - Decorators (@keyword, @not_keyword)
        - Libraries as Python classes
            - Import params -> constructors
            - Import as package - set PythonPath
            - Decorators
                - @library
                    - Disables automatic keyword recognition
                    - Can set metadata
    2. Dynamic libraries
        - API methods
        - New in RF 6.1 - [interfaces in public API](https://robot-framework.readthedocs.io/en/stable/autodoc/robot.api.html#module-robot.api.interfaces)
        - PythonLibCore - shortly
            - Gives cetralized access to keywords implemented in multiple classes / files
            - Useful for larger libraries
            - https://github.com/robotframework/PythonLibCore
    3. Hybrid libraries
3. Large excercies
    1. Create a static library for automating an OpenAPI compatible REST API using the [Python OpenAPI Client generator](https://github.com/openapi-generators/openapi-python-client)
    2. Create a dynamic library for automating an XML RPC application, using standard Python XML RPC client
4. Publishing on PyPi
    - Developing a library as package - install with pip -e
    - What does a public library need?
        - Readme
        - License
        - Version
    - [Official packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
5. Remote interface - if time allows