---
type: Jurisdiction
title: "Rush County, IN"
classification: county
fips: "18139"
state: "IN"
demographics:
  population: 16739
  population_under_18: 3782
  population_18_64: 9699
  population_65_plus: 3258
  median_household_income: 66473
  poverty_rate: 11.87
  homeownership_rate: 74.86
  unemployment_rate: 4.3
  median_home_value: 166800
  gini_index: 0.3875
  vacancy_rate: 8.68
  race_white: 16027
  race_black: 106
  race_asian: 0
  race_native: 0
  hispanic: 321
  bachelors_plus: 2998
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/54"
    rel: in-district
    area_weight: 0.9304
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 0.0696
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Rush County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16739 |
| Under 18 | 3782 |
| 18–64 | 9699 |
| 65+ | 3258 |
| Median household income | 66473 |
| Poverty rate | 11.87 |
| Homeownership rate | 74.86 |
| Unemployment rate | 4.3 |
| Median home value | 166800 |
| Gini index | 0.3875 |
| Vacancy rate | 8.68 |
| White | 16027 |
| Black | 106 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 321 |
| Bachelor's or higher | 2998 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 100% (state senate)
- [IN House District 54](/us/states/in/districts/house/54.md) — 93% (state house)
- [IN House District 55](/us/states/in/districts/house/55.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
