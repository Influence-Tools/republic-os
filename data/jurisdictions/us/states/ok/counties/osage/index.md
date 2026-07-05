---
type: Jurisdiction
title: "Osage County, OK"
classification: county
fips: "40113"
state: "OK"
demographics:
  population: 45997
  population_under_18: 9617
  population_18_64: 26546
  population_65_plus: 9834
  median_household_income: 62847
  poverty_rate: 13.09
  homeownership_rate: 78.3
  unemployment_rate: 5.34
  median_home_value: 182100
  gini_index: 0.4497
  vacancy_rate: 12.63
  race_white: 28985
  race_black: 4657
  race_asian: 121
  race_native: 5117
  hispanic: 2155
  bachelors_plus: 9935
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/10"
    rel: in-district
    area_weight: 0.9898
  - to: "us/states/ok/districts/senate/11"
    rel: in-district
    area_weight: 0.0101
  - to: "us/states/ok/districts/house/37"
    rel: in-district
    area_weight: 0.5219
  - to: "us/states/ok/districts/house/10"
    rel: in-district
    area_weight: 0.2909
  - to: "us/states/ok/districts/house/35"
    rel: in-district
    area_weight: 0.1047
  - to: "us/states/ok/districts/house/66"
    rel: in-district
    area_weight: 0.0791
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Osage County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45997 |
| Under 18 | 9617 |
| 18–64 | 26546 |
| 65+ | 9834 |
| Median household income | 62847 |
| Poverty rate | 13.09 |
| Homeownership rate | 78.3 |
| Unemployment rate | 5.34 |
| Median home value | 182100 |
| Gini index | 0.4497 |
| Vacancy rate | 12.63 |
| White | 28985 |
| Black | 4657 |
| Asian | 121 |
| Native | 5117 |
| Hispanic/Latino | 2155 |
| Bachelor's or higher | 9935 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 10](/us/states/ok/districts/senate/10.md) — 99% (state senate)
- [OK Senate District 11](/us/states/ok/districts/senate/11.md) — 1% (state senate)
- [OK House District 37](/us/states/ok/districts/house/37.md) — 52% (state house)
- [OK House District 10](/us/states/ok/districts/house/10.md) — 29% (state house)
- [OK House District 35](/us/states/ok/districts/house/35.md) — 10% (state house)
- [OK House District 66](/us/states/ok/districts/house/66.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
