import pytest
from unittest.mock import Mock, patch
from app.services.bot import Bot  # Assuming you have a Bot class in bot.py
from bot.app.handlers import handle_start, handle_help  # Assuming these handlers exist

@pytest.fixture
def bot():
    return Bot()

def test_bot_initialization(bot):
    assert isinstance(bot, Bot)

@patch('bot.services.bot.TelegramBot')
def test_bot_start(mock_telegram_bot, bot):
    bot.start()
    mock_telegram_bot.return_value.start_polling.assert_called_once()

def test_handle_start():
    mock_update = Mock()
    mock_context = Mock()
    result = handle_start(mock_update, mock_context)
    assert "Welcome to the Time Management Bot!" in result

def test_handle_help():
    mock_update = Mock()
    mock_context = Mock()
    result = handle_help(mock_update, mock_context)
    assert "Here are the available commands:" in result

@pytest.mark.parametrize("command,expected_handler", [
    ("/start", "handle_start"),
    ("/help", "handle_help"),
])
def test_command_handler_mapping(bot, command, expected_handler):
    handler = bot.get_handler(command)
    assert handler.__name__ == expected_handler

# @pytest.mark.integration
# def test_database_connection():
#     from bot.services.database import Databas
#     db = Database()
#     assert db.connect() == True

@pytest.mark.integration
def test_telegram_api_connection(bot):
    assert bot.test_telegram_connection() == True
