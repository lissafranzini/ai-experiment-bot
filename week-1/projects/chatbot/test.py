from unittest.mock import patch, MagicMock
from config import MODEL, SYSTEM_INSTRUCTION, TEMPERATURE
from chatbot import Chatbot 


def test_model_is_set():
    assert MODEL is not None
    assert isinstance(MODEL, str)

def test_temperature_is_valid():
    assert isinstance(TEMPERATURE, float)
    assert 0.0 <= TEMPERATURE <= 2.0

def test_system_instruction_is_set():
    assert SYSTEM_INSTRUCTION is not None
    assert len(SYSTEM_INSTRUCTION) > 0

def test_conversation_starts_empty():
    bot = Chatbot()
    assert bot.chat_history == []

def test_clear_history():
    bot = Chatbot()
    bot.chat_history = ["message"]
    bot.clear_history()
    assert bot.chat_history == []

def test_help():
    bot = Chatbot()
    result = bot.process_input("help")
    assert result == "help"

def test_process_input_sends_message_to_ai():
    bot = Chatbot()
    
    fake_response = MagicMock()
    fake_response.text = "Hello! I'm a fake AI response."
    
#Temporarily replaces the actual ai client with my mock
    with patch("chatbot.ai_client", return_value=fake_response) as mock_ai:
        result = bot.process_input("Hi there")
    
    assert result == "Hello! I'm a fake AI response."
    

    mock_ai.assert_called_once()
    
    assert len(bot.chat_history) == 2  
    assert bot.chat_history[0]["role"] == "user"
    assert bot.chat_history[1]["role"] == "model"