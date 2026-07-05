---
type: Jurisdiction
title: "Scott County, IA"
classification: county
fips: "19163"
state: "IA"
demographics:
  population: 174608
  population_under_18: 40411
  population_18_64: 103580
  population_65_plus: 30617
  median_household_income: 78277
  poverty_rate: 11.5
  homeownership_rate: 69.98
  unemployment_rate: 3.65
  median_home_value: 222000
  gini_index: 0.4523
  vacancy_rate: 6.88
  race_white: 138119
  race_black: 12617
  race_asian: 4993
  race_native: 332
  hispanic: 12902
  bachelors_plus: 60383
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/41"
    rel: in-district
    area_weight: 0.3698
  - to: "us/states/ia/districts/senate/35"
    rel: in-district
    area_weight: 0.3159
  - to: "us/states/ia/districts/senate/47"
    rel: in-district
    area_weight: 0.208
  - to: "us/states/ia/districts/senate/49"
    rel: in-district
    area_weight: 0.1062
  - to: "us/states/ia/districts/house/82"
    rel: in-district
    area_weight: 0.3035
  - to: "us/states/ia/districts/house/94"
    rel: in-district
    area_weight: 0.1441
  - to: "us/states/ia/districts/house/98"
    rel: in-district
    area_weight: 0.0867
  - to: "us/states/ia/districts/house/81"
    rel: in-district
    area_weight: 0.0663
  - to: "us/states/ia/districts/house/93"
    rel: in-district
    area_weight: 0.064
  - to: "us/states/ia/districts/house/97"
    rel: in-district
    area_weight: 0.0195
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Scott County, IA

County jurisdiction — 7 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 174608 |
| Under 18 | 40411 |
| 18–64 | 103580 |
| 65+ | 30617 |
| Median household income | 78277 |
| Poverty rate | 11.5 |
| Homeownership rate | 69.98 |
| Unemployment rate | 3.65 |
| Median home value | 222000 |
| Gini index | 0.4523 |
| Vacancy rate | 6.88 |
| White | 138119 |
| Black | 12617 |
| Asian | 4993 |
| Native | 332 |
| Hispanic/Latino | 12902 |
| Bachelor's or higher | 60383 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 41](/us/states/ia/districts/senate/41.md) — 37% (state senate)
- [IA Senate District 35](/us/states/ia/districts/senate/35.md) — 32% (state senate)
- [IA Senate District 47](/us/states/ia/districts/senate/47.md) — 21% (state senate)
- [IA Senate District 49](/us/states/ia/districts/senate/49.md) — 11% (state senate)
- [IA House District 82](/us/states/ia/districts/house/82.md) — 30% (state house)
- [IA House District 94](/us/states/ia/districts/house/94.md) — 14% (state house)
- [IA House District 98](/us/states/ia/districts/house/98.md) — 9% (state house)
- [IA House District 81](/us/states/ia/districts/house/81.md) — 7% (state house)
- [IA House District 93](/us/states/ia/districts/house/93.md) — 6% (state house)
- [IA House District 97](/us/states/ia/districts/house/97.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
