---
type: Jurisdiction
title: "Lincoln County, OK"
classification: county
fips: "40081"
state: "OK"
demographics:
  population: 34219
  population_under_18: 8028
  population_18_64: 19558
  population_65_plus: 6633
  median_household_income: 62216
  poverty_rate: 17.27
  homeownership_rate: 80.3
  unemployment_rate: 3.86
  median_home_value: 166500
  gini_index: 0.4491
  vacancy_rate: 9.75
  race_white: 27938
  race_black: 569
  race_asian: 192
  race_native: 1896
  hispanic: 1364
  bachelors_plus: 5067
districts:
  - to: "us/states/ok/districts/05"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ok/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/32"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Lincoln County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34219 |
| Under 18 | 8028 |
| 18–64 | 19558 |
| 65+ | 6633 |
| Median household income | 62216 |
| Poverty rate | 17.27 |
| Homeownership rate | 80.3 |
| Unemployment rate | 3.86 |
| Median home value | 166500 |
| Gini index | 0.4491 |
| Vacancy rate | 9.75 |
| White | 27938 |
| Black | 569 |
| Asian | 192 |
| Native | 1896 |
| Hispanic/Latino | 1364 |
| Bachelor's or higher | 5067 |

## Districts

- [OK-05](/us/states/ok/districts/05.md) — 100% (congressional)
- [OK Senate District 28](/us/states/ok/districts/senate/28.md) — 100% (state senate)
- [OK House District 32](/us/states/ok/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
