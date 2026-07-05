---
type: Jurisdiction
title: "Noble County, OK"
classification: county
fips: "40103"
state: "OK"
demographics:
  population: 10897
  population_under_18: 2466
  population_18_64: 6071
  population_65_plus: 2360
  median_household_income: 66365
  poverty_rate: 12.86
  homeownership_rate: 77.72
  unemployment_rate: 2.63
  median_home_value: 146400
  gini_index: 0.4217
  vacancy_rate: 18.33
  race_white: 8631
  race_black: 30
  race_asian: 30
  race_native: 697
  hispanic: 511
  bachelors_plus: 1769
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/38"
    rel: in-district
    area_weight: 0.6004
  - to: "us/states/ok/districts/house/35"
    rel: in-district
    area_weight: 0.3996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Noble County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10897 |
| Under 18 | 2466 |
| 18–64 | 6071 |
| 65+ | 2360 |
| Median household income | 66365 |
| Poverty rate | 12.86 |
| Homeownership rate | 77.72 |
| Unemployment rate | 2.63 |
| Median home value | 146400 |
| Gini index | 0.4217 |
| Vacancy rate | 18.33 |
| White | 8631 |
| Black | 30 |
| Asian | 30 |
| Native | 697 |
| Hispanic/Latino | 511 |
| Bachelor's or higher | 1769 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 20](/us/states/ok/districts/senate/20.md) — 100% (state senate)
- [OK House District 38](/us/states/ok/districts/house/38.md) — 60% (state house)
- [OK House District 35](/us/states/ok/districts/house/35.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
