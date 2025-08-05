cmake_minimum_required(VERSION 3.30)

project(km_homepage NONE)

add_subdirectory(curriculum_vitae)

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
  configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/scripts/publications.md.in
    ${CMAKE_CURRENT_SOURCE_DIR}/content/publications/index.md
    )
else()
  message("Could not find Python. Skipping parsing bib files.")
endif()
