---
type: Jurisdiction
title: "Hunterdon County, NJ"
classification: county
fips: "34019"
state: "NJ"
demographics:
  population: 130160
  population_under_18: 24884
  population_18_64: 78178
  population_65_plus: 27098
  median_household_income: 141715
  poverty_rate: 3.99
  homeownership_rate: 85.14
  unemployment_rate: 4.6
  median_home_value: 517200
  gini_index: 0.4431
  vacancy_rate: 2.41
  race_white: 105731
  race_black: 3336
  race_asian: 6436
  race_native: 244
  hispanic: 12117
  bachelors_plus: 77088
districts:
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/nj/districts/senate/23"
    rel: in-district
    area_weight: 0.4257
  - to: "us/states/nj/districts/senate/15"
    rel: in-district
    area_weight: 0.2877
  - to: "us/states/nj/districts/senate/16"
    rel: in-district
    area_weight: 0.2862
  - to: "us/states/nj/districts/house/23"
    rel: in-district
    area_weight: 0.4257
  - to: "us/states/nj/districts/house/15"
    rel: in-district
    area_weight: 0.2877
  - to: "us/states/nj/districts/house/16"
    rel: in-district
    area_weight: 0.2862
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Hunterdon County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 130160 |
| Under 18 | 24884 |
| 18–64 | 78178 |
| 65+ | 27098 |
| Median household income | 141715 |
| Poverty rate | 3.99 |
| Homeownership rate | 85.14 |
| Unemployment rate | 4.6 |
| Median home value | 517200 |
| Gini index | 0.4431 |
| Vacancy rate | 2.41 |
| White | 105731 |
| Black | 3336 |
| Asian | 6436 |
| Native | 244 |
| Hispanic/Latino | 12117 |
| Bachelor's or higher | 77088 |

## Districts

- [NJ-07](/us/states/nj/districts/07.md) — 100% (congressional)
- [NJ Senate District 23](/us/states/nj/districts/senate/23.md) — 43% (state senate)
- [NJ Senate District 15](/us/states/nj/districts/senate/15.md) — 29% (state senate)
- [NJ Senate District 16](/us/states/nj/districts/senate/16.md) — 29% (state senate)
- [NJ House District 23](/us/states/nj/districts/house/23.md) — 43% (state house)
- [NJ House District 15](/us/states/nj/districts/house/15.md) — 29% (state house)
- [NJ House District 16](/us/states/nj/districts/house/16.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
