FROM python:3.9-slim AS build-env

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# install requirements
COPY /api /api
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# :nonroot-amd64
# FROM gcr.io/distroless/python3:debug-amd64

# Copy virtual env from python-deps stage
# COPY --from=build-env /.venv /.venv
# COPY --from=build-env /api /api
ENV PATH="/.venv/bin:$PATH"

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "80"]
