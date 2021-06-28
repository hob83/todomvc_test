from typing import Literal

import pydantic


EnvContent = Literal['local', 'stage', 'prod']
BrowserName = Literal['chrome', 'firefox']


class Settings(pydantic.BaseSettings):

    context: EnvContent = 'local'

    browser_name: BrowserName = 'firefox'  # or 'chrome'
    browser_quit_after_each_test: bool = False
    headless: bool = False


settings = Settings(_env_file=f'config.{Settings().context}.env')
