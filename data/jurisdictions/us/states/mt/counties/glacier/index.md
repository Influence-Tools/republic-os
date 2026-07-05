---
type: Jurisdiction
title: "Glacier County, MT"
classification: county
fips: "30035"
state: "MT"
demographics:
  population: 13637
  population_under_18: 4134
  population_18_64: 7701
  population_65_plus: 1802
  median_household_income: 46875
  poverty_rate: 31.14
  homeownership_rate: 63.71
  unemployment_rate: 10.02
  median_home_value: 165100
  gini_index: 0.4971
  vacancy_rate: 19.79
  race_white: 4115
  race_black: 34
  race_asian: 81
  race_native: 8812
  hispanic: 389
  bachelors_plus: 1908
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mt/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/16"
    rel: in-district
    area_weight: 0.8792
  - to: "us/states/mt/districts/house/15"
    rel: in-district
    area_weight: 0.1207
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Glacier County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13637 |
| Under 18 | 4134 |
| 18–64 | 7701 |
| 65+ | 1802 |
| Median household income | 46875 |
| Poverty rate | 31.14 |
| Homeownership rate | 63.71 |
| Unemployment rate | 10.02 |
| Median home value | 165100 |
| Gini index | 0.4971 |
| Vacancy rate | 19.79 |
| White | 4115 |
| Black | 34 |
| Asian | 81 |
| Native | 8812 |
| Hispanic/Latino | 389 |
| Bachelor's or higher | 1908 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 8](/us/states/mt/districts/senate/8.md) — 100% (state senate)
- [MT House District 16](/us/states/mt/districts/house/16.md) — 88% (state house)
- [MT House District 15](/us/states/mt/districts/house/15.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
