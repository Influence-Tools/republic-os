---
type: Jurisdiction
title: "Warren County, MS"
classification: county
fips: "28149"
state: "MS"
demographics:
  population: 43020
  population_under_18: 10115
  population_18_64: 24750
  population_65_plus: 8155
  median_household_income: 59401
  poverty_rate: 19.52
  homeownership_rate: 69.86
  unemployment_rate: 4.81
  median_home_value: 156400
  gini_index: 0.4685
  vacancy_rate: 22.23
  race_white: 20018
  race_black: 20966
  race_asian: 261
  race_native: 60
  hispanic: 918
  bachelors_plus: 12029
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9955
  - to: "us/states/ms/districts/senate/23"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ms/districts/house/54"
    rel: in-district
    area_weight: 0.5389
  - to: "us/states/ms/districts/house/85"
    rel: in-district
    area_weight: 0.2665
  - to: "us/states/ms/districts/house/55"
    rel: in-district
    area_weight: 0.1938
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Warren County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43020 |
| Under 18 | 10115 |
| 18–64 | 24750 |
| 65+ | 8155 |
| Median household income | 59401 |
| Poverty rate | 19.52 |
| Homeownership rate | 69.86 |
| Unemployment rate | 4.81 |
| Median home value | 156400 |
| Gini index | 0.4685 |
| Vacancy rate | 22.23 |
| White | 20018 |
| Black | 20966 |
| Asian | 261 |
| Native | 60 |
| Hispanic/Latino | 918 |
| Bachelor's or higher | 12029 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 23](/us/states/ms/districts/senate/23.md) — 100% (state senate)
- [MS House District 54](/us/states/ms/districts/house/54.md) — 54% (state house)
- [MS House District 85](/us/states/ms/districts/house/85.md) — 27% (state house)
- [MS House District 55](/us/states/ms/districts/house/55.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
