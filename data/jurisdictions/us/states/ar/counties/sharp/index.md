---
type: Jurisdiction
title: "Sharp County, AR"
classification: county
fips: "05135"
state: "AR"
demographics:
  population: 17773
  population_under_18: 3622
  population_18_64: 9620
  population_65_plus: 4531
  median_household_income: 44637
  poverty_rate: 16.46
  homeownership_rate: 78.84
  unemployment_rate: 8.14
  median_home_value: 105100
  gini_index: 0.5062
  vacancy_rate: 28.02
  race_white: 16279
  race_black: 88
  race_asian: 119
  race_native: 31
  hispanic: 437
  bachelors_plus: 2327
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/28"
    rel: in-district
    area_weight: 0.6555
  - to: "us/states/ar/districts/house/2"
    rel: in-district
    area_weight: 0.3445
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Sharp County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17773 |
| Under 18 | 3622 |
| 18–64 | 9620 |
| 65+ | 4531 |
| Median household income | 44637 |
| Poverty rate | 16.46 |
| Homeownership rate | 78.84 |
| Unemployment rate | 8.14 |
| Median home value | 105100 |
| Gini index | 0.5062 |
| Vacancy rate | 28.02 |
| White | 16279 |
| Black | 88 |
| Asian | 119 |
| Native | 31 |
| Hispanic/Latino | 437 |
| Bachelor's or higher | 2327 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 100% (state senate)
- [AR House District 28](/us/states/ar/districts/house/28.md) — 66% (state house)
- [AR House District 2](/us/states/ar/districts/house/2.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
