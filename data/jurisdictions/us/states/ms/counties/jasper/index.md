---
type: Jurisdiction
title: "Jasper County, MS"
classification: county
fips: "28061"
state: "MS"
demographics:
  population: 16059
  population_under_18: 3678
  population_18_64: 8943
  population_65_plus: 3438
  median_household_income: 48660
  poverty_rate: 19.43
  homeownership_rate: 82.14
  unemployment_rate: 6.22
  median_home_value: 107100
  gini_index: 0.4537
  vacancy_rate: 18.27
  race_white: 7247
  race_black: 8355
  race_asian: 41
  race_native: 0
  hispanic: 126
  bachelors_plus: 1725
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/34"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/84"
    rel: in-district
    area_weight: 0.6797
  - to: "us/states/ms/districts/house/80"
    rel: in-district
    area_weight: 0.2316
  - to: "us/states/ms/districts/house/79"
    rel: in-district
    area_weight: 0.0887
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Jasper County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16059 |
| Under 18 | 3678 |
| 18–64 | 8943 |
| 65+ | 3438 |
| Median household income | 48660 |
| Poverty rate | 19.43 |
| Homeownership rate | 82.14 |
| Unemployment rate | 6.22 |
| Median home value | 107100 |
| Gini index | 0.4537 |
| Vacancy rate | 18.27 |
| White | 7247 |
| Black | 8355 |
| Asian | 41 |
| Native | 0 |
| Hispanic/Latino | 126 |
| Bachelor's or higher | 1725 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 34](/us/states/ms/districts/senate/34.md) — 100% (state senate)
- [MS House District 84](/us/states/ms/districts/house/84.md) — 68% (state house)
- [MS House District 80](/us/states/ms/districts/house/80.md) — 23% (state house)
- [MS House District 79](/us/states/ms/districts/house/79.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
