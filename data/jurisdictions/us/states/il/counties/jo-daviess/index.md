---
type: Jurisdiction
title: "Jo Daviess County, IL"
classification: county
fips: "17085"
state: "IL"
demographics:
  population: 21851
  population_under_18: 3972
  population_18_64: 11338
  population_65_plus: 6541
  median_household_income: 73993
  poverty_rate: 7.84
  homeownership_rate: 80.38
  unemployment_rate: 3.59
  median_home_value: 209900
  gini_index: 0.4282
  vacancy_rate: 22.69
  race_white: 20434
  race_black: 166
  race_asian: 118
  race_native: 63
  hispanic: 912
  bachelors_plus: 6302
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/il/districts/senate/45"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/house/89"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Jo Daviess County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21851 |
| Under 18 | 3972 |
| 18–64 | 11338 |
| 65+ | 6541 |
| Median household income | 73993 |
| Poverty rate | 7.84 |
| Homeownership rate | 80.38 |
| Unemployment rate | 3.59 |
| Median home value | 209900 |
| Gini index | 0.4282 |
| Vacancy rate | 22.69 |
| White | 20434 |
| Black | 166 |
| Asian | 118 |
| Native | 63 |
| Hispanic/Latino | 912 |
| Bachelor's or higher | 6302 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 45](/us/states/il/districts/senate/45.md) — 100% (state senate)
- [IL House District 89](/us/states/il/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
