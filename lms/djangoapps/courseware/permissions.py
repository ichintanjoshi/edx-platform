"""
Permission definitions for the courseware djangoapp
"""

from bridgekeeper import perms
from .rules import HasAccessRule

VIEW_COURSE_HOME = 'courseware.view_course_home'
perms[VIEW_COURSE_HOME] = HasAccessRule('load')
ACCESS_COURSE = 'courseware.access_course'
perms[ACCESS_COURSE] = HasAccessRule('staff')
CAN_MASQUERADE_AS_STUDENT = 'courseware.can_masquerade_as_student'
perms[CAN_MASQUERADE_AS_STUDENT] = HasAccessRule('staff')
