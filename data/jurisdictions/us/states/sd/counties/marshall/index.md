---
type: Jurisdiction
title: "Marshall County, SD"
classification: county
fips: "46091"
state: "SD"
demographics:
  population: 4344
  population_under_18: 1218
  population_18_64: 1062
  population_65_plus: 2064
  median_household_income: 78156
  poverty_rate: 6.06
  homeownership_rate: 80.31
  unemployment_rate: 0.32
  median_home_value: 156500
  gini_index: 0.4487
  vacancy_rate: 32.22
  race_white: 3670
  race_black: 19
  race_asian: 8
  race_native: 255
  hispanic: 278
  bachelors_plus: 929
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/sd/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/sd/districts/house/1"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Marshall County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4344 |
| Under 18 | 1218 |
| 18–64 | 1062 |
| 65+ | 2064 |
| Median household income | 78156 |
| Poverty rate | 6.06 |
| Homeownership rate | 80.31 |
| Unemployment rate | 0.32 |
| Median home value | 156500 |
| Gini index | 0.4487 |
| Vacancy rate | 32.22 |
| White | 3670 |
| Black | 19 |
| Asian | 8 |
| Native | 255 |
| Hispanic/Latino | 278 |
| Bachelor's or higher | 929 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 1](/us/states/sd/districts/senate/1.md) — 100% (state senate)
- [SD House District 1](/us/states/sd/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
