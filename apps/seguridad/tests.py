from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class SeguridadUrlsTests(TestCase):
    protected_urls = (
        ("inicio:inicio", {}),
        ("cliente:cliente_list", {}),
        ("cliente:cliente_create", {}),
        ("cliente:cliente_update", {"pk": 1}),
        ("cliente:cliente_delete", {"pk": 1}),
        ("habitacion:habitacion_list", {}),
        ("habitacion:habitacion_create", {}),
        ("habitacion:habitacion_update", {"pk": 1}),
        ("habitacion:habitacion_delete", {"pk": 1}),
        ("reserva:reserva_list", {}),
        ("reserva:reserva_create", {}),
        ("reserva:reserva_update", {"pk": 1}),
        ("reserva:reserva_delete", {"pk": 1}),
        ("actividad_turistica:actividad_turistica_list", {}),
        ("actividad_turistica:actividad_turistica_create", {}),
        ("actividad_turistica:actividad_turistica_update", {"pk": 1}),
        ("actividad_turistica:actividad_turistica_delete", {"pk": 1}),
        ("hotel:hotel_list", {}),
        ("hotel:hotel_create", {}),
        ("hotel:hotel_update", {"pk": 1}),
        ("hotel:hotel_delete", {"pk": 1}),
    )

    def test_protected_urls_redirect_anonymous_users_to_login(self):
        for route_name, kwargs in self.protected_urls:
            with self.subTest(route=route_name, kwargs=kwargs):
                url = reverse(route_name, kwargs=kwargs)
                response = self.client.get(url)

                self.assertEqual(response.status_code, 302)
                self.assertEqual(
                    response.url,
                    f"{reverse('seguridad:login')}?next={url}",
                )

    def test_login_and_logout_work(self):
        username = "seguridad-test"
        password = "StrongPassword123!"
        get_user_model().objects.create_user(
            username=username,
            password=password,
        )

        response = self.client.post(
            reverse("seguridad:login"),
            {"username": username, "password": password},
        )
        self.assertRedirects(response, reverse("inicio:inicio"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        response = self.client.post(reverse("seguridad:logout"))
        self.assertRedirects(response, reverse("seguridad:login"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
