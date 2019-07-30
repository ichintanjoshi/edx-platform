"""
Permission definitions for the courseware djangoapp
"""

from bridgekeeper import perms
from .rules import HasAccessRule

EDIT_BOOKMARK = 'courseware.edit_bookmark'
VIEW_COURSE_HOME = 'courseware.view_course_home'

perms[EDIT_BOOKMARK] = HasAccessRule('staff')
perms[VIEW_COURSE_HOME] = HasAccessRule('load')
