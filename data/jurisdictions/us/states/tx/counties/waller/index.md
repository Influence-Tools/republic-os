---
type: Jurisdiction
title: "Waller County, TX"
classification: county
fips: "48473"
state: "TX"
demographics:
  population: 61552
  population_under_18: 14610
  population_18_64: 39799
  population_65_plus: 7143
  median_household_income: 80397
  poverty_rate: 14.63
  homeownership_rate: 72.02
  unemployment_rate: 6.78
  median_home_value: 318700
  gini_index: 0.4688
  vacancy_rate: 9.85
  race_white: 27463
  race_black: 14538
  race_asian: 1239
  race_native: 823
  hispanic: 20629
  bachelors_plus: 12577
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.7007
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 0.2993
  - to: "us/states/tx/districts/house/85"
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

# Waller County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61552 |
| Under 18 | 14610 |
| 18–64 | 39799 |
| 65+ | 7143 |
| Median household income | 80397 |
| Poverty rate | 14.63 |
| Homeownership rate | 72.02 |
| Unemployment rate | 6.78 |
| Median home value | 318700 |
| Gini index | 0.4688 |
| Vacancy rate | 9.85 |
| White | 27463 |
| Black | 14538 |
| Asian | 1239 |
| Native | 823 |
| Hispanic/Latino | 20629 |
| Bachelor's or higher | 12577 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 70% (state senate)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 30% (state senate)
- [TX House District 85](/us/states/tx/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
