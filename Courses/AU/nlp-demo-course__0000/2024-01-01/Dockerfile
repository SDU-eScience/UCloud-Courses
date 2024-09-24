FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.2.4

LABEL course="NLP Demo Course" \
      author="Jes Elgin Jensen, Rytis Mikutavicius & Roberta Rocca" \
      description="Example JupyterLab-centered UCloud course based on the 2023 course Natural Language Processing taken as part of the MSc in Cognitive Science at Aarhus University."

ENV REFRESHED_AT=2024-08-07

USER $NB_UID

WORKDIR /home/$NB_USER

# install required libraries
COPY --chown="${NB_USER}":"${NB_GID}" requirements.txt .

RUN pip install --upgrade pip --no-cache-dir \
 && pip install -r requirements.txt --no-cache-dir
 
## Add scripts and data
COPY --chown="${NB_USER}":"${NB_GID}" data /tmp/data
COPY --chown="${NB_USER}":"${NB_GID}" scripts /tmp/scripts
COPY --chown="${NB_USER}":"${NB_GID}" src /tmp/src
COPY --chown="${NB_USER}":"${NB_GID}" syllabus /tmp/syllabus
COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course

EXPOSE 8888

RUN chmod 755 /usr/bin/start_course

WORKDIR /work
