from main.functions.show_about import showAbout
from main.functions.show_more_help import showMoreHelp
from main.functions.go_git_repo import goGitRepo

class HelpConnections:
    def __init__(self):

        #---- Help CONNECTIONS
        self.about.triggered.connect(showAbout)
        self.moreHelp.triggered.connect(showMoreHelp)
        self.contribute.triggered.connect(goGitRepo)
        #---------------------------------------------------------------------------------------