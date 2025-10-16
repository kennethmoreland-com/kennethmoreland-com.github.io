cmake_minimum_required(VERSION 3.30)

project(km_homepage NONE)

add_subdirectory(curriculum_vitae)

#################################
# Capture CV pdf and copy into cv submodule so it can be pushed
# to web page delivery.
#set(cv_target curriculum_vitae_pdf)
#get_target_property(cv_filename ${cv_target} OUTPUT_NAME)
set(cv_filename "${CMAKE_CURRENT_BINARY_DIR}/curriculum_vitae/curriculum_vitae.pdf")
set(cv_capture "${CMAKE_CURRENT_SOURCE_DIR}/cv/cv-kmoreland.pdf")
add_custom_command(OUTPUT ${cv_capture}
  MAIN_DEPENDENCY ${cv_filename}
  COMMAND ${CMAKE_COMMAND} -E copy ${cv_filename} ${cv_capture}
  COMMENT "Capturing CV PDF"
  )

add_custom_target(capture_cv ALL
  DEPENDS ${cv_capture}
  )

#################################
# Parse bibtex files to build publications page.
find_package(Python)

set_property(DIRECTORY APPEND PROPERTY
  CMAKE_CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/scripts/bib2md.py)

function(bib2md md_var bib_file)
  set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS ${bib_file})
  execute_process(
    COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/scripts/bib2md.py ${bib_file}
    OUTPUT_VARIABLE markdown
    ECHO_ERROR_VARIABLE
    RESULT_VARIABLE result
    )
  if(NOT "${result}" EQUAL 0)
    message(SEND_ERROR "Bib parser failed to run.")
  endif()
  set(${md_var} "${markdown}" PARENT_SCOPE)
endfunction()

if(Python_FOUND)
  bib2md(JOURNAL_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/journal.bib)
  bib2md(PHD_PUB ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/phd.bib)
  bib2md(WORKSHOP_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/workshop.bib)
  bib2md(NOPEER_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/nopeer.bib)
  bib2md(POSTER_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/poster.bib)
  bib2md(PRESENTATION_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/presentation.bib)
  bib2md(PANEL_PUBS ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/panel.bib)
  set(PUBS_COMMENT "DO NOT EDIT! This file generated from .bib files.")
  configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/scripts/publications.md.in
    ${CMAKE_CURRENT_SOURCE_DIR}/content/publications/index.md
    )

  set_property(DIRECTORY APPEND PROPERTY
    CMAKE_CONFIGURE_DEPENDS 
      ${CMAKE_CURRENT_SOURCE_DIR}/scripts/yaml2activities.py
      ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/professional-activities.yaml
    )
  execute_process(
    COMMAND ${Python_EXECUTABLE}
      ${CMAKE_CURRENT_SOURCE_DIR}/scripts/yaml2activities.py
      ${CMAKE_CURRENT_SOURCE_DIR}/curriculum_vitae/professional-activities.yaml
    OUTPUT_VARIABLE markdown
    ECHO_ERROR_VARIABLE
    RESULT_VARIABLE result
    )
  if(NOT "${result}" EQUAL 0)
    message(SEND_ERROR "YAML parser failed to run.")
  endif()
  file(WRITE
    ${CMAKE_CURRENT_SOURCE_DIR}/content/professional-activities/index.md
    ${markdown}
    )
else()
  message("Could not find Python. Skipping parsing bib and yaml files.")
endif()
