---
type: Jurisdiction
title: "Harrison County, IA"
classification: county
fips: "19085"
state: "IA"
demographics:
  population: 14632
  population_under_18: 3378
  population_18_64: 8308
  population_65_plus: 2946
  median_household_income: 79535
  poverty_rate: 7.09
  homeownership_rate: 77.14
  unemployment_rate: 2.29
  median_home_value: 176000
  gini_index: 0.3969
  vacancy_rate: 9.09
  race_white: 13882
  race_black: 18
  race_asian: 43
  race_native: 9
  hispanic: 328
  bachelors_plus: 2841
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ia/districts/senate/8"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ia/districts/house/15"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Harrison County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14632 |
| Under 18 | 3378 |
| 18–64 | 8308 |
| 65+ | 2946 |
| Median household income | 79535 |
| Poverty rate | 7.09 |
| Homeownership rate | 77.14 |
| Unemployment rate | 2.29 |
| Median home value | 176000 |
| Gini index | 0.3969 |
| Vacancy rate | 9.09 |
| White | 13882 |
| Black | 18 |
| Asian | 43 |
| Native | 9 |
| Hispanic/Latino | 328 |
| Bachelor's or higher | 2841 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 8](/us/states/ia/districts/senate/8.md) — 100% (state senate)
- [IA House District 15](/us/states/ia/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
