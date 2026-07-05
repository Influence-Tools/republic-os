---
type: Jurisdiction
title: "Bradley County, AR"
classification: county
fips: "05011"
state: "AR"
demographics:
  population: 10208
  population_under_18: 2505
  population_18_64: 5768
  population_65_plus: 1935
  median_household_income: 41476
  poverty_rate: 19.86
  homeownership_rate: 65.96
  unemployment_rate: 6.62
  median_home_value: 94800
  gini_index: 0.515
  vacancy_rate: 25.85
  race_white: 5503
  race_black: 2647
  race_asian: 0
  race_native: 580
  hispanic: 1628
  bachelors_plus: 1413
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.5751
  - to: "us/states/ar/districts/house/94"
    rel: in-district
    area_weight: 0.4247
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Bradley County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10208 |
| Under 18 | 2505 |
| 18–64 | 5768 |
| 65+ | 1935 |
| Median household income | 41476 |
| Poverty rate | 19.86 |
| Homeownership rate | 65.96 |
| Unemployment rate | 6.62 |
| Median home value | 94800 |
| Gini index | 0.515 |
| Vacancy rate | 25.85 |
| White | 5503 |
| Black | 2647 |
| Asian | 0 |
| Native | 580 |
| Hispanic/Latino | 1628 |
| Bachelor's or higher | 1413 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 100% (state senate)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 58% (state house)
- [AR House District 94](/us/states/ar/districts/house/94.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
