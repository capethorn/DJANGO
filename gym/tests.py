from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker
from django.contrib.auth.models import User
from django.utils import timezone

from gym.models import (
    Subscription, Option, OptionToSubscription, 
    AppointmentCoach, AppointmentGroup, Additionally, Addres
)

class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        subscription = Subscription.objects.create(
            name="Месячная",
            price=1500,
        )
        r = self.client.get("/api/subscription/")
        data = r.json()

        assert subscription.name == data[0]['name']
        assert subscription.id == data[0]['id']
        assert subscription.price == data[0]['price']
        assert len(data) == 1

    def test_create_subscription(self):
        r = self.client.post("/api/subscription/", data={
            "name": "Годовая",
            "price": 12000
        })

        new_id = r.json()['id']
        subscriptions = Subscription.objects.all()
        assert len(subscriptions) == 1

        new_sub = Subscription.objects.filter(id=new_id).first()
        assert new_sub.name == "Годовая"
        assert new_sub.price == 12000

    def test_delete_subscription(self):
        subscriptions = baker.make("gym.Subscription", 10)
        r = self.client.get('/api/subscription/')
        data = r.json()
        assert len(data) == 10

        id_to_delete = subscriptions[3].id
        self.client.delete(f'/api/subscription/{id_to_delete}/')

        r = self.client.get('/api/subscription/')
        data = r.json()
        assert len(data) == 9
        assert id_to_delete not in [i['id'] for i in data]

    def test_update_subscription(self):
        subscriptions = baker.make("gym.Subscription", 10)
        sub: Subscription = subscriptions[2]

        r = self.client.put(f'/api/subscription/{sub.id}/', {
            "name": "Обновленная подписка",
            "price": 9999
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/subscription/{sub.id}/')
        data = r.json()
        assert data['name'] == "Обновленная подписка"
        assert data['price'] == 9999

        sub.refresh_from_db()
        assert sub.name == data['name']


class OptionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        option = Option.objects.create(name="Бассейн")
        r = self.client.get("/api/option/")
        data = r.json()

        assert option.name == data[0]['name']
        assert len(data) == 1

    def test_create_option(self):
        r = self.client.post("/api/option/", data={"name": "Сауна"})
        new_id = r.json()['id']
        
        options = Option.objects.all()
        assert len(options) == 1
        
        new_option = Option.objects.filter(id=new_id).first()
        assert new_option.name == "Сауна"

    def test_delete_option(self):
        options = baker.make("gym.Option", 5)
        id_to_delete = options[1].id
        self.client.delete(f'/api/option/{id_to_delete}/')

        r = self.client.get('/api/option/')
        data = r.json()
        assert len(data) == 4
        assert id_to_delete not in [i['id'] for i in data]

    def test_update_option(self):
        options = baker.make("gym.Option", 3)
        opt: Option = options[1]

        r = self.client.put(f'/api/option/{opt.id}/', {"name": "Массаж"})
        assert r.status_code == 200

        opt.refresh_from_db()
        assert opt.name == "Массаж"


class OptionToSubscriptionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        link = baker.make("gym.OptionToSubscription")
        r = self.client.get("/api/option-to-subscription/")
        data = r.json()
        
        assert link.subscription.id == data[0]['subscription']
        assert link.option.id == data[0]['option']
        assert len(data) == 1

    def test_create_link(self):
        sub = baker.make("gym.Subscription")
        opt = baker.make("gym.Option")
        
        r = self.client.post("/api/option-to-subscription/", data={
            "subscription": sub.id,
            "option": opt.id
        })
        new_id = r.json()['id']
        
        links = OptionToSubscription.objects.all()
        assert len(links) == 1
        new_link = OptionToSubscription.objects.get(id=new_id)
        assert new_link.subscription == sub
        assert new_link.option == opt

    def test_delete_link(self):
        links = baker.make("gym.OptionToSubscription", 4)
        id_to_delete = links[0].id
        self.client.delete(f'/api/option-to-subscription/{id_to_delete}/')

        r = self.client.get('/api/option-to-subscription/')
        assert len(r.json()) == 3

    def test_update_link(self):
        links = baker.make("gym.OptionToSubscription", 2)
        link: OptionToSubscription = links[0]
        new_opt = baker.make("gym.Option")

        r = self.client.put(f'/api/option-to-subscription/{link.id}/', {
            "subscription": link.subscription.id,
            "option": new_opt.id
        })
        assert r.status_code == 200

        link.refresh_from_db()
        assert link.option.id == new_opt.id


class AppointmentCoachTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        appointment = baker.make("gym.AppointmentCoach")
        r = self.client.get("/api/appointment-coach/")
        data = r.json()

        assert appointment.coach.id == data[0]['coach']
        assert appointment.user.id == data[0]['user']
        assert len(data) == 1

    def test_create_appointment(self):
        coach = baker.make(User)
        user = baker.make(User)
        now = timezone.now()

        r = self.client.post("/api/appointment-coach/", data={
            "coach": coach.id,
            "user": user.id,
            "data": now.isoformat()
        })
        
        new_id = r.json()['id']
        appointments = AppointmentCoach.objects.all()
        assert len(appointments) == 1

    def test_delete_appointment(self):
        appointments = baker.make("gym.AppointmentCoach", 5)
        id_to_delete = appointments[2].id
        self.client.delete(f'/api/appointment-coach/{id_to_delete}/')

        r = self.client.get('/api/appointment-coach/')
        assert len(r.json()) == 4

    def test_update_appointment(self):
        appointments = baker.make("gym.AppointmentCoach", 2)
        appt: AppointmentCoach = appointments[0]
        new_coach = baker.make(User)

        r = self.client.put(f'/api/appointment-coach/{appt.id}/', {
            "coach": new_coach.id,
            "user": appt.user.id,
            "data": timezone.now().isoformat()
        })
        assert r.status_code == 200

        appt.refresh_from_db()
        assert appt.coach.id == new_coach.id


class AppointmentGroupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        group = baker.make("gym.AppointmentGroup", name="Йога", capacity=10, type="Групповая")
        r = self.client.get("/api/appointment-group/")
        data = r.json()

        assert group.name == data[0]['name']
        assert group.capacity == data[0]['capacity']
        assert len(data) == 1

    def test_create_group(self):
        r = self.client.post("/api/appointment-group/", data={
            "name": "Кроссфит",
            "capacity": 15,
            "type": "Силовая"
        })
        assert len(AppointmentGroup.objects.all()) == 1

    def test_delete_group(self):
        groups = baker.make("gym.AppointmentGroup", 3)
        self.client.delete(f'/api/appointment-group/{groups[0].id}/')
        
        r = self.client.get('/api/appointment-group/')
        assert len(r.json()) == 2

    def test_update_group(self):
        groups = baker.make("gym.AppointmentGroup", 2)
        group: AppointmentGroup = groups[0]

        r = self.client.put(f'/api/appointment-group/{group.id}/', {
            "name": "Новое название",
            "capacity": 20,
            "type": group.type
        })
        assert r.status_code == 200

        group.refresh_from_db()
        assert group.name == "Новое название"


class AdditionallyTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        add = Additionally.objects.create(name="Полотенце")
        r = self.client.get("/api/additionally/")
        assert r.json()[0]['name'] == add.name

    def test_create_additionally(self):
        self.client.post("/api/additionally/", data={"name": "Вода"})
        assert len(Additionally.objects.all()) == 1

    def test_delete_additionally(self):
        adds = baker.make("gym.Additionally", 3)
        self.client.delete(f'/api/additionally/{adds[0].id}/')
        assert len(Additionally.objects.all()) == 2

    def test_update_additionally(self):
        adds = baker.make("gym.Additionally", 2)
        self.client.put(f'/api/additionally/{adds[0].id}/', {"name": "Снек"})
        adds[0].refresh_from_db()
        assert adds[0].name == "Снек"


class AddresTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        addr = Addres.objects.create(addres="ул. Ленина 1")
        r = self.client.get("/api/addres/")
        assert r.json()[0]['addres'] == addr.addres

    def test_create_addres(self):
        self.client.post("/api/addres/", data={"addres": "ул. Пушкина 2"})
        assert len(Addres.objects.all()) == 1

    def test_delete_addres(self):
        addrs = baker.make("gym.Addres", 3)
        self.client.delete(f'/api/addres/{addrs[0].id}/')
        assert len(Addres.objects.all()) == 2

    def test_update_addres(self):
        addrs = baker.make("gym.Addres", 2)
        self.client.put(f'/api/addres/{addrs[0].id}/', {"addres": "Новый адрес"})
        addrs[0].refresh_from_db()
        assert addrs[0].addres == "Новый адрес"