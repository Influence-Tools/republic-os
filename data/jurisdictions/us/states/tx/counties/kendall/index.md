---
type: Jurisdiction
title: "Kendall County, TX"
classification: county
fips: "48259"
state: "TX"
demographics:
  population: 48567
  population_under_18: 10852
  population_18_64: 27826
  population_65_plus: 9889
  median_household_income: 114962
  poverty_rate: 5.03
  homeownership_rate: 79.49
  unemployment_rate: 4.74
  median_home_value: 512700
  gini_index: 0.4911
  vacancy_rate: 7.66
  race_white: 36503
  race_black: 455
  race_asian: 800
  race_native: 107
  hispanic: 11835
  bachelors_plus: 22404
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/19"
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

# Kendall County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48567 |
| Under 18 | 10852 |
| 18–64 | 27826 |
| 65+ | 9889 |
| Median household income | 114962 |
| Poverty rate | 5.03 |
| Homeownership rate | 79.49 |
| Unemployment rate | 4.74 |
| Median home value | 512700 |
| Gini index | 0.4911 |
| Vacancy rate | 7.66 |
| White | 36503 |
| Black | 455 |
| Asian | 800 |
| Native | 107 |
| Hispanic/Latino | 11835 |
| Bachelor's or higher | 22404 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 100% (state senate)
- [TX House District 19](/us/states/tx/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
