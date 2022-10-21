from app import main

def test_main(mocker):
    # arrange
    mocker.patch.object(main, "dependant_value", return_value=42)

    # act
    result = main.dependant_value()

    # assert
    assert result == 42

