FROM homeassistant/home-assistant:beta

RUN mkdir -p /config
COPY configuration.yaml /config

EXPOSE 8123

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash
