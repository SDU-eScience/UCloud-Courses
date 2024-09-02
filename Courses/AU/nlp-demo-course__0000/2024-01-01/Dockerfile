FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.2.4

LABEL course="NLP Demo Course" \
      author="Jes Elgin Jensen, Rytis Mikutavicius & Roberta Rocca" \
      description="Example UCloud course based on the 2023 course Natural Language Processing taken as part of the MSc in Cognitive Science at Aarhus University. "

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
COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course

EXPOSE 8888

RUN chmod 755 /usr/bin/start_course

USER $NB_UID

WORKDIR /work
