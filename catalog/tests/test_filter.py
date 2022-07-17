from django.test import Client
from .test_basesample import BaseTestSample


class CatalogTestingFilter(BaseTestSample):
    
    def setUp(self):
        super().setUp()
        
    def test_index_filter_category_1(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2, self.i4])
        
    def test_index_filter_category_2(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3_C2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3, self.i5])
        
    def test_index_filter_category_3(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2, self.i3, self.i4, self.i5])
        
    def test_index_filter_category_4(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list), [])
        
    def test_index_filter_price_1(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '10-99999',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i3, self.i4, self.i5])
        
    def test_index_filter_price_2(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '0-12.99',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2])
        
    def test_index_filter_price_3(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '10-20',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i4])
        
    def test_index_filter_price_4(self):
        c = Client()
        response = c.get("/catalog", {
            'price': '13-15',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list), [])
        
    def test_index_filter_category_price_1(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C3',
            'price': '15-20'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i4])
        
    def test_index_filter_category_price_2(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C2',
            'price': '10-40',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3])
        
    def test_index_filter_category_price_3(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C3',
            'price': '1-25',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list), [])
