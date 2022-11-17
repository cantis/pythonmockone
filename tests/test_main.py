from app.core.main import dependant_value, main


def test_main(mocker):
    # arrange
    mocker.patch("dependant_value", return_value=99)

    # act
    result = main.main()

    # assert
    assert result == '99'
