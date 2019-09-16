#!/usr/bin/env bash
curl -X POST \
  http://localhost/v1/job_parser \
  -H 'Content-Type: application/json' \
  -d '{
	"title": "Geography Teacher",
	"description": "Forde Education are looking to recruit a Teacher of Geography for an immediate start in a Doncaster Secondary school.   The school has a thriving and welcoming environment with very high expectations of students both in progress and behaviour. This position will be working until Easter with a likely extension until July 2011.   The successful candidates will need to demonstrate good practical subject knowledge  but also possess the knowledge and experience to teach to GCSE level with the possibility of teaching to A’Level to smaller groups of students.   All our candidate will be required to hold a relevant teaching qualifications with QTS  successful applicants will be required to provide recent relevant references and undergo a Enhanced CRB check.   To apply for this post or to gain information regarding similar roles please either submit your CV in application or Call Debbie Slater for more information."
}'