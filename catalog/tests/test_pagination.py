from django.test import Client
from .test_basesample import BaseTestSample


class CatalogTestingPagination(BaseTestSample):
    
    def setUp(self):
        super().setUp()

    def test_index_pagination_1(self):
        c = Client()
        response = c.get("/catalog", {
            'num': '2',
            'page': '2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3, self.i4])
    
    def test_index_pagination_2(self):
        c = Client()
        response = c.get("/catalog", {
            'num': '4',
            'page': '1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i2, self.i3, self.i4])
        
    def test_index_pagination_3(self):
        c = Client()
        response = c.get("/catalog", {
            'num': '4',
            'page': '100',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i5,])
        
    def test_index_pagination_4(self):
        c = Client()
        response = c.get("/catalog", {
            'num': '1',
            'page': '-1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1,])
        
    def test_index_pagination_5(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C2',
            'price': '12-25',
            'num': '2',
            'page': '2',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i4,])
