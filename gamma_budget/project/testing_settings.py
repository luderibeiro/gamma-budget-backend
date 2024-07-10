from .settings import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Use an in-memory SQLite database
        # Or specify a file path to a temporary SQLite database:
        # 'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    },
}
