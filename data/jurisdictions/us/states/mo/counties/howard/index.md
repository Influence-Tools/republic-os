---
type: Jurisdiction
title: "Howard County, MO"
classification: county
fips: "29089"
state: "MO"
demographics:
  population: 10147
  population_under_18: 2155
  population_18_64: 5950
  population_65_plus: 2042
  median_household_income: 65938
  poverty_rate: 12.04
  homeownership_rate: 78.69
  unemployment_rate: 3.74
  median_home_value: 159400
  gini_index: 0.4166
  vacancy_rate: 18.04
  race_white: 8779
  race_black: 561
  race_asian: 21
  race_native: 151
  hispanic: 229
  bachelors_plus: 2491
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/48"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Howard County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10147 |
| Under 18 | 2155 |
| 18–64 | 5950 |
| 65+ | 2042 |
| Median household income | 65938 |
| Poverty rate | 12.04 |
| Homeownership rate | 78.69 |
| Unemployment rate | 3.74 |
| Median home value | 159400 |
| Gini index | 0.4166 |
| Vacancy rate | 18.04 |
| White | 8779 |
| Black | 561 |
| Asian | 21 |
| Native | 151 |
| Hispanic/Latino | 229 |
| Bachelor's or higher | 2491 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 100% (state senate)
- [MO House District 48](/us/states/mo/districts/house/48.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
