# Using an official Python image as the base
FROM python:3.10-slim

# Defining variables for app path and user/group
ENV APP_HOME=/app
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV USER_NAME=django_user
ENV USER_UID=1000
ENV USER_GID=1000

# Installing system dependencies for Poetry and PostgreSQL 
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID --create-home $USER_NAME


# Install poetry via curl (may take a while...)
RUN echo "Installing Poetry via curl, this may take a while..." \
    && sleep 2 \
    && curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4

# Setting the working directory for the app
WORKDIR $APP_HOME

# Copying the entire project before installing dependencies
COPY . $APP_HOME

# Making the "commands.sh" script executable
RUN chmod +x $APP_HOME/docker-scripts/commands.sh

# Installing dependencies with Poetry, without creating a virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Exposing the app port
EXPOSE 8000

# Change ownership of the app directory to non-root user
RUN chown -R $USER_NAME:$USER_NAME $APP_HOME

# Switch to non-root user
USER $USER_NAME

# Command to start the script that will execute setup commands and start the server
CMD ["/app/docker-scripts/commands.sh"]
