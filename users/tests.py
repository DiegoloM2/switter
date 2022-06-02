from django.test import TestCase, Client
from django.contrib.auth import get_user_model


User = get_user_model()

class TestUserModel(TestCase):


    def test_create_user(self):
        user = User.objects.create_user (
            email = "test@whatev.com", 
            password = "test123"
        )

        self.assertEqual(user.email, "test@whatev.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email = "test@superuser.com", 
            password = "testsuperuser"
        )
        self.assertEqual(user.email, "test@superuser.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)


class TestCustomUserAdminSite(TestCase):

    #First, set up the data:
    def test_admin_sites(self):
        #Every test must have a request factory which creates a request with a valid superuser logged in:
        client = Client()
        
        
        superuser = User.objects.create_superuser(
            email = "adminTest@superuser.com", 
            password = "testsuperuser"
        )

        #Login the client with a superuser so that we can access the admin page.
        client.login(email=superuser.email, password="testsuperuser")



        # Test all user admin pages.
        admin_pages = [
            
            #Test main user site
            "/admin/users/customuser/",

            #Test change site
            f"/admin/users/customuser/{superuser.id}/change/",

            #Test add site
            "/admin/users/customuser/add/",
            
            #Test change password
            f"/admin/users/customuser/{superuser.id}/password/",  
            
            #Test search
            "/admin/users/customuser/?q=d"

        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200

            assert "<!DOCTYPE html" in str(resp.content)

