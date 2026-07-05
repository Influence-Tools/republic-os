---
type: Jurisdiction
title: "Sac County, IA"
classification: county
fips: "19161"
state: "IA"
demographics:
  population: 9689
  population_under_18: 2105
  population_18_64: 5233
  population_65_plus: 2351
  median_household_income: 73838
  poverty_rate: 9.16
  homeownership_rate: 78.01
  unemployment_rate: 4.43
  median_home_value: 141400
  gini_index: 0.4128
  vacancy_rate: 15.94
  race_white: 8982
  race_black: 49
  race_asian: 63
  race_native: 8
  hispanic: 422
  bachelors_plus: 1902
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Sac County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9689 |
| Under 18 | 2105 |
| 18–64 | 5233 |
| 65+ | 2351 |
| Median household income | 73838 |
| Poverty rate | 9.16 |
| Homeownership rate | 78.01 |
| Unemployment rate | 4.43 |
| Median home value | 141400 |
| Gini index | 0.4128 |
| Vacancy rate | 15.94 |
| White | 8982 |
| Black | 49 |
| Asian | 63 |
| Native | 8 |
| Hispanic/Latino | 422 |
| Bachelor's or higher | 1902 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 4](/us/states/ia/districts/senate/4.md) — 100% (state senate)
- [IA House District 7](/us/states/ia/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
