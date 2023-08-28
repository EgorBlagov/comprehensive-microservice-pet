from pytest_mock import MockerFixture

from comprehensive_microservice.utils import single_call


def test_multiple_calls_return_same_object(mocker: MockerFixture):
    @single_call
    def f():
        return mocker.MagicMock()

    first_call = f()
    second_call = f()
    assert first_call is second_call


def test_multiple_calls_preserve_none(mocker: MockerFixture):
    counter = mocker.MagicMock()

    @single_call
    def f():
        counter()
        return None

    assert f() is None
    assert f() is None
    assert counter.call_count == 1
