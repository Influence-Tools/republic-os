---
type: Jurisdiction
title: "Mesa County, CO"
classification: county
fips: "08077"
state: "CO"
demographics:
  population: 158601
  population_under_18: 32410
  population_18_64: 92779
  population_65_plus: 33412
  median_household_income: 73658
  poverty_rate: 10.72
  homeownership_rate: 72.47
  unemployment_rate: 5.42
  median_home_value: 378600
  gini_index: 0.444
  vacancy_rate: 5.92
  race_white: 130703
  race_black: 995
  race_asian: 1424
  race_native: 1327
  hispanic: 24519
  bachelors_plus: 48372
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/54"
    rel: in-district
    area_weight: 0.9797
  - to: "us/states/co/districts/house/55"
    rel: in-district
    area_weight: 0.0202
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Mesa County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 158601 |
| Under 18 | 32410 |
| 18–64 | 92779 |
| 65+ | 33412 |
| Median household income | 73658 |
| Poverty rate | 10.72 |
| Homeownership rate | 72.47 |
| Unemployment rate | 5.42 |
| Median home value | 378600 |
| Gini index | 0.444 |
| Vacancy rate | 5.92 |
| White | 130703 |
| Black | 995 |
| Asian | 1424 |
| Native | 1327 |
| Hispanic/Latino | 24519 |
| Bachelor's or higher | 48372 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 7](/us/states/co/districts/senate/7.md) — 100% (state senate)
- [CO House District 54](/us/states/co/districts/house/54.md) — 98% (state house)
- [CO House District 55](/us/states/co/districts/house/55.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
