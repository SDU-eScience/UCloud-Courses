FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.4.3

LABEL course="" \
      author="" \
      description=""

ENV REFRESHED_AT 2023-04-14

# change to root if necessary
USER 0

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      rar \
      unrar \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /home/$NB_USER

USER $NB_UID

COPY --chown="${NB_USER}":"${NB_GID}" requirements.txt .

RUN pip install --upgrade pip --no-cache-dir \
 && pip install -r requirements.txt --no-cache-dir

## Add entrypoint script
COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
