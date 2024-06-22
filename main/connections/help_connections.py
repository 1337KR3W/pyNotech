class HelpConnections:
    def __init__(self):

        #---- Help CONNECTIONS
        self.about.triggered.connect(self.showAbout)
        self.moreHelp.triggered.connect(self.showMoreHelp)
        self.contribute.triggered.connect(self.goGitRepo)
        #---------------------------------------------------------------------------------------