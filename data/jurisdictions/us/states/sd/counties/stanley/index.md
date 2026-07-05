---
type: Jurisdiction
title: "Stanley County, SD"
classification: county
fips: "46117"
state: "SD"
demographics:
  population: 3015
  population_under_18: 678
  population_18_64: 845
  population_65_plus: 1492
  median_household_income: 87712
  poverty_rate: 5.07
  homeownership_rate: 83.1
  unemployment_rate: 0.48
  median_home_value: 203500
  gini_index: 0.3804
  vacancy_rate: 16.34
  race_white: 2655
  race_black: 3
  race_asian: 0
  race_native: 78
  hispanic: 66
  bachelors_plus: 802
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/24"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Stanley County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3015 |
| Under 18 | 678 |
| 18–64 | 845 |
| 65+ | 1492 |
| Median household income | 87712 |
| Poverty rate | 5.07 |
| Homeownership rate | 83.1 |
| Unemployment rate | 0.48 |
| Median home value | 203500 |
| Gini index | 0.3804 |
| Vacancy rate | 16.34 |
| White | 2655 |
| Black | 3 |
| Asian | 0 |
| Native | 78 |
| Hispanic/Latino | 66 |
| Bachelor's or higher | 802 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 24](/us/states/sd/districts/senate/24.md) — 100% (state senate)
- [SD House District 24](/us/states/sd/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
