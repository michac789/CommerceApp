from django.test import Client
from datetime import datetime as dt, timedelta as td, timezone as tz
from .test_basesample import BaseTestSample
from myshop.models import Item


class CatalogTestingFilter(BaseTestSample):
    
    def setUp(self):
        super().setUp()
        
    def loadSampleDate(self): # TODO - issue with time testing here
        self.i1.time = dt.now() - td(days=3)
        self.i2.time = dt.now() - td(days=4.5)
        self.i3.time = dt.now() - td(days=8.2)
        self.i4.time = dt.now() - td(days=7.5)
        self.i5.time = dt.now() - td(days=1.7)
        self.i1.save()
        self.i2.save()
        self.i3.save()
        self.i4.save()
        self.i5.save()
        
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
        
    def test_index_filter_time_1(self):
        pass
        # TODO - issue with datetime testing here
        # self.i1.time = dt.now(tz.utc) - td(days=3)
        # self.i1.save()
        # for item in Item.objects.all():
        #     print(item.id)
        #     print(item.time)
        # print(self.i1.time)
        # self.loadSampleDate()
        # c = Client()
        # response = c.get("/catalog", { 'time': '2',})
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(list(response.context["pagination"].object_list),
        #                 [self.i2, self.i3, self.i4, self.i5])
