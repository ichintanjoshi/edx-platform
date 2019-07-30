"""
URLs for the CCX Feature.
"""
from __future__ import absolute_import

from django.conf.urls import url

from lms.djangoapps.ccx.views import (
    create_ccx,
    ccx_gradebook,
    ccx_grades_csv,
    ccx_schedule,
    ccx_students_management,
    dashboard,
    save_ccx,
    set_grading_policy
)

urlpatterns = [
    url(r'^ccx_coach$', dashboard, name='ccx_coach_dashboard'),
    url(r'^create_ccx$', create_ccx, name='create_ccx'),
    url(r'^save_ccx$', save_ccx, name='save_ccx'),
    url(r'^ccx_schedule$', ccx_schedule, name='ccx_schedule'),
    url(r'^ccx-manage-students$', ccx_students_management, name='ccx-manage-students'),

    # Grade book
    url(r'^ccx_gradebook$', ccx_gradebook, name='ccx_gradebook'),
    url(r'^ccx_gradebook/(?P<offset>[0-9]+)$', ccx_gradebook, name='ccx_gradebook'),

    url(r'^ccx_grades.csv$', ccx_grades_csv, name='ccx_grades_csv'),
    url(r'^ccx_set_grading_policy$', set_grading_policy, name='ccx_set_grading_policy'),
]
