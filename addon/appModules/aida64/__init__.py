import addonHandler
import api
import appModuleHandler
import mouseHandler
import tones
import ui
import winUser
from controlTypes import Role
from scriptHandler import script

addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
    scriptCategory = 'Aida Menu'

    @script(
        description=_('Open the menu'),
        gesture='kb:nvda+o',
    )
    def script_open_menu(self, gesture):
        try:
            search_field = api.getForegroundObject().children[1].children[0]
        except IndexError:
            search_field = None
        if search_field is None or search_field.role != Role.EDITABLETEXT:
            ui.message(_('Failed to open the menu.'))
            return
        menu_x = search_field.location.right + 15
        menu_y = search_field.location.center.y
        winUser.setCursorPos(menu_x, menu_y)
        mouseHandler.doPrimaryClick()
        tones.beep(100, 50)
