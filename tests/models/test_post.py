import pytest

from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title="pyteste with factory")


@pytest.mark.django_db
def teste_create_published_post(post_published):
    assert post_published.title == "pytest with factory"