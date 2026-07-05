---
type: Jurisdiction
title: "Hardeman County, TX"
classification: county
fips: "48197"
state: "TX"
demographics:
  population: 3501
  population_under_18: 746
  population_18_64: 1996
  population_65_plus: 759
  median_household_income: 63333
  poverty_rate: 10.68
  homeownership_rate: 73.9
  unemployment_rate: 2.41
  median_home_value: 81900
  gini_index: 0.4272
  vacancy_rate: 31.97
  race_white: 2575
  race_black: 118
  race_asian: 48
  race_native: 39
  hispanic: 897
  bachelors_plus: 521
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hardeman County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3501 |
| Under 18 | 746 |
| 18–64 | 1996 |
| 65+ | 759 |
| Median household income | 63333 |
| Poverty rate | 10.68 |
| Homeownership rate | 73.9 |
| Unemployment rate | 2.41 |
| Median home value | 81900 |
| Gini index | 0.4272 |
| Vacancy rate | 31.97 |
| White | 2575 |
| Black | 118 |
| Asian | 48 |
| Native | 39 |
| Hispanic/Latino | 897 |
| Bachelor's or higher | 521 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
