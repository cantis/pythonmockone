import pytest

from app.core import main


def test_main(mocker):
    # arrange
    mocker.patch("app.core.main.dependant_value", return_value=99)

    # act
    result = main.main()

    # assert
    assert result == '99'
