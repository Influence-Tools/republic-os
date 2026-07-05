---
type: Jurisdiction
title: "Castro County, TX"
classification: county
fips: "48069"
state: "TX"
demographics:
  population: 7344
  population_under_18: 2135
  population_18_64: 3833
  population_65_plus: 1376
  median_household_income: 56776
  poverty_rate: 19.19
  homeownership_rate: 63.57
  unemployment_rate: 3.74
  median_home_value: 95000
  gini_index: 0.4699
  vacancy_rate: 20.21
  race_white: 3000
  race_black: 86
  race_asian: 66
  race_native: 60
  hispanic: 4817
  bachelors_plus: 1000
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Castro County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7344 |
| Under 18 | 2135 |
| 18–64 | 3833 |
| 65+ | 1376 |
| Median household income | 56776 |
| Poverty rate | 19.19 |
| Homeownership rate | 63.57 |
| Unemployment rate | 3.74 |
| Median home value | 95000 |
| Gini index | 0.4699 |
| Vacancy rate | 20.21 |
| White | 3000 |
| Black | 86 |
| Asian | 66 |
| Native | 60 |
| Hispanic/Latino | 4817 |
| Bachelor's or higher | 1000 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
