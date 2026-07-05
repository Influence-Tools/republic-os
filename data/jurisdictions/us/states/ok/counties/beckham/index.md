---
type: Jurisdiction
title: "Beckham County, OK"
classification: county
fips: "40009"
state: "OK"
demographics:
  population: 22148
  population_under_18: 5125
  population_18_64: 13675
  population_65_plus: 3348
  median_household_income: 53328
  poverty_rate: 21.68
  homeownership_rate: 67.83
  unemployment_rate: 7.86
  median_home_value: 143500
  gini_index: 0.4555
  vacancy_rate: 19.23
  race_white: 17861
  race_black: 1230
  race_asian: 262
  race_native: 407
  hispanic: 3006
  bachelors_plus: 2512
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/57"
    rel: in-district
    area_weight: 0.669
  - to: "us/states/ok/districts/house/55"
    rel: in-district
    area_weight: 0.3309
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Beckham County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22148 |
| Under 18 | 5125 |
| 18–64 | 13675 |
| 65+ | 3348 |
| Median household income | 53328 |
| Poverty rate | 21.68 |
| Homeownership rate | 67.83 |
| Unemployment rate | 7.86 |
| Median home value | 143500 |
| Gini index | 0.4555 |
| Vacancy rate | 19.23 |
| White | 17861 |
| Black | 1230 |
| Asian | 262 |
| Native | 407 |
| Hispanic/Latino | 3006 |
| Bachelor's or higher | 2512 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 57](/us/states/ok/districts/house/57.md) — 67% (state house)
- [OK House District 55](/us/states/ok/districts/house/55.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
