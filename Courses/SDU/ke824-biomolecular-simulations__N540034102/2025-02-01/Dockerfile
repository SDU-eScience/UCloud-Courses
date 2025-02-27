FROM dreg.cloud.sdu.dk/ucloud-apps/gromacs-te:2024.4

LABEL course="KE824: Biomolecular Simulations" \
      author="Himanshu Khandelia" \
      description="UCloud course app for 'KE824: Biomolecular Simulations' built on top of GROMACS."

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER 0 

WORKDIR /tmp 

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      file \
      # Install packages to inflate RAR archives
      rar \
      unrar \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

USER ${USERID}

ENV PATH=$HOME/.local/bin:$PATH

RUN pip install --no-cache-dir matplotlib pandas 


## Add entrypoint script
COPY --chown=$USER:$USER  start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
