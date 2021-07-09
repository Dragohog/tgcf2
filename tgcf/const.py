"""Declare all global constants."""

COMMANDS = {
    "start": "Проверьте, жив ли я",
    "forward": "Добавить новый источник",
    "remove": "Удалить существующий источник",
    "help": "Помощь",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.yml"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"


class BotMessages:
    """Messages given by the bot to users."""

    # pylint: disable=too-few-public-methods
    start = "Привет! Я жив"
    bot_help = "В процессе.."
