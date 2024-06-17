FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.2.2

LABEL course="" \
      author="" \
      description=""

ENV REFRESHED_AT 2023-04-14

# change to root if necessary
USER 0

WORKDIR /home/$NB_USER

USER $NB_UID

# Add course materials for each class
COPY --chown="${NB_USER}":"${NB_GID}" nbs .
COPY --chown="${NB_USER}":"${NB_GID}" classes .

# install required libraries
COPY --chown="${NB_USER}":"${NB_GID}" requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

## Add scripts and data
COPY --chown="${NB_USER}":"${NB_GID}" data /work/data
COPY --chown="${NB_USER}":"${NB_GID}" scripts /work/scripts
COPY --chown="${NB_USER}":"${NB_GID}" src /work/src
COPY --chown="${NB_USER}":"${NB_GID}" syllabus /work/syllabus

COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
