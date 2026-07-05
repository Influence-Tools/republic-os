---
type: Jurisdiction
title: "Bristol city, VA"
classification: county
fips: "51520"
state: "VA"
demographics:
  population: 16849
  population_under_18: 3798
  population_18_64: 4880
  population_65_plus: 8171
  median_household_income: 50404
  poverty_rate: 17.95
  homeownership_rate: 63.63
  unemployment_rate: 6.32
  median_home_value: 184100
  gini_index: 0.465
  vacancy_rate: 16.38
  race_white: 14334
  race_black: 969
  race_asian: 76
  race_native: 0
  hispanic: 465
  bachelors_plus: 4177
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/house/44"
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

# Bristol city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16849 |
| Under 18 | 3798 |
| 18–64 | 4880 |
| 65+ | 8171 |
| Median household income | 50404 |
| Poverty rate | 17.95 |
| Homeownership rate | 63.63 |
| Unemployment rate | 6.32 |
| Median home value | 184100 |
| Gini index | 0.465 |
| Vacancy rate | 16.38 |
| White | 14334 |
| Black | 969 |
| Asian | 76 |
| Native | 0 |
| Hispanic/Latino | 465 |
| Bachelor's or higher | 4177 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 44](/us/states/va/districts/house/44.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
