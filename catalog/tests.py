from django.test import TestCase, Client

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
            title="t1", description="", price=12.99,
            category=self.c1, seller=self.user1,
        )
        self.i2 = Item.objects.create(
            title="t2", description="", price=8.7,
            category=self.c1, seller=self.user1,
        )
        self.i3 = Item.objects.create(
            title="t3", description="", price=21.01,
            category=self.c2, seller=self.user1,
        )
        self.i4 = Item.objects.create(
            title="t4", description="", price=19.4,
            category=self.c1, seller=self.user2,
        )
        self.i5 = Item.objects.create(
            title="t5", description="", price=50,
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
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i2, self.i3, self.i4, self.i5])
        self.assertQuerysetEqual(response.context["items"], Item.objects.all(),
                                 transform=lambda _: _)
        
    def test_index_filter_category_1(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i2, self.i4])
        
    def test_index_filter_category_2(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3_C2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i3, self.i5])
        
    def test_index_filter_category_3(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i2, self.i3, self.i4, self.i5])
        
    def test_index_filter_category_4(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]), [])
        
    def test_index_filter_price_1(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '10-99999',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i3, self.i4, self.i5])
        
    def test_index_filter_price_2(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '0-12.99',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i2])
        
    def test_index_filter_price_3(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '10-20',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i1, self.i4])
        
    def test_index_filter_price_4(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '13-15',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]), [])
        
    def test_index_filter_category_price_1(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C3',
            'price': '15-20'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i4])
        
    def test_index_filter_category_price_2(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C2',
            'price': '10-40',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]),
                         [self.i3])
        
    def test_index_filter_category_price_3(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3',
            'price': '1-25',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["items"]), [])
