from django.test import TestCase
from .models import Author, Project
# Create your tests here.

class AuthorTestClass(TestCase):

    def setUp(self):
        self.moha = Author(first_name = 'Moha', last_name = 'Moha', email = 'moha@moha.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.moha,Editor))


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='moha')
        self.project = Project.objects.create(id=1, name='test', description='test 1', user=self.user, link='http://test.com')
        self.rating = Rating.objects.create(id=1, design=6, usability=7, content=9, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_project_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(project_id=id)
        self.assertTrue(len(rating) == 1)

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.project = project.objects.create(id=1, title='test project', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, project))

    def test_save_project(self):
        self.project.save_project()
        project = project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = project.all_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_project(self):
        self.project.save()
        project = project.search_project('test')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = project.search_project('test')
        self.assertTrue(len(project) < 1)