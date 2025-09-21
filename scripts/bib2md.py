#!/usr/bin/env python3

import sys

# Note, this requires bibtexparser 2.0 or better.
import bibtexparser
import bibtexparser.middlewares

if (len(sys.argv) != 2):
  print(f'USAGE: {sys.argv[0]} <input>.bib')
  exit(1)

input_file = sys.argv[1]

layers = [
  bibtexparser.middlewares.SeparateCoAuthors(),
  bibtexparser.middlewares.SplitNameParts(),
  bibtexparser.middlewares.MonthLongStringMiddleware(),
  bibtexparser.middlewares.LatexDecodingMiddleware(),
]

primary_links = [
  'homeurl', 'url',
]
secondary_links = [
  'video', 'poster', 'slides',
]

bibdata = bibtexparser.parse_file(input_file, append_middleware=layers)

def write_name(file, bibname):
  name = ' '.join(bibname.first)
  if bibname.von:
    name += ' ' + ' '.join(bibname.von)
  name += ' ' + ' '.join(bibname.last)
  if bibname.jr:
    name += ' ' + ' '.join(bibname.jr)
  if (len(bibname.first) > 0) and (bibname.first[0][0] == 'K') and (bibname.last == ['Moreland']):
    file.write(f'**{name}**')
  else:
    file.write(name)

def write_authors(file, authors):
  if len(authors) == 1:
    write_name(file, authors[0])
  elif len(authors) == 2:
    write_name(file, authors[0])
    if (authors[1].last == ['others']):
      file.write(', _et al_')
    else:
      file.write(' and ')
      write_name(file, authors[1])
  else:
    for name in authors[:-1]:
      write_name(file, name)
      file.write(', ')
    if (authors[-1].last == ['others']):
      file.write('_et al_')
    else:
      file.write('and ')
      write_name(file, authors[-1])
  file.write('.\n')

def hyperlink(text, link=None):
  if link:
    return f'[{text}]({link})'
  else:
    return text

def replace_math(text):
  import re
  text = re.sub(r'\$\^(.+)\$', r'<sup>\1</sup>', text)
  return text

def write_title(file, entry):
  title = None
  if 'chapter' in entry:
    title = f'{entry["chapter"]}'
  else:
    title = f'{entry["title"]}'
  title = replace_math(title)
  link = None
  for plink in primary_links:
    if (not link) and (plink in entry):
      link = entry[plink]
  if (not link) and ('doi' in entry):
    link = f'https://dx.doi.org/{entry["doi"]}'
  for slink_name in secondary_links:
    slink = slink_name + 'url'
    if (not link) and (slink in entry):
      link = entry[slink]
  file.write('{{% pubtitle %}}')
  file.write(hyperlink(title, link))
  file.write('{{% /pubtitle %}}.\n')

# outf = open(output_tex, 'w')
outf = sys.stdout

for entry in bibdata.entries:
  write_title(outf, entry)
  if 'author' in entry:
    write_authors(outf, entry['author'])
  if 'journal' in entry:
    outf.write(f'_{entry["journal"]}_, ')
  elif 'booktitle' in entry:
    outf.write(f'In _{entry["booktitle"]}_, ')
  elif 'venue' in entry:
    outf.write(f'_{entry["venue"]}_, ')
  elif entry.entry_type == 'inbook':
    outf.write(f'_{entry["title"]}_, ')
  if entry.entry_type == 'techreport':
    outf.write('Technical Report ')
  if entry.entry_type == 'phdthesis':
    outf.write(f'PhD thesis, {entry["school"]}, ')
  if 'publisher' in entry:
    outf.write(f'{entry["publisher"]}, ')
  if 'number' in entry:
    outf.write(f'{entry["number"]}, ')
  if 'institution' in entry:
    outf.write(f'{entry["institution"]}, ')
  if 'howpublished' in entry:
    outf.write(f'_{entry["howpublished"]}_, ')
  if 'volume' in entry:
    outf.write(f'{entry["volume"]}')
    if 'number' in entry:
      outf.write(f'({entry["number"]})')
    if 'pages' in entry:
      outf.write(f':{entry["pages"]}')
    outf.write(', ')
  elif 'pages' in entry:
    outf.write(f'pages {entry['pages']}')
    outf.write(', ')
  if 'month' in entry:
    outf.write(f'{entry["month"]} ')
    if 'day' in entry:
      outf.write(f'{entry["day"]}, ')
  outf.write(f'{entry["year"]}.\n')
  if 'note' in entry:
    outf.write(f'{entry["note"]}.\n')
  if 'doi' in entry:
    outf.write(hyperlink(f'doi:{entry["doi"]}', f'https://dx.doi.org/{entry["doi"]}'))
    outf.write('.\n')
  if 'isbn' in entry:
    outf.write(f'ISBN:{entry["isbn"]}.\n')
  found_main_link = False
  for plink in primary_links:
    if plink in entry:
      found_main_link = True
  for slink_name in secondary_links:
    slink = slink_name + 'url'
    if slink in entry:
      if found_main_link:
        outf.write(f'<small>([{slink_name}]({entry[slink]}))</small>\n')
      else:
        found_main_link = True
  outf.write('\n')
