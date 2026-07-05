---
type: Jurisdiction
title: "Ionia County, MI"
classification: county
fips: "26067"
state: "MI"
demographics:
  population: 66574
  population_under_18: 13909
  population_18_64: 42143
  population_65_plus: 10522
  median_household_income: 75611
  poverty_rate: 10.62
  homeownership_rate: 77.29
  unemployment_rate: 3.93
  median_home_value: 198500
  gini_index: 0.4158
  vacancy_rate: 6.06
  race_white: 57874
  race_black: 2261
  race_asian: 304
  race_native: 398
  hispanic: 3539
  bachelors_plus: 11128
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/33"
    rel: in-district
    area_weight: 0.814
  - to: "us/states/mi/districts/senate/18"
    rel: in-district
    area_weight: 0.1859
  - to: "us/states/mi/districts/house/78"
    rel: in-district
    area_weight: 0.748
  - to: "us/states/mi/districts/house/91"
    rel: in-district
    area_weight: 0.1262
  - to: "us/states/mi/districts/house/93"
    rel: in-district
    area_weight: 0.1258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Ionia County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66574 |
| Under 18 | 13909 |
| 18–64 | 42143 |
| 65+ | 10522 |
| Median household income | 75611 |
| Poverty rate | 10.62 |
| Homeownership rate | 77.29 |
| Unemployment rate | 3.93 |
| Median home value | 198500 |
| Gini index | 0.4158 |
| Vacancy rate | 6.06 |
| White | 57874 |
| Black | 2261 |
| Asian | 304 |
| Native | 398 |
| Hispanic/Latino | 3539 |
| Bachelor's or higher | 11128 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 33](/us/states/mi/districts/senate/33.md) — 81% (state senate)
- [MI Senate District 18](/us/states/mi/districts/senate/18.md) — 19% (state senate)
- [MI House District 78](/us/states/mi/districts/house/78.md) — 75% (state house)
- [MI House District 91](/us/states/mi/districts/house/91.md) — 13% (state house)
- [MI House District 93](/us/states/mi/districts/house/93.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
