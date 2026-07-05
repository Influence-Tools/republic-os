---
type: Jurisdiction
title: "Mineral County, MT"
classification: county
fips: "30061"
state: "MT"
demographics:
  population: 4959
  population_under_18: 1028
  population_18_64: 2537
  population_65_plus: 1394
  median_household_income: 63450
  poverty_rate: 13.53
  homeownership_rate: 81.12
  unemployment_rate: 3.1
  median_home_value: 364300
  gini_index: 0.4542
  vacancy_rate: 16.41
  race_white: 4556
  race_black: 9
  race_asian: 14
  race_native: 71
  hispanic: 185
  bachelors_plus: 1222
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/mt/districts/senate/45"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/mt/districts/house/90"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Mineral County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4959 |
| Under 18 | 1028 |
| 18–64 | 2537 |
| 65+ | 1394 |
| Median household income | 63450 |
| Poverty rate | 13.53 |
| Homeownership rate | 81.12 |
| Unemployment rate | 3.1 |
| Median home value | 364300 |
| Gini index | 0.4542 |
| Vacancy rate | 16.41 |
| White | 4556 |
| Black | 9 |
| Asian | 14 |
| Native | 71 |
| Hispanic/Latino | 185 |
| Bachelor's or higher | 1222 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 45](/us/states/mt/districts/senate/45.md) — 100% (state senate)
- [MT House District 90](/us/states/mt/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
