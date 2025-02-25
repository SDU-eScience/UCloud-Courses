FROM dreg.cloud.sdu.dk/ucloud-apps/gromacs-te:2024.4

LABEL course="KE824: Biomolecular Simulations" \
      author="Himanshu Khandelia" \
      description=""

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER 0

WORKDIR /home/$USER

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
      git-lfs \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* 

USER ${USERID}

RUN pip install --no-cache-dir matplotlib pandas

## Add entrypoint script
COPY --chown=$USER:$USER  start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
