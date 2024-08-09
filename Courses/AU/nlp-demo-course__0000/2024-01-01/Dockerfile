FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.2.4

LABEL course="" \
      author="" \
      description=""

ENV REFRESHED_AT=2024-08-07

# change to root if necessary
USER 0

WORKDIR /home/$NB_USER

# install required libraries
COPY --chown="${NB_USER}":"${NB_GID}" requirements.txt .

RUN pip install --upgrade pip==24.2 --no-cache-dir \
 && pip install -r requirements.txt --no-cache-dir
 
## Add scripts and data
COPY --chown="${NB_USER}":"${NB_GID}" data /work/data
COPY --chown="${NB_USER}":"${NB_GID}" scripts /work/scripts
COPY --chown="${NB_USER}":"${NB_GID}" src /work/src
COPY --chown="${NB_USER}":"${NB_GID}" syllabus /work/syllabus
COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course.sh

EXPOSE 8080

RUN chmod 755 /usr/bin/start_course.sh

USER $NB_UID

WORKDIR /work
