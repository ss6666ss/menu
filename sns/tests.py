from django.test import TestCase

from django.contrib.auth.models import User
from .models import Group,Message

class SnsTests(TestCase):

    @classmethod 
    def setUpClass(cls):
        super().setUpClass()
        (usr, grp) = cls.create_user_and_group()
        cls.create_message(usr, grp)

    @classmethod
    def create_user_and_group(cls):
        User(username = "public", password = "p6u6b6l6i6c", is_staff = False, is_active = True).save()
        pb_usr = User.objects.filter(username = 'public').first()
        Group(title = 'public', owner_id = pb_usr.id).save
        pb_grp = Group.objects.filter(title = 'public').first()
        User(username = "test",password = "test", is_staff = True, is_active = True).save()
        usr = User.objects.filter(username = 'test').first()

        return (usr, pb_grp)

    def create_message(cls, usr, grp):
        Message(content = 'this is test message.', owner_id = usr.id, group_id = grp.id).save()
        Message(content = 'test', owner_id = usr.id, group_id = grp.id).save()
        Message(content = "ok", owner_id = usr.id, group_id = grp.id).save()
        Message(content = "ng", owner__id = usr.id, group_id = grp.id).save()
        Message(content = 'finish', owner_id = usr.id, group_id = grp.id).save()

    def test_check(self):
        usr = User.objects.filter(username = 'test').first()
        response = self.client.get(reverse('index'))
        self.assertIs(response.tatus_code, 302)

        self.client.force_login(usr)
        response = self.client.get(reverse('index'))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, 'this is test message.')