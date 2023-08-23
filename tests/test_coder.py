import pytest

from comprehensive_microservice.coder import DataCoder, DataModel


@pytest.fixture()
def data_coder():
    return DataCoder()


@pytest.fixture()
def first_data():
    return DataModel(title="my first data", text="some text")


@pytest.fixture()
def second_data():
    return DataModel(title="my second data", text="another text")


class TestCase:
    def test_coder_saves(self, data_coder: DataCoder, first_data: DataModel):
        code = data_coder.save(first_data)
        assert code

    def test_coder_gets(self, data_coder: DataCoder, first_data: DataModel):
        code = data_coder.save(first_data)
        restored_data = data_coder.get(code)

        assert restored_data is not first_data
        assert restored_data == first_data

    def test_coder_different_codes(self, data_coder: DataCoder, first_data: DataModel):
        code_1 = data_coder.save(first_data)
        code_2 = data_coder.save(first_data)

        assert code_1 != code_2

    def test_multiple_texts(
        self, data_coder: DataCoder, first_data: DataModel, second_data: DataModel
    ):
        code_1 = data_coder.save(first_data)
        code_2 = data_coder.save(second_data)

        assert code_1 != code_2
        assert data_coder.get(code_1) == first_data
        assert data_coder.get(code_2) == second_data

    def test_coder_code_format(self, data_coder: DataCoder, first_data: DataModel):
        code = data_coder.save(first_data)
        assert code.isalnum()

    def test_coder_raises_if_no_code(self, data_coder: DataCoder):
        with pytest.raises(KeyError):
            data_coder.get("unknownkey")
