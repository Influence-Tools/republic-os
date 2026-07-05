---
type: Jurisdiction
title: "Uvalde County, TX"
classification: county
fips: "48463"
state: "TX"
demographics:
  population: 24881
  population_under_18: 6595
  population_18_64: 14188
  population_65_plus: 4098
  median_household_income: 53801
  poverty_rate: 22.17
  homeownership_rate: 70.56
  unemployment_rate: 4.3
  median_home_value: 150800
  gini_index: 0.4947
  vacancy_rate: 16.62
  race_white: 14609
  race_black: 86
  race_asian: 425
  race_native: 367
  hispanic: 17635
  bachelors_plus: 4037
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/80"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Uvalde County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24881 |
| Under 18 | 6595 |
| 18–64 | 14188 |
| 65+ | 4098 |
| Median household income | 53801 |
| Poverty rate | 22.17 |
| Homeownership rate | 70.56 |
| Unemployment rate | 4.3 |
| Median home value | 150800 |
| Gini index | 0.4947 |
| Vacancy rate | 16.62 |
| White | 14609 |
| Black | 86 |
| Asian | 425 |
| Native | 367 |
| Hispanic/Latino | 17635 |
| Bachelor's or higher | 4037 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 80](/us/states/tx/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
