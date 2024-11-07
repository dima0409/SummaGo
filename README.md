
# Api сервиса SummaGo для транскрипции и суммаризации видео

## Описание


Этот инструмент предназначен для анализа видеофайлов. Сервис использует различные библиотеки для анализа и обработки видеофайлов.
## Функциональность
- Получения списка всех видеофайлов из Яндекс.Диск.
- Загрузка видеофайла из облака пользователя.
- Обработка видео и его конвертация в аудио.
- Транскрипция и дальнейшая суммаризация.

## Библиотеки
В коде используются библиотеки:
 - aiohappyeyeballs  
 - aiohttp  
 - aiosignal  
 - alembic  
 - amqp  
 - annotated-types  
 - anyio  
 - asyncpg  
 - attrs  
 - billiard  
 - celery  
 - certifi  
 - charset-normalizer  
 - click  
 - click-didyoumean  
 - click-plugins  
 - click-repl  
 - colorama  
 - decorator  
 - fastapi  
 - filelock  
 - frozenlist  
 - fsspec  
 - greenlet  
 - h11  
 - idna  
 - imageio  
 - imageio-ffmpeg  
 - Jinja2   
 - kombu   
 - llvmlite   
 - Mako   
 - MarkupSafe   
 - more-itertools  
 - moviepy   
 - mpmath   
 - multidict   
 - networkx  
 - numba   
 - numpy  
 - openai-whisper   
 - pillow   
 - proglog   
 - prompt_toolkit   
 - propcache  
  - pydantic   
  - pydantic-settings   
  - pydantic_core   
  - pydub  
  - python-dateutil   
  - python-dotenv   
  - regex   
  - requests   
  - setuptools   
  - six
  - sniffio   
  - SQLAlchemy   
  - sqlmodel   
  - starlette   
  - sympy   
  - tiktoken  
  - torch   
  - tqdm   
  - typing_extensions   
  - tzdata   
  - urllib3   
  - uvicorn   
  - vine 
  - wcwidth   
  - yarl  
  -  redis   
  - psycopg   
  - nltk

## Установка
Для начала работы склонируйте репозиторий:
```shell
git clone https://github.com/dima0409/SummaGo
```
Перейдите в папку ```api```
```shell
cd api
```
Запустите docker compose
```shell
docker-compose up
```
Сервис будет доступен по адресу:
```
http://127.0.0.1:8000/api/v1/docs
```
## Важно
Во время тестирования не используйте Swagger. Из-за наличия ошибки [#612](https://github.com/fastapi/fastapi/issues/612) Swagger не обрабатывает Auth хедер. Рекомендуется использовать другие api клиенты.
