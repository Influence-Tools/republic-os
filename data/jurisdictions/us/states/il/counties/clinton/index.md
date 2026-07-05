---
type: Jurisdiction
title: "Clinton County, IL"
classification: county
fips: "17027"
state: "IL"
demographics:
  population: 36954
  population_under_18: 7980
  population_18_64: 22019
  population_65_plus: 6955
  median_household_income: 86588
  poverty_rate: 7.37
  homeownership_rate: 80.29
  unemployment_rate: 3.42
  median_home_value: 192400
  gini_index: 0.4283
  vacancy_rate: 7.58
  race_white: 33584
  race_black: 1164
  race_asian: 231
  race_native: 77
  hispanic: 1512
  bachelors_plus: 9017
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.5065
  - to: "us/states/il/districts/house/109"
    rel: in-district
    area_weight: 0.4935
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Clinton County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36954 |
| Under 18 | 7980 |
| 18–64 | 22019 |
| 65+ | 6955 |
| Median household income | 86588 |
| Poverty rate | 7.37 |
| Homeownership rate | 80.29 |
| Unemployment rate | 3.42 |
| Median home value | 192400 |
| Gini index | 0.4283 |
| Vacancy rate | 7.58 |
| White | 33584 |
| Black | 1164 |
| Asian | 231 |
| Native | 77 |
| Hispanic/Latino | 1512 |
| Bachelor's or higher | 9017 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 100% (state senate)
- [IL House District 110](/us/states/il/districts/house/110.md) — 51% (state house)
- [IL House District 109](/us/states/il/districts/house/109.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
