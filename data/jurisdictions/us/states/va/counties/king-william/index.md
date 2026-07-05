---
type: Jurisdiction
title: "King William County, VA"
classification: county
fips: "51101"
state: "VA"
demographics:
  population: 18593
  population_under_18: 4224
  population_18_64: 11240
  population_65_plus: 3129
  median_household_income: 86056
  poverty_rate: 5.86
  homeownership_rate: 88.87
  unemployment_rate: 2.29
  median_home_value: 315700
  gini_index: 0.3817
  vacancy_rate: 4.89
  race_white: 14420
  race_black: 2795
  race_asian: 116
  race_native: 208
  hispanic: 612
  bachelors_plus: 3877
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/va/districts/house/68"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# King William County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18593 |
| Under 18 | 4224 |
| 18–64 | 11240 |
| 65+ | 3129 |
| Median household income | 86056 |
| Poverty rate | 5.86 |
| Homeownership rate | 88.87 |
| Unemployment rate | 2.29 |
| Median home value | 315700 |
| Gini index | 0.3817 |
| Vacancy rate | 4.89 |
| White | 14420 |
| Black | 2795 |
| Asian | 116 |
| Native | 208 |
| Hispanic/Latino | 612 |
| Bachelor's or higher | 3877 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 100% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 100% (state senate)
- [VA House District 68](/us/states/va/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
