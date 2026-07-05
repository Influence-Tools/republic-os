---
type: Jurisdiction
title: "Calhoun County, SC"
classification: county
fips: "45017"
state: "SC"
demographics:
  population: 14182
  population_under_18: 2639
  population_18_64: 8081
  population_65_plus: 3462
  median_household_income: 58682
  poverty_rate: 12.94
  homeownership_rate: 85.03
  unemployment_rate: 5.85
  median_home_value: 172100
  gini_index: 0.4791
  vacancy_rate: 12.58
  race_white: 7803
  race_black: 5526
  race_asian: 30
  race_native: 0
  hispanic: 557
  bachelors_plus: 3453
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/sc/districts/senate/26"
    rel: in-district
    area_weight: 0.5019
  - to: "us/states/sc/districts/senate/36"
    rel: in-district
    area_weight: 0.4977
  - to: "us/states/sc/districts/house/93"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Calhoun County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14182 |
| Under 18 | 2639 |
| 18–64 | 8081 |
| 65+ | 3462 |
| Median household income | 58682 |
| Poverty rate | 12.94 |
| Homeownership rate | 85.03 |
| Unemployment rate | 5.85 |
| Median home value | 172100 |
| Gini index | 0.4791 |
| Vacancy rate | 12.58 |
| White | 7803 |
| Black | 5526 |
| Asian | 30 |
| Native | 0 |
| Hispanic/Latino | 557 |
| Bachelor's or higher | 3453 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 100% (congressional)
- [SC Senate District 26](/us/states/sc/districts/senate/26.md) — 50% (state senate)
- [SC Senate District 36](/us/states/sc/districts/senate/36.md) — 50% (state senate)
- [SC House District 93](/us/states/sc/districts/house/93.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
