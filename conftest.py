from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright

from prego_model.prego import Prego


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def final_project(get_playwright):
    prego = Prego(get_playwright)
    yield prego
    prego.close()