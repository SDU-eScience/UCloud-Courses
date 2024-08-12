FROM dreg.cloud.sdu.dk/ucloud-apps/rstudio:4.4.1

LABEL course="" \
      author="" \
      description=""

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER 0

USER ${NB_USER}

WORKDIR /home/$NB_USER

## Add scripts and data
COPY --chown="${NB_USER}":"${NB_GID}" renv /work/renv
COPY --chown="${NB_USER}":"${NB_GID}" slides /work/slides

## Add entrypoint script
COPY --chown=${NB_USER}:${NB_GID} start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
