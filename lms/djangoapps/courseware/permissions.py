"""
Permission definitions for the courseware djangoapp
"""

from bridgekeeper import perms
from .rules import HasAccessRule

VIEW_COURSE_HOME = 'courseware.view_course_home'
VIEW_XQA_INTERFACE = 'courseware.view_xqa_interface'

perms[VIEW_COURSE_HOME] = HasAccessRule('load')
perms[VIEW_XQA_INTERFACE] = HasAccessRule('staff')
