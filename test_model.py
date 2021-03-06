import pytest
import model


game_model = model.HealthfyModel()

status_cases = [(40, model.red, game_model.feeding_status, game_model.feed),
                (30, model.black, game_model.feeding_status, game_model.feed),
                (18, model.red, game_model.sleeping_status, game_model.sleep),
                (12, model.black, game_model.sleeping_status, game_model.sleep),
                (25, model.red, game_model.working_status, game_model.work),
                (39, model.black, game_model.working_status, game_model.work),
                (6, model.red, game_model.socializing_status, game_model.talk),
                (20, model.black, game_model.socializing_status, game_model.talk),
                (32, model.red, game_model.bathroom_status, game_model.potty),
                (23, model.black, game_model.bathroom_status, game_model.potty),
                (23, model.black, game_model.bathroom_status, game_model.potty),
                (3, model.black, game_model.bathroom_status, game_model.bomb),
                ] # Test cases to check time, color, status and button


@pytest.mark.parametrize("time, color, status, button", status_cases)
def test_feeding_status(time, color, status, button):
    game_model.timer_sec = time
    status()
    assert button.current_color == color
