---
type: Jurisdiction
title: "Texas County, MO"
classification: county
fips: "29215"
state: "MO"
demographics:
  population: 25161
  population_under_18: 5564
  population_18_64: 14180
  population_65_plus: 5417
  median_household_income: 50036
  poverty_rate: 19.81
  homeownership_rate: 77.22
  unemployment_rate: 5.1
  median_home_value: 146700
  gini_index: 0.4223
  vacancy_rate: 13.66
  race_white: 22463
  race_black: 912
  race_asian: 37
  race_native: 68
  hispanic: 620
  bachelors_plus: 4336
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/143"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Texas County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25161 |
| Under 18 | 5564 |
| 18–64 | 14180 |
| 65+ | 5417 |
| Median household income | 50036 |
| Poverty rate | 19.81 |
| Homeownership rate | 77.22 |
| Unemployment rate | 5.1 |
| Median home value | 146700 |
| Gini index | 0.4223 |
| Vacancy rate | 13.66 |
| White | 22463 |
| Black | 912 |
| Asian | 37 |
| Native | 68 |
| Hispanic/Latino | 620 |
| Bachelor's or higher | 4336 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 143](/us/states/mo/districts/house/143.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
