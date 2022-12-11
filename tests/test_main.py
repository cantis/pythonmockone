from app.core import main


def test_main():
    # arrange
    # mocker.patch.object("main.dependant_value", return_value=99)

    # act
    result = main.main()

    # assert
    assert result == '99'
