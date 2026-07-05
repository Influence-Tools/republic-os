---
type: Jurisdiction
title: "Jackson County, MS"
classification: county
fips: "28059"
state: "MS"
demographics:
  population: 145249
  population_under_18: 33197
  population_18_64: 86985
  population_65_plus: 25067
  median_household_income: 66201
  poverty_rate: 13.84
  homeownership_rate: 72.66
  unemployment_rate: 6.71
  median_home_value: 193100
  gini_index: 0.4625
  vacancy_rate: 9.3
  race_white: 97625
  race_black: 27543
  race_asian: 3175
  race_native: 652
  hispanic: 11070
  bachelors_plus: 36341
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.7378
  - to: "us/states/ms/districts/senate/51"
    rel: in-district
    area_weight: 0.3376
  - to: "us/states/ms/districts/senate/47"
    rel: in-district
    area_weight: 0.2985
  - to: "us/states/ms/districts/senate/52"
    rel: in-district
    area_weight: 0.0793
  - to: "us/states/ms/districts/house/109"
    rel: in-district
    area_weight: 0.3028
  - to: "us/states/ms/districts/house/114"
    rel: in-district
    area_weight: 0.1423
  - to: "us/states/ms/districts/house/111"
    rel: in-district
    area_weight: 0.1231
  - to: "us/states/ms/districts/house/112"
    rel: in-district
    area_weight: 0.1047
  - to: "us/states/ms/districts/house/110"
    rel: in-district
    area_weight: 0.0226
  - to: "us/states/ms/districts/house/113"
    rel: in-district
    area_weight: 0.02
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Jackson County, MS

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 145249 |
| Under 18 | 33197 |
| 18–64 | 86985 |
| 65+ | 25067 |
| Median household income | 66201 |
| Poverty rate | 13.84 |
| Homeownership rate | 72.66 |
| Unemployment rate | 6.71 |
| Median home value | 193100 |
| Gini index | 0.4625 |
| Vacancy rate | 9.3 |
| White | 97625 |
| Black | 27543 |
| Asian | 3175 |
| Native | 652 |
| Hispanic/Latino | 11070 |
| Bachelor's or higher | 36341 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 74% (congressional)
- [MS Senate District 51](/us/states/ms/districts/senate/51.md) — 34% (state senate)
- [MS Senate District 47](/us/states/ms/districts/senate/47.md) — 30% (state senate)
- [MS Senate District 52](/us/states/ms/districts/senate/52.md) — 8% (state senate)
- [MS House District 109](/us/states/ms/districts/house/109.md) — 30% (state house)
- [MS House District 114](/us/states/ms/districts/house/114.md) — 14% (state house)
- [MS House District 111](/us/states/ms/districts/house/111.md) — 12% (state house)
- [MS House District 112](/us/states/ms/districts/house/112.md) — 10% (state house)
- [MS House District 110](/us/states/ms/districts/house/110.md) — 2% (state house)
- [MS House District 113](/us/states/ms/districts/house/113.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
