# -*- coding: utf-8 -*-
from group_lib import Group
from fixture.variables import Profinity


def test_create_group(app):
    """Validation of correct create test group (All field fill up)"""

    old_groups = app.group.get_group_list()
    group = Group(group_name=Profinity.correct_data, group_header=Profinity.correct_data,
                           group_footer=Profinity.correct_data)
    app.group.create(group)
    app.group.click_group_page()

    new_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)

    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max)


def test_create_group_name(app):
    """Validation of correct create test group (Only group name fill up)"""
    old_groups = app.group.get_group_list()
    group = Group(group_name='test')
    app.group.create(group)

    app.group.click_group_page()
    new_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max)

def test_edit_group(app):
    """Validation of correct edit group (all field updated)"""


    app.group.validation_of_group_exist()
    old_groups = app.group.get_group_list()
    group = Group(group_name=Profinity.long_word_20, group_header=Profinity.long_word_20,
                               group_footer=Profinity.long_word_20)
    group.id = old_groups[0].id
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) == len(new_groups)

    old_groups[0] = group
    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max)

def test_delete_group(app):
    """Validation of correct delete group"""

    app.group.validation_of_group_exist()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups)-1 == len(new_groups), 'Group does not created'
    old_groups[0:1] = []
    assert old_groups == new_groups




