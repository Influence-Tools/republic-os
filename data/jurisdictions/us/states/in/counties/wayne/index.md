---
type: Jurisdiction
title: "Wayne County, IN"
classification: county
fips: "18177"
state: "IN"
demographics:
  population: 66397
  population_under_18: 15017
  population_18_64: 38279
  population_65_plus: 13101
  median_household_income: 55692
  poverty_rate: 17.89
  homeownership_rate: 69.22
  unemployment_rate: 5.42
  median_home_value: 140200
  gini_index: 0.4914
  vacancy_rate: 12.24
  race_white: 57465
  race_black: 2566
  race_asian: 602
  race_native: 119
  hispanic: 2630
  bachelors_plus: 12752
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/27"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/56"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Wayne County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66397 |
| Under 18 | 15017 |
| 18–64 | 38279 |
| 65+ | 13101 |
| Median household income | 55692 |
| Poverty rate | 17.89 |
| Homeownership rate | 69.22 |
| Unemployment rate | 5.42 |
| Median home value | 140200 |
| Gini index | 0.4914 |
| Vacancy rate | 12.24 |
| White | 57465 |
| Black | 2566 |
| Asian | 602 |
| Native | 119 |
| Hispanic/Latino | 2630 |
| Bachelor's or higher | 12752 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 27](/us/states/in/districts/senate/27.md) — 100% (state senate)
- [IN House District 56](/us/states/in/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
