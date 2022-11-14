from app.core.main import dependant_value

def test_main(mocker):
    # arrange
    mocker.patch("dependant_value", return_value=42)


    # act
    result = dependant_value()
    # assert
    assert result == 42

