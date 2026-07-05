---
type: Jurisdiction
title: "Marshall County, OK"
classification: county
fips: "40095"
state: "OK"
demographics:
  population: 15792
  population_under_18: 3674
  population_18_64: 8562
  population_65_plus: 3556
  median_household_income: 57245
  poverty_rate: 16.08
  homeownership_rate: 77.57
  unemployment_rate: 4.71
  median_home_value: 164500
  gini_index: 0.4481
  vacancy_rate: 32.27
  race_white: 10429
  race_black: 67
  race_asian: 69
  race_native: 1127
  hispanic: 2866
  bachelors_plus: 2482
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/14"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ok/districts/house/49"
    rel: in-district
    area_weight: 0.7104
  - to: "us/states/ok/districts/house/21"
    rel: in-district
    area_weight: 0.2894
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Marshall County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15792 |
| Under 18 | 3674 |
| 18–64 | 8562 |
| 65+ | 3556 |
| Median household income | 57245 |
| Poverty rate | 16.08 |
| Homeownership rate | 77.57 |
| Unemployment rate | 4.71 |
| Median home value | 164500 |
| Gini index | 0.4481 |
| Vacancy rate | 32.27 |
| White | 10429 |
| Black | 67 |
| Asian | 69 |
| Native | 1127 |
| Hispanic/Latino | 2866 |
| Bachelor's or higher | 2482 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 14](/us/states/ok/districts/senate/14.md) — 100% (state senate)
- [OK House District 49](/us/states/ok/districts/house/49.md) — 71% (state house)
- [OK House District 21](/us/states/ok/districts/house/21.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
