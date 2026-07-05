---
type: Jurisdiction
title: "McIntosh County, OK"
classification: county
fips: "40091"
state: "OK"
demographics:
  population: 19400
  population_under_18: 3869
  population_18_64: 10581
  population_65_plus: 4950
  median_household_income: 46281
  poverty_rate: 21.06
  homeownership_rate: 76.57
  unemployment_rate: 5.29
  median_home_value: 146200
  gini_index: 0.4809
  vacancy_rate: 34.56
  race_white: 13087
  race_black: 504
  race_asian: 186
  race_native: 3094
  hispanic: 637
  bachelors_plus: 3053
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/15"
    rel: in-district
    area_weight: 0.8639
  - to: "us/states/ok/districts/house/13"
    rel: in-district
    area_weight: 0.136
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# McIntosh County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19400 |
| Under 18 | 3869 |
| 18–64 | 10581 |
| 65+ | 4950 |
| Median household income | 46281 |
| Poverty rate | 21.06 |
| Homeownership rate | 76.57 |
| Unemployment rate | 5.29 |
| Median home value | 146200 |
| Gini index | 0.4809 |
| Vacancy rate | 34.56 |
| White | 13087 |
| Black | 504 |
| Asian | 186 |
| Native | 3094 |
| Hispanic/Latino | 637 |
| Bachelor's or higher | 3053 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 8](/us/states/ok/districts/senate/8.md) — 100% (state senate)
- [OK House District 15](/us/states/ok/districts/house/15.md) — 86% (state house)
- [OK House District 13](/us/states/ok/districts/house/13.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
