import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_exercicio_modulo_8(client):
    url = reverse('exercicio')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Exercicio Modulo 8 Resolvido'