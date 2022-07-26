from django.test import Client
from .test_basesample import BaseTestSample


class CatalogTestingSearch(BaseTestSample):
    
    def setUp(self):
        super().setUp()

    def test_index_search_1(self):
        c = Client()
        response = c.get("/catalog", { 'search': 'ab',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i1, self.i4])
        
    def test_index_search_2(self):
        c = Client()
        response = c.get("/catalog", { 'search': 'a2 bb da',})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i3, self.i4])
        
    def test_index_search_3(self):
        c = Client()
        response = c.get("/catalog", {
            'category': 'C1_C2',
            'price': '0-30',
            'search': 'aa b',
            'sort': 'ascprice',
            'num': 2,
            'page': 1,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["pagination"].object_list),
                         [self.i2, self.i1])
