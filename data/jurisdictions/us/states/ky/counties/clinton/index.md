---
type: Jurisdiction
title: "Clinton County, KY"
classification: county
fips: "21053"
state: "KY"
demographics:
  population: 9202
  population_under_18: 1974
  population_18_64: 5334
  population_65_plus: 1894
  median_household_income: 44844
  poverty_rate: 17.47
  homeownership_rate: 71.15
  unemployment_rate: 4.99
  median_home_value: 122200
  gini_index: 0.4277
  vacancy_rate: 20.54
  race_white: 8666
  race_black: 15
  race_asian: 173
  race_native: 50
  hispanic: 315
  bachelors_plus: 1612
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/ky/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/83"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Clinton County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9202 |
| Under 18 | 1974 |
| 18–64 | 5334 |
| 65+ | 1894 |
| Median household income | 44844 |
| Poverty rate | 17.47 |
| Homeownership rate | 71.15 |
| Unemployment rate | 4.99 |
| Median home value | 122200 |
| Gini index | 0.4277 |
| Vacancy rate | 20.54 |
| White | 8666 |
| Black | 15 |
| Asian | 173 |
| Native | 50 |
| Hispanic/Latino | 315 |
| Bachelor's or higher | 1612 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 15](/us/states/ky/districts/senate/15.md) — 100% (state senate)
- [KY House District 83](/us/states/ky/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
