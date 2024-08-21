FROM dreg.cloud.sdu.dk/ucloud-apps/jupyter-base:4.2.4

LABEL course="Social Data Science 1" \
      author="Rolf Lyneborg Lund" \
      description="Social Data Science I is a foundational module designed to equip students with essential skills in social data science with a strong emphasis on Python programming and data analysis. The course introduces students to the fundamental principles and tools necessary for data science applications in social contexts. The curriculum is structured to provide a comprehensive introduction to Python, which is the primary tool used throughout the course. The course offers insights in three main areas: Python Basics and Data Handling, Data Cleaning and Management, and Data Visualization.\nStudents learn how to handle data within Python, including time-series and textual data, advancing to more complex data structures and problem-solving techniques.\nSessions on messy data theory and practical data cleaning cover the theoretical underpinnings and practical skills needed for scraping data and making API calls. The course emphasizes the importance of cleaning and organizing unstructured data from various sources.\nThe data visualization component of the course introduces the theoretical concepts and practical applications of visualizing data. This includes using specific visualization tools to create compelling graphical representations of data and network visualizations."

ENV REFRESHED_AT 2024-08-15

## Change to root if necessary
USER 0

WORKDIR /home/$NB_USER

## Install required libraries
RUN pip install --upgrade --no-cache-dir \
 && pip install --no-cache-dir \
      matplotlib \
      numpy \
      pandas \
      plotnine

## Add entrypoint script
COPY --chown="${NB_USER}":"${NB_GID}" start_course.sh /usr/bin/start_course

## Expose port 8888 for Jupyter Notebook
EXPOSE 8888

RUN chmod 755 /usr/bin/start_course

USER $NB_UID

WORKDIR /work
