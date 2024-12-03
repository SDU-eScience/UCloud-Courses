FROM dreg.cloud.sdu.dk/ucloud-apps/rstudio:4.4.1

LABEL course="RStudio Demo Course" \
      author="Jes Elgin Jensen, Rytis Mikutavicius, Mine Çetinkaya-Rundel" \
      description="Example RStudio-centered UCloud course based on based on Duke University's Statistical Science Introductory Data Science courses"

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /home/${USERID}

## Add environment files
COPY --chown=${USERID}:${GROUPID} renv /Renvironment/renv
COPY --chown=${USERID}:${GROUPID} .Rprofile /Renvironment/.Rprofile
COPY --chown=${USERID}:${GROUPID} renv.lock /Renvironment/renv.lock

## Add entrypoint script
COPY --chown=${USERID}:${GROUPID} start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
