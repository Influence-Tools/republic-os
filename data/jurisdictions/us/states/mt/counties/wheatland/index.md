---
type: Jurisdiction
title: "Wheatland County, MT"
classification: county
fips: "30107"
state: "MT"
demographics:
  population: 2056
  population_under_18: 445
  population_18_64: 1015
  population_65_plus: 596
  median_household_income: 49489
  poverty_rate: 23.02
  homeownership_rate: 75.54
  unemployment_rate: 0.82
  median_home_value: 180800
  gini_index: 0.4833
  vacancy_rate: 23.94
  race_white: 1967
  race_black: 20
  race_asian: 7
  race_native: 32
  hispanic: 51
  bachelors_plus: 434
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/78"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Wheatland County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2056 |
| Under 18 | 445 |
| 18–64 | 1015 |
| 65+ | 596 |
| Median household income | 49489 |
| Poverty rate | 23.02 |
| Homeownership rate | 75.54 |
| Unemployment rate | 0.82 |
| Median home value | 180800 |
| Gini index | 0.4833 |
| Vacancy rate | 23.94 |
| White | 1967 |
| Black | 20 |
| Asian | 7 |
| Native | 32 |
| Hispanic/Latino | 51 |
| Bachelor's or higher | 434 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 100% (state senate)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
