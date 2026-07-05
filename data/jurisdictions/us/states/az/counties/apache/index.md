---
type: Jurisdiction
title: "Apache County, AZ"
classification: county
fips: "04001"
state: "AZ"
demographics:
  population: 65341
  population_under_18: 18851
  population_18_64: 20072
  population_65_plus: 26418
  median_household_income: 41438
  poverty_rate: 30.53
  homeownership_rate: 79.44
  unemployment_rate: 10.69
  median_home_value: 63700
  gini_index: 0.5177
  vacancy_rate: 27.23
  race_white: 13582
  race_black: 633
  race_asian: 465
  race_native: 46752
  hispanic: 4169
  bachelors_plus: 9973
districts:
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Apache County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65341 |
| Under 18 | 18851 |
| 18–64 | 20072 |
| 65+ | 26418 |
| Median household income | 41438 |
| Poverty rate | 30.53 |
| Homeownership rate | 79.44 |
| Unemployment rate | 10.69 |
| Median home value | 63700 |
| Gini index | 0.5177 |
| Vacancy rate | 27.23 |
| White | 13582 |
| Black | 633 |
| Asian | 465 |
| Native | 46752 |
| Hispanic/Latino | 4169 |
| Bachelor's or higher | 9973 |

## Districts

- [AZ-02](/us/states/az/districts/02.md) — 100% (congressional)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 100% (state senate)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
