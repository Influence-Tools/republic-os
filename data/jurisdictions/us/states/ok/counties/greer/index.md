---
type: Jurisdiction
title: "Greer County, OK"
classification: county
fips: "40055"
state: "OK"
demographics:
  population: 5489
  population_under_18: 1094
  population_18_64: 3458
  population_65_plus: 937
  median_household_income: 59406
  poverty_rate: 16.92
  homeownership_rate: 77.98
  unemployment_rate: 7.26
  median_home_value: 109100
  gini_index: 0.4554
  vacancy_rate: 25.45
  race_white: 4446
  race_black: 328
  race_asian: 10
  race_native: 111
  hispanic: 712
  bachelors_plus: 681
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/52"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Greer County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5489 |
| Under 18 | 1094 |
| 18–64 | 3458 |
| 65+ | 937 |
| Median household income | 59406 |
| Poverty rate | 16.92 |
| Homeownership rate | 77.98 |
| Unemployment rate | 7.26 |
| Median home value | 109100 |
| Gini index | 0.4554 |
| Vacancy rate | 25.45 |
| White | 4446 |
| Black | 328 |
| Asian | 10 |
| Native | 111 |
| Hispanic/Latino | 712 |
| Bachelor's or higher | 681 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 52](/us/states/ok/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
