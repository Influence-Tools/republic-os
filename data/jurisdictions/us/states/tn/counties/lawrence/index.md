---
type: Jurisdiction
title: "Lawrence County, TN"
classification: county
fips: "47099"
state: "TN"
demographics:
  population: 45385
  population_under_18: 11359
  population_18_64: 25965
  population_65_plus: 8061
  median_household_income: 54706
  poverty_rate: 14.99
  homeownership_rate: 77.55
  unemployment_rate: 4.9
  median_home_value: 194400
  gini_index: 0.4511
  vacancy_rate: 9.28
  race_white: 42177
  race_black: 631
  race_asian: 166
  race_native: 6
  hispanic: 1272
  bachelors_plus: 6444
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/70"
    rel: in-district
    area_weight: 0.6229
  - to: "us/states/tn/districts/house/71"
    rel: in-district
    area_weight: 0.3769
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Lawrence County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45385 |
| Under 18 | 11359 |
| 18–64 | 25965 |
| 65+ | 8061 |
| Median household income | 54706 |
| Poverty rate | 14.99 |
| Homeownership rate | 77.55 |
| Unemployment rate | 4.9 |
| Median home value | 194400 |
| Gini index | 0.4511 |
| Vacancy rate | 9.28 |
| White | 42177 |
| Black | 631 |
| Asian | 166 |
| Native | 6 |
| Hispanic/Latino | 1272 |
| Bachelor's or higher | 6444 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 70](/us/states/tn/districts/house/70.md) — 62% (state house)
- [TN House District 71](/us/states/tn/districts/house/71.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
