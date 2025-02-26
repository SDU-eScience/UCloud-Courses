FROM dreg.cloud.sdu.dk/ucloud-apps/gromacs-te:2024.4

LABEL course="KE824: Biomolecular Simulations" \
      author="Himanshu Khandelia" \
      description="UCloud course app for 'KE824: Biomolecular Simulations' built on top of GROMACS."

## Use bash instead of sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /tmp

USER ${USERID}

RUN pip install --no-cache-dir matplotlib pandas

## Add entrypoint script
COPY --chown=$USER:$USER  start_course.sh /usr/bin/start_course
RUN chmod 755 /usr/bin/start_course

WORKDIR /work
