FROM dreg.cloud.sdu.dk/ucloud-apps/rstudio:4.4.1

LABEL course="" \
      author="" \
      description=""

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER 0

WORKDIR /home/${USERID}

## Add scripts and data
COPY --chown=${USERID}:${GROUPID} renv /work/renv
COPY --chown=${USERID}:${GROUPID} slides /work/slides

## Add entrypoint script
COPY --chown=${USERID}:${GROUPID} start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

COPY --chown=${USERID}:${GROUPID} req.sh /usr/bin/req
RUN chmod 755 /usr/bin/req

WORKDIR /work
