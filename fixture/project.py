# -*- coding: utf-8 -*-
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")
                and len(wd.find_elements_by_link_text("Manage Projects")) == 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def change_field_value(self, field_name, input_text):
        wd = self.app.wd
        if input_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_text)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector(".width100 [class^='row']")[1:]:
                name = element.find_element_by_css_selector('a').text
                description = element.find_elements_by_css_selector('td')[4].text
                id = element.find_element_by_css_selector('a').get_attribute("href").split('=')[-1]
                self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)
