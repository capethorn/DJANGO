from django.test import TestCase
from rest_framework.test import APIClient
from gym.models import Subscription
from model_bakery import baker


class SubscriptionViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    
    def test_get_list(self):

        sub = baker.make("Subscription")        
        
        
        r = self.client.get('/api/subscription/')
        data = r.json()
        print(data)

        assert sub.name == data[0]['name']
        assert sub.price == data[0]['price']
        assert len(data) == 1 


    # def test_create_student(self):
    #     r =  self.client.post("/api/subscription/",{
    #         "name": "Подписка",
    #         "price": "цена"
    #     })

   
    #     subs = Subscription.objects.all()
    #     assert len(subs) == 1

    #     Subscription.objects.filter(id=id)
 