from widgets.menu_bar import cop

class EditConnections:
    def __init__(self):

        #---- Edit CONNECTIONS
        self.copy.triggered.connect(self.text_edit.copy)
        self.cut.triggered.connect(self.text_edit.cut)
        self.paste.triggered.connect(self.text_edit.paste)
        self.search.triggered.connect(self.searchAndHighlight)
        self.selectAll.triggered.connect(self.text_edit.selectAll)
        self.cleanSearch.triggered.connect(self.cleanSearchTerms)
        self.undo.triggered.connect(self.text_edit.undo)
        self.redo.triggered.connect(self.text_edit.redo)