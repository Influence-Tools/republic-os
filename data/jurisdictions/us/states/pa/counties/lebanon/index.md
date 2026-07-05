---
type: Jurisdiction
title: "Lebanon County, PA"
classification: county
fips: "42075"
state: "PA"
demographics:
  population: 144186
  population_under_18: 32492
  population_18_64: 82169
  population_65_plus: 29525
  median_household_income: 78425
  poverty_rate: 10.1
  homeownership_rate: 71.27
  unemployment_rate: 4.32
  median_home_value: 242000
  gini_index: 0.4341
  vacancy_rate: 5.36
  race_white: 116318
  race_black: 3168
  race_asian: 2331
  race_native: 93
  hispanic: 21918
  bachelors_plus: 33532
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/senate/48"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/102"
    rel: in-district
    area_weight: 0.6827
  - to: "us/states/pa/districts/house/101"
    rel: in-district
    area_weight: 0.1959
  - to: "us/states/pa/districts/house/98"
    rel: in-district
    area_weight: 0.1212
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Lebanon County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 144186 |
| Under 18 | 32492 |
| 18–64 | 82169 |
| 65+ | 29525 |
| Median household income | 78425 |
| Poverty rate | 10.1 |
| Homeownership rate | 71.27 |
| Unemployment rate | 4.32 |
| Median home value | 242000 |
| Gini index | 0.4341 |
| Vacancy rate | 5.36 |
| White | 116318 |
| Black | 3168 |
| Asian | 2331 |
| Native | 93 |
| Hispanic/Latino | 21918 |
| Bachelor's or higher | 33532 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 48](/us/states/pa/districts/senate/48.md) — 100% (state senate)
- [PA House District 102](/us/states/pa/districts/house/102.md) — 68% (state house)
- [PA House District 101](/us/states/pa/districts/house/101.md) — 20% (state house)
- [PA House District 98](/us/states/pa/districts/house/98.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
