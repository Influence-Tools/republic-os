---
type: Jurisdiction
title: "Bailey County, TX"
classification: county
fips: "48017"
state: "TX"
demographics:
  population: 6913
  population_under_18: 1856
  population_18_64: 3696
  population_65_plus: 1361
  median_household_income: 61420
  poverty_rate: 12.02
  homeownership_rate: 79.9
  unemployment_rate: 0.0
  median_home_value: 105300
  gini_index: 0.4895
  vacancy_rate: 19.38
  race_white: 4929
  race_black: 61
  race_asian: 52
  race_native: 0
  hispanic: 4565
  bachelors_plus: 802
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bailey County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6913 |
| Under 18 | 1856 |
| 18–64 | 3696 |
| 65+ | 1361 |
| Median household income | 61420 |
| Poverty rate | 12.02 |
| Homeownership rate | 79.9 |
| Unemployment rate | 0.0 |
| Median home value | 105300 |
| Gini index | 0.4895 |
| Vacancy rate | 19.38 |
| White | 4929 |
| Black | 61 |
| Asian | 52 |
| Native | 0 |
| Hispanic/Latino | 4565 |
| Bachelor's or higher | 802 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
