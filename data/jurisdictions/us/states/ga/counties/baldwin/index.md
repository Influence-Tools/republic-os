---
type: Jurisdiction
title: "Baldwin County, GA"
classification: county
fips: "13009"
state: "GA"
demographics:
  population: 43642
  population_under_18: 8036
  population_18_64: 28090
  population_65_plus: 7516
  median_household_income: 54403
  poverty_rate: 21.71
  homeownership_rate: 61.06
  unemployment_rate: 6.16
  median_home_value: 181900
  gini_index: 0.5423
  vacancy_rate: 18.32
  race_white: 22800
  race_black: 18040
  race_asian: 759
  race_native: 31
  hispanic: 1255
  bachelors_plus: 9908
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9935
  - to: "us/states/ga/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/149"
    rel: in-district
    area_weight: 0.6751
  - to: "us/states/ga/districts/house/128"
    rel: in-district
    area_weight: 0.3245
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Baldwin County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43642 |
| Under 18 | 8036 |
| 18–64 | 28090 |
| 65+ | 7516 |
| Median household income | 54403 |
| Poverty rate | 21.71 |
| Homeownership rate | 61.06 |
| Unemployment rate | 6.16 |
| Median home value | 181900 |
| Gini index | 0.5423 |
| Vacancy rate | 18.32 |
| White | 22800 |
| Black | 18040 |
| Asian | 759 |
| Native | 31 |
| Hispanic/Latino | 1255 |
| Bachelor's or higher | 9908 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 99% (congressional)
- [GA Senate District 25](/us/states/ga/districts/senate/25.md) — 100% (state senate)
- [GA House District 149](/us/states/ga/districts/house/149.md) — 68% (state house)
- [GA House District 128](/us/states/ga/districts/house/128.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
