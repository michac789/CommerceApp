from django.test import Client
from .test_basesample import BaseTestSample


class CatalogTestingFilter(BaseTestSample):
    
    def setUp(self):
        super().setUp()
        
    def test_index_sort_1(self):
        c = Client()
        response = c.get("/catalog", { 'sort': 'asctitle',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3, self.i5, self.i1, self.i4, self.i2])
        response = c.get("/catalog", { 'sort': 'destitle',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i2, self.i4, self.i1, self.i5, self.i3])
        
    def test_index_sort_2(self):
        c = Client()
        response = c.get("/catalog", { 'sort': 'ascprice',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i2, self.i1, self.i4, self.i3, self.i5])
        response = c.get("/catalog", { 'sort': 'desprice',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i5, self.i3, self.i4, self.i1, self.i2])
        
    def test_index_sort_3(self):
        c = Client()
        response = c.get("/catalog", { 'sort': 'asctime',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2, self.i3, self.i4, self.i5])
        response = c.get("/catalog", { 'sort': 'destime',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i5, self.i4, self.i3, self.i2, self.i1])
        
    def test_index_sort_4(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C2',
            'price': '13-22',
            'sort': 'destitle',
            'num': 1,
            'page': 2,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3])
        
    def test_index_sort_5(self):
        c = Client()
        response = c.get("/catalog", {
            'sort': 'ascprice',
            'num': 3,
            'page': 1,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i2, self.i1, self.i4])
