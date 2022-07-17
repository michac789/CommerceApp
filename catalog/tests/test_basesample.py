from django.test import TestCase, Client
from tests import *

from myshop.models import Category, Item
from sso.models import User


class BaseTestSample(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", email="user1@gmail.com", password="123",
        )
        self.user2 = User.objects.create_user(
            username="user2", email="user2@gmail.com", password="123",
        )
        self.c1 = Category.objects.create(category="c1", code="C1")
        self.c2 = Category.objects.create(category="c2", code="C2")
        self.c3 = Category.objects.create(category="c3", code="C3")
        self.i1 = Item.objects.create(
            title="ab", description="", price=12.99,
            category=self.c1, seller=self.user1,
        )
        self.i2 = Item.objects.create(
            title="Ba", description="", price=8.7,
            category=self.c1, seller=self.user1,
        )
        self.i3 = Item.objects.create(
            title="a2", description="", price=21.01,
            category=self.c2, seller=self.user1,
        )
        self.i4 = Item.objects.create(
            title="ad", description="", price=19.4,
            category=self.c1, seller=self.user2,
        )
        self.i5 = Item.objects.create(
            title="Aa", description="", price=50,
            category=self.c2, seller=self.user2,
        )


class CatalogTestingIndex(BaseTestSample):
    
    def setUp(self):
        super().setUp()
    
    def test_index_all(self):
        c = Client()
        response = c.get("/catalog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2, self.i3, self.i4, self.i5])
        self.assertQuerysetEqual(response.context["pagination"], Item.objects.all(),
                                 transform=lambda _: _)
