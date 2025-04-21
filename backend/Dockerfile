# Bun currently has an issue where it hangs docker builds
FROM python:3.13-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.config.settings

RUN uv venv
RUN uv sync --frozen

EXPOSE 8000
# Two workers for the sake of the 1-cored VM
CMD ["uv", "run", "gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]