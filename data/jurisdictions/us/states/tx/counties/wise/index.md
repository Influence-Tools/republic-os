---
type: Jurisdiction
title: "Wise County, TX"
classification: county
fips: "48497"
state: "TX"
demographics:
  population: 75005
  population_under_18: 18405
  population_18_64: 44942
  population_65_plus: 11658
  median_household_income: 93421
  poverty_rate: 8.89
  homeownership_rate: 81.39
  unemployment_rate: 5.31
  median_home_value: 304900
  gini_index: 0.4095
  vacancy_rate: 8.7
  race_white: 60127
  race_black: 1273
  race_asian: 559
  race_native: 568
  hispanic: 15852
  bachelors_plus: 14672
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.5095
  - to: "us/states/tx/districts/26"
    rel: in-district
    area_weight: 0.4904
  - to: "us/states/tx/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/64"
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

# Wise County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 75005 |
| Under 18 | 18405 |
| 18–64 | 44942 |
| 65+ | 11658 |
| Median household income | 93421 |
| Poverty rate | 8.89 |
| Homeownership rate | 81.39 |
| Unemployment rate | 5.31 |
| Median home value | 304900 |
| Gini index | 0.4095 |
| Vacancy rate | 8.7 |
| White | 60127 |
| Black | 1273 |
| Asian | 559 |
| Native | 568 |
| Hispanic/Latino | 15852 |
| Bachelor's or higher | 14672 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 51% (congressional)
- [TX-26](/us/states/tx/districts/26.md) — 49% (congressional)
- [TX Senate District 12](/us/states/tx/districts/senate/12.md) — 100% (state senate)
- [TX House District 64](/us/states/tx/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
