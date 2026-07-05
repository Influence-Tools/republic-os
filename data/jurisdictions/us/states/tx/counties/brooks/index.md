---
type: Jurisdiction
title: "Brooks County, TX"
classification: county
fips: "48047"
state: "TX"
demographics:
  population: 6943
  population_under_18: 1452
  population_18_64: 3994
  population_65_plus: 1497
  median_household_income: 47764
  poverty_rate: 19.4
  homeownership_rate: 52.8
  unemployment_rate: 19.94
  median_home_value: 81000
  gini_index: 0.4542
  vacancy_rate: 23.35
  race_white: 1672
  race_black: 40
  race_asian: 0
  race_native: 62
  hispanic: 6256
  bachelors_plus: 1035
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Brooks County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6943 |
| Under 18 | 1452 |
| 18–64 | 3994 |
| 65+ | 1497 |
| Median household income | 47764 |
| Poverty rate | 19.4 |
| Homeownership rate | 52.8 |
| Unemployment rate | 19.94 |
| Median home value | 81000 |
| Gini index | 0.4542 |
| Vacancy rate | 23.35 |
| White | 1672 |
| Black | 40 |
| Asian | 0 |
| Native | 62 |
| Hispanic/Latino | 6256 |
| Bachelor's or higher | 1035 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 100% (congressional)
- [TX Senate District 20](/us/states/tx/districts/senate/20.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
