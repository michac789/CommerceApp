from django.test import Client

from myshop.models import Item
from cart.models import Bookmark, Cart
from catalog.tests import BaseTestSample


class APIBookmarkTest(BaseTestSample):
    
    def setUp(self):
        super().setUp()
        self.book1 = Bookmark.objects.create(
            item=self.i1, user=self.user1,
        )
        self.book2 = Bookmark.objects.create(
            item=self.i3, user=self.user2,
        )
        self.book3 = Bookmark.objects.create(
            item=self.i5, user=self.user1,
        )
        
    def test_api_bookmark_1(self):
        c = Client()
        response = c.get("/api/bookmark/0")
        self.assertEqual(response.status_code, 302)
        
    def test_api_bookmark_2(self):
        c = Client()
        c.login(username="user1", password="123")
        response = c.get("/api/bookmark/0")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            [self.book1.serialize(), self.book3.serialize()],
        )
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 2
        )

    def test_api_bookmark_3(self):
        c = Client()
        c.login(username="user1", password="123")
        response1 = c.put("/api/bookmark/1")
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 2
        )
        response2 = c.put("/api/bookmark/2")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 3
        )
        
    def test_api_bookmark_4(self):
        c = Client()
        c.login(username="user1", password="123")
        response1 = c.put("/api/bookmark/6")
        self.assertEqual(response1.status_code, 404)
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 2
        )
        
    def test_api_bookmark_5(self):
        c = Client()
        c.login(username="user1", password="123")
        response1 = c.delete("/api/bookmark/1")
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 1
        )
        response2 = c.delete("/api/bookmark/2")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(
            Bookmark.objects.filter(user=self.user1).count(), 1
        )
        response3 = c.get("/api/bookmark/0")
        self.assertEqual(response3.status_code, 200)
        self.assertJSONEqual(
            response3.content, [self.book3.serialize()],
        )


class APICartTest(BaseTestSample):
    
    def setUp(self):
        super().setUp()
        self.cart1 = Cart.objects.create(
            item=self.i1, user=self.user2,
        )
        self.cart2 = Cart.objects.create(
            item=self.i2, user=self.user2,
        )
        self.cart3 = Cart.objects.create(
            item=self.i4, user=self.user1,
        )
        
    def test_api_cart_1(self):
        c = Client()
        response = c.get("/api/cart/1")
        self.assertEqual(response.status_code, 302)

    def test_api_cart_2(self):
        c = Client()
        c.login(username="user1", password="123")
        response1 = c.get("/api/cart/0")
        self.assertEqual(response1.status_code, 200)
        self.assertJSONEqual(
            response1.content, [self.cart3.serialize()],
        )
        self.assertEqual(
            Cart.objects.filter(user=self.user1).count(), 1
        )
        response2 = c.put("/api/cart/5")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(
            Cart.objects.filter(user=self.user1).count(), 2
        )
        
    def test_api_cart_3(self):
        c = Client()
        c.login(username="user2", password="123")
        response = c.put("/api/cart/0")
        self.assertEqual(response.status_code, 404)
        
    def test_api_cart_4(self):
        c1 = Client()
        c1.login(username="user2", password="123")
        response = c1.put("/api/cart/5")
        self.assertEqual(response.status_code, 400)
        c2 = Client()
        c2.login(username="user2", password="123")
        Item.objects.create(
            title="t6", description="", price=999,
            category=self.c3, seller=self.user1, closed=True
        )
        response = c2.put("/api/cart/6")
        self.assertEqual(response.status_code, 400)
        
    def test_api_cart_5(self):
        c = Client()
        c.login(username="user2", password="123")
        response1 = c.delete("/api/cart/1")
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(
            Cart.objects.filter(user=self.user1).count(), 1
        )
        response2 = c.delete("/api/cart/2")
        self.assertEqual(response2.status_code, 200)
        response3 = c.get("/api/cart/0")
        self.assertEqual(response3.status_code, 200)
        self.assertJSONEqual(
            response3.content, [],
        )
