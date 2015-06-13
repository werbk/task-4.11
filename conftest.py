import pytest
import logging

from fixture.TestBase import BaseClass
from fixture.variables import UserLogin


fixture = None


@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        fixture = BaseClass()

    else:
        if not fixture.is_valid():
            fixture = BaseClass()

    fixture.session.ensure_login(UserLogin.name, UserLogin.password)
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):

    def fin():
        fixture.session.ensure_logout()
        fixture.restore()
    request.addfinalizer(fin)
    return fixture


