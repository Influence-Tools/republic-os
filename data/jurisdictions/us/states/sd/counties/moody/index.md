---
type: Jurisdiction
title: "Moody County, SD"
classification: county
fips: "46101"
state: "SD"
demographics:
  population: 6397
  population_under_18: 1830
  population_18_64: 1668
  population_65_plus: 2899
  median_household_income: 78427
  poverty_rate: 11.64
  homeownership_rate: 73.47
  unemployment_rate: 2.8
  median_home_value: 226500
  gini_index: 0.4134
  vacancy_rate: 7.25
  race_white: 4772
  race_black: 14
  race_asian: 108
  race_native: 822
  hispanic: 371
  bachelors_plus: 1728
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/house/25"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Moody County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6397 |
| Under 18 | 1830 |
| 18–64 | 1668 |
| 65+ | 2899 |
| Median household income | 78427 |
| Poverty rate | 11.64 |
| Homeownership rate | 73.47 |
| Unemployment rate | 2.8 |
| Median home value | 226500 |
| Gini index | 0.4134 |
| Vacancy rate | 7.25 |
| White | 4772 |
| Black | 14 |
| Asian | 108 |
| Native | 822 |
| Hispanic/Latino | 371 |
| Bachelor's or higher | 1728 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 25](/us/states/sd/districts/senate/25.md) — 100% (state senate)
- [SD House District 25](/us/states/sd/districts/house/25.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
