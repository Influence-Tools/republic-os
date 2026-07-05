---
type: Jurisdiction
title: "Randolph County, AR"
classification: county
fips: "05121"
state: "AR"
demographics:
  population: 18838
  population_under_18: 4613
  population_18_64: 10584
  population_65_plus: 3641
  median_household_income: 50911
  poverty_rate: 22.39
  homeownership_rate: 73.55
  unemployment_rate: 5.27
  median_home_value: 130600
  gini_index: 0.448
  vacancy_rate: 15.27
  race_white: 16781
  race_black: 207
  race_asian: 78
  race_native: 48
  hispanic: 488
  bachelors_plus: 2179
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/1"
    rel: in-district
    area_weight: 0.5902
  - to: "us/states/ar/districts/house/2"
    rel: in-district
    area_weight: 0.4096
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Randolph County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18838 |
| Under 18 | 4613 |
| 18–64 | 10584 |
| 65+ | 3641 |
| Median household income | 50911 |
| Poverty rate | 22.39 |
| Homeownership rate | 73.55 |
| Unemployment rate | 5.27 |
| Median home value | 130600 |
| Gini index | 0.448 |
| Vacancy rate | 15.27 |
| White | 16781 |
| Black | 207 |
| Asian | 78 |
| Native | 48 |
| Hispanic/Latino | 488 |
| Bachelor's or higher | 2179 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 21](/us/states/ar/districts/senate/21.md) — 100% (state senate)
- [AR House District 1](/us/states/ar/districts/house/1.md) — 59% (state house)
- [AR House District 2](/us/states/ar/districts/house/2.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
