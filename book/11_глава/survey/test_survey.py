import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """Опрос который будет доступен для всех функций тестирования."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey
    
def test_store_single_response(language_survey):
    """Проверяет, что один ответ сохранен правильно."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Проверяет, что три ответа были сохранены правильно."""
    resposes = ['English', 'Spanish', 'Mandarin']
    for response in resposes:
        language_survey.store_response(response)

    for response in resposes:
        assert response in language_survey.responses