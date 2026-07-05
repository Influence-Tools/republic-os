---
type: Jurisdiction
title: "Tama County, IA"
classification: county
fips: "19171"
state: "IA"
demographics:
  population: 16868
  population_under_18: 4003
  population_18_64: 9328
  population_65_plus: 3537
  median_household_income: 70781
  poverty_rate: 14.8
  homeownership_rate: 75.95
  unemployment_rate: 3.84
  median_home_value: 148600
  gini_index: 0.3968
  vacancy_rate: 11.52
  race_white: 13459
  race_black: 207
  race_asian: 116
  race_native: 1029
  hispanic: 1968
  bachelors_plus: 3056
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/27"
    rel: in-district
    area_weight: 0.7995
  - to: "us/states/ia/districts/senate/38"
    rel: in-district
    area_weight: 0.2004
  - to: "us/states/ia/districts/house/53"
    rel: in-district
    area_weight: 0.7995
  - to: "us/states/ia/districts/house/76"
    rel: in-district
    area_weight: 0.2004
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Tama County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16868 |
| Under 18 | 4003 |
| 18–64 | 9328 |
| 65+ | 3537 |
| Median household income | 70781 |
| Poverty rate | 14.8 |
| Homeownership rate | 75.95 |
| Unemployment rate | 3.84 |
| Median home value | 148600 |
| Gini index | 0.3968 |
| Vacancy rate | 11.52 |
| White | 13459 |
| Black | 207 |
| Asian | 116 |
| Native | 1029 |
| Hispanic/Latino | 1968 |
| Bachelor's or higher | 3056 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 27](/us/states/ia/districts/senate/27.md) — 80% (state senate)
- [IA Senate District 38](/us/states/ia/districts/senate/38.md) — 20% (state senate)
- [IA House District 53](/us/states/ia/districts/house/53.md) — 80% (state house)
- [IA House District 76](/us/states/ia/districts/house/76.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
