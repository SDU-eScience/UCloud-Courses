FROM dreg.cloud.sdu.dk/ucloud-apps/rstudio:4.4.1

LABEL course="RStudio Demo Course" \
      author="Jes Elgin Jensen, Rytis Mikutavicius, Mine Çetinkaya-Rundel" \
      description="Example RStudio-centered UCloud course based on based on Duke University's Statistical Science Introductory Data Science courses"

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER 0

RUN apt-get update -qq \
 && install2.r --error --deps TRUE \
    janitor \
    plotly \
 && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

USER $USERID

## Add entrypoint script
COPY --chown=${USERID}:${GROUPID} start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
