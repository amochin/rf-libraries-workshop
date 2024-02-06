"""
Implement RF Dynamic Library API according to User Guide:
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#dynamic-library-api
"""
class MyLib:
    def get_keyword_names(self):
        my_keywords = ["Get captain",
                       "Get captains favorite sport"]
        return my_keywords
    
    def run_keyword(self, name, args):
        print(f"Calling keyword {name} with args {args}")

    def get_keyword_arguments(self, name):
        if name == "Get captain":
            return ["Starship"]
        else:
            return ["Captains name"]