#####################
# ZOOM OUT FUNCTION #
def zoomOutEditor(self):
    self.current_font_size -= 1
    self.custom_font.setPointSize(self.current_font_size)
    self.text_edit.setFont(self.custom_font)
#---------------------------------------------------------------------------------------