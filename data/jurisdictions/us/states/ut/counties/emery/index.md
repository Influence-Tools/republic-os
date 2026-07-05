---
type: Jurisdiction
title: "Emery County, UT"
classification: county
fips: "49015"
state: "UT"
demographics:
  population: 10046
  population_under_18: 2805
  population_18_64: 5371
  population_65_plus: 1870
  median_household_income: 74291
  poverty_rate: 12.49
  homeownership_rate: 80.1
  unemployment_rate: 3.59
  median_home_value: 218700
  gini_index: 0.3892
  vacancy_rate: 16.23
  race_white: 9385
  race_black: 8
  race_asian: 0
  race_native: 75
  hispanic: 752
  bachelors_plus: 1600
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/26"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/house/69"
    rel: in-district
    area_weight: 0.8358
  - to: "us/states/ut/districts/house/67"
    rel: in-district
    area_weight: 0.1641
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Emery County, UT

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10046 |
| Under 18 | 2805 |
| 18–64 | 5371 |
| 65+ | 1870 |
| Median household income | 74291 |
| Poverty rate | 12.49 |
| Homeownership rate | 80.1 |
| Unemployment rate | 3.59 |
| Median home value | 218700 |
| Gini index | 0.3892 |
| Vacancy rate | 16.23 |
| White | 9385 |
| Black | 8 |
| Asian | 0 |
| Native | 75 |
| Hispanic/Latino | 752 |
| Bachelor's or higher | 1600 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 100% (congressional)
- [UT Senate District 26](/us/states/ut/districts/senate/26.md) — 100% (state senate)
- [UT House District 69](/us/states/ut/districts/house/69.md) — 84% (state house)
- [UT House District 67](/us/states/ut/districts/house/67.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
