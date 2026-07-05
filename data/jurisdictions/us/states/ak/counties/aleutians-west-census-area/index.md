---
type: Jurisdiction
title: "Aleutians West Census Area, AK"
classification: county
fips: "02016"
state: "AK"
demographics:
  population: 5235
  population_under_18: 683
  population_18_64: 2414
  population_65_plus: 2138
  median_household_income: 135500
  poverty_rate: 11.31
  homeownership_rate: 33.47
  unemployment_rate: 4.31
  median_home_value: 434700
  gini_index: 0.3569
  vacancy_rate: 29.5
  race_white: 1276
  race_black: 369
  race_asian: 2079
  race_native: 435
  hispanic: 715
  bachelors_plus: 892
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.341
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.3219
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.3219
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Aleutians West Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5235 |
| Under 18 | 683 |
| 18–64 | 2414 |
| 65+ | 2138 |
| Median household income | 135500 |
| Poverty rate | 11.31 |
| Homeownership rate | 33.47 |
| Unemployment rate | 4.31 |
| Median home value | 434700 |
| Gini index | 0.3569 |
| Vacancy rate | 29.5 |
| White | 1276 |
| Black | 369 |
| Asian | 2079 |
| Native | 435 |
| Hispanic/Latino | 715 |
| Bachelor's or higher | 892 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 34% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 32% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
