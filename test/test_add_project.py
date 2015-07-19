# -*- coding: utf-8 -*-
from model.project import Project
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(name=random_string("name_", 10), description=random_string("description_", 10))
    old_projects = app.soap.get_project_list()
    if project in old_projects:
        app.project.delete_project(project)
        old_projects.remove(project)
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = app.soap.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
