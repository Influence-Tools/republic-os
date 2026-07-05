---
type: Jurisdiction
title: "Ector County, TX"
classification: county
fips: "48135"
state: "TX"
demographics:
  population: 164654
  population_under_18: 50018
  population_18_64: 98378
  population_65_plus: 16258
  median_household_income: 71536
  poverty_rate: 16.45
  homeownership_rate: 64.67
  unemployment_rate: 5.88
  median_home_value: 200200
  gini_index: 0.4704
  vacancy_rate: 6.29
  race_white: 79219
  race_black: 7352
  race_asian: 2015
  race_native: 942
  hispanic: 104530
  bachelors_plus: 22798
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/81"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Ector County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 164654 |
| Under 18 | 50018 |
| 18–64 | 98378 |
| 65+ | 16258 |
| Median household income | 71536 |
| Poverty rate | 16.45 |
| Homeownership rate | 64.67 |
| Unemployment rate | 5.88 |
| Median home value | 200200 |
| Gini index | 0.4704 |
| Vacancy rate | 6.29 |
| White | 79219 |
| Black | 7352 |
| Asian | 2015 |
| Native | 942 |
| Hispanic/Latino | 104530 |
| Bachelor's or higher | 22798 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 81](/us/states/tx/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
