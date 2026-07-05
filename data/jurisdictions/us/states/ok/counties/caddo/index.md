---
type: Jurisdiction
title: "Caddo County, OK"
classification: county
fips: "40015"
state: "OK"
demographics:
  population: 26447
  population_under_18: 6083
  population_18_64: 16203
  population_65_plus: 4161
  median_household_income: 55353
  poverty_rate: 18.3
  homeownership_rate: 72.71
  unemployment_rate: 5.83
  median_home_value: 115700
  gini_index: 0.4192
  vacancy_rate: 21.59
  race_white: 14650
  race_black: 897
  race_asian: 119
  race_native: 4816
  hispanic: 4487
  bachelors_plus: 3614
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/65"
    rel: in-district
    area_weight: 0.8199
  - to: "us/states/ok/districts/house/55"
    rel: in-district
    area_weight: 0.1326
  - to: "us/states/ok/districts/house/56"
    rel: in-district
    area_weight: 0.0475
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Caddo County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26447 |
| Under 18 | 6083 |
| 18–64 | 16203 |
| 65+ | 4161 |
| Median household income | 55353 |
| Poverty rate | 18.3 |
| Homeownership rate | 72.71 |
| Unemployment rate | 5.83 |
| Median home value | 115700 |
| Gini index | 0.4192 |
| Vacancy rate | 21.59 |
| White | 14650 |
| Black | 897 |
| Asian | 119 |
| Native | 4816 |
| Hispanic/Latino | 4487 |
| Bachelor's or higher | 3614 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 26](/us/states/ok/districts/senate/26.md) — 100% (state senate)
- [OK House District 65](/us/states/ok/districts/house/65.md) — 82% (state house)
- [OK House District 55](/us/states/ok/districts/house/55.md) — 13% (state house)
- [OK House District 56](/us/states/ok/districts/house/56.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
