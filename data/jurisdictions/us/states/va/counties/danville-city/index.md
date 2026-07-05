---
type: Jurisdiction
title: "Danville city, VA"
classification: county
fips: "51590"
state: "VA"
demographics:
  population: 42214
  population_under_18: 10537
  population_18_64: 12620
  population_65_plus: 19057
  median_household_income: 44423
  poverty_rate: 24.65
  homeownership_rate: 47.78
  unemployment_rate: 5.56
  median_home_value: 119100
  gini_index: 0.4877
  vacancy_rate: 14.79
  race_white: 16795
  race_black: 21517
  race_asian: 522
  race_native: 31
  hispanic: 2348
  bachelors_plus: 8128
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/49"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Danville city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42214 |
| Under 18 | 10537 |
| 18–64 | 12620 |
| 65+ | 19057 |
| Median household income | 44423 |
| Poverty rate | 24.65 |
| Homeownership rate | 47.78 |
| Unemployment rate | 5.56 |
| Median home value | 119100 |
| Gini index | 0.4877 |
| Vacancy rate | 14.79 |
| White | 16795 |
| Black | 21517 |
| Asian | 522 |
| Native | 31 |
| Hispanic/Latino | 2348 |
| Bachelor's or higher | 8128 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 9](/us/states/va/districts/senate/9.md) — 100% (state senate)
- [VA House District 49](/us/states/va/districts/house/49.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
