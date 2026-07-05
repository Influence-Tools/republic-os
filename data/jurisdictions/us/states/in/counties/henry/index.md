---
type: Jurisdiction
title: "Henry County, IN"
classification: county
fips: "18065"
state: "IN"
demographics:
  population: 48970
  population_under_18: 9904
  population_18_64: 29478
  population_65_plus: 9588
  median_household_income: 63150
  poverty_rate: 13.63
  homeownership_rate: 76.19
  unemployment_rate: 3.72
  median_home_value: 154400
  gini_index: 0.4252
  vacancy_rate: 11.21
  race_white: 45439
  race_black: 1101
  race_asian: 245
  race_native: 43
  hispanic: 1113
  bachelors_plus: 8278
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/54"
    rel: in-district
    area_weight: 0.8948
  - to: "us/states/in/districts/house/56"
    rel: in-district
    area_weight: 0.0545
  - to: "us/states/in/districts/house/33"
    rel: in-district
    area_weight: 0.0505
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Henry County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48970 |
| Under 18 | 9904 |
| 18–64 | 29478 |
| 65+ | 9588 |
| Median household income | 63150 |
| Poverty rate | 13.63 |
| Homeownership rate | 76.19 |
| Unemployment rate | 3.72 |
| Median home value | 154400 |
| Gini index | 0.4252 |
| Vacancy rate | 11.21 |
| White | 45439 |
| Black | 1101 |
| Asian | 245 |
| Native | 43 |
| Hispanic/Latino | 1113 |
| Bachelor's or higher | 8278 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 27](/us/states/in/districts/senate/27.md) — 100% (state senate)
- [IN House District 54](/us/states/in/districts/house/54.md) — 89% (state house)
- [IN House District 56](/us/states/in/districts/house/56.md) — 5% (state house)
- [IN House District 33](/us/states/in/districts/house/33.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
