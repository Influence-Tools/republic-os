---
type: Jurisdiction
title: "Woodward County, OK"
classification: county
fips: "40153"
state: "OK"
demographics:
  population: 20158
  population_under_18: 4869
  population_18_64: 11925
  population_65_plus: 3364
  median_household_income: 61417
  poverty_rate: 14.02
  homeownership_rate: 73.24
  unemployment_rate: 6.18
  median_home_value: 169000
  gini_index: 0.439
  vacancy_rate: 15.61
  race_white: 15975
  race_black: 220
  race_asian: 78
  race_native: 692
  hispanic: 3073
  bachelors_plus: 3739
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/58"
    rel: in-district
    area_weight: 0.4848
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 0.2886
  - to: "us/states/ok/districts/house/59"
    rel: in-district
    area_weight: 0.2266
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Woodward County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20158 |
| Under 18 | 4869 |
| 18–64 | 11925 |
| 65+ | 3364 |
| Median household income | 61417 |
| Poverty rate | 14.02 |
| Homeownership rate | 73.24 |
| Unemployment rate | 6.18 |
| Median home value | 169000 |
| Gini index | 0.439 |
| Vacancy rate | 15.61 |
| White | 15975 |
| Black | 220 |
| Asian | 78 |
| Native | 692 |
| Hispanic/Latino | 3073 |
| Bachelor's or higher | 3739 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 58](/us/states/ok/districts/house/58.md) — 48% (state house)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 29% (state house)
- [OK House District 59](/us/states/ok/districts/house/59.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
