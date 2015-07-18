# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project(app):
    project = Project(name="TestName Project", description="TestDescription Project")
    old_projects = app.project.get_project_list()
    if project in old_projects:
        app.project.delete_project(project)
        old_projects.remove(project)
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
