# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__   = 'GPL v3'
__copyright__ = '2020, Bennett Kanuka <bkanuka@gmail.com>'
__docformat__ = 'restructuredtext en'

# The class that all Interface Action plugin wrappers must inherit from
from calibre.customize import InterfaceActionBase

class HideStatusbarPlugin(InterfaceActionBase):

    name                = 'Hide Statusbar'
    description         = 'Hides the statusbar'
    supported_platforms = ['windows', 'osx', 'linux']
    author              = 'Bennett Kanuka'
    version             = (1, 0, 1)
    minimum_calibre_version = (5, 0, 0)

    #: This field defines the GUI plugin class that contains all the code
    #: that actually does something. Its format is module_path:class_name
    #: The specified class must be defined in the specified module.
    actual_plugin       = 'calibre_plugins.hide_statusbar.ui:InterfacePlugin'

    def is_customizable(self):
        return False

