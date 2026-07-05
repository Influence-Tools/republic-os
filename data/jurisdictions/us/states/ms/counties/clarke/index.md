---
type: Jurisdiction
title: "Clarke County, MS"
classification: county
fips: "28023"
state: "MS"
demographics:
  population: 15314
  population_under_18: 3333
  population_18_64: 8565
  population_65_plus: 3416
  median_household_income: 46108
  poverty_rate: 17.39
  homeownership_rate: 82.29
  unemployment_rate: 7.02
  median_home_value: 118100
  gini_index: 0.4825
  vacancy_rate: 22.24
  race_white: 9706
  race_black: 4777
  race_asian: 26
  race_native: 66
  hispanic: 166
  bachelors_plus: 2549
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/house/84"
    rel: in-district
    area_weight: 0.6685
  - to: "us/states/ms/districts/house/80"
    rel: in-district
    area_weight: 0.2236
  - to: "us/states/ms/districts/house/81"
    rel: in-district
    area_weight: 0.1077
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Clarke County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15314 |
| Under 18 | 3333 |
| 18–64 | 8565 |
| 65+ | 3416 |
| Median household income | 46108 |
| Poverty rate | 17.39 |
| Homeownership rate | 82.29 |
| Unemployment rate | 7.02 |
| Median home value | 118100 |
| Gini index | 0.4825 |
| Vacancy rate | 22.24 |
| White | 9706 |
| Black | 4777 |
| Asian | 26 |
| Native | 66 |
| Hispanic/Latino | 166 |
| Bachelor's or higher | 2549 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 33](/us/states/ms/districts/senate/33.md) — 100% (state senate)
- [MS House District 84](/us/states/ms/districts/house/84.md) — 67% (state house)
- [MS House District 80](/us/states/ms/districts/house/80.md) — 22% (state house)
- [MS House District 81](/us/states/ms/districts/house/81.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
