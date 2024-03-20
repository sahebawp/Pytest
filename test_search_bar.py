
import pytest
from selenium import webdriver


class TestSearch():

    @pytest.fixture
    def browser(self):
        self.setup()
        yield
        self.teardown()
