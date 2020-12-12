import pytest
import model

def test_text_objects():
    assert model.Button().create_text_objects("Test Text", pygame.font.SysFont("comicsansms", 30))
    
def test_user_score():
    assert model.HealthfyModel().user_score == 5