---
type: Jurisdiction
title: "Robertson County, TN"
classification: county
fips: "47147"
state: "TN"
demographics:
  population: 75539
  population_under_18: 18178
  population_18_64: 46109
  population_65_plus: 11252
  median_household_income: 83047
  poverty_rate: 10.36
  homeownership_rate: 77.62
  unemployment_rate: 3.31
  median_home_value: 335000
  gini_index: 0.4145
  vacancy_rate: 5.26
  race_white: 60710
  race_black: 5448
  race_asian: 566
  race_native: 185
  hispanic: 7559
  bachelors_plus: 15356
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/tn/districts/senate/23"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/66"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Robertson County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 75539 |
| Under 18 | 18178 |
| 18–64 | 46109 |
| 65+ | 11252 |
| Median household income | 83047 |
| Poverty rate | 10.36 |
| Homeownership rate | 77.62 |
| Unemployment rate | 3.31 |
| Median home value | 335000 |
| Gini index | 0.4145 |
| Vacancy rate | 5.26 |
| White | 60710 |
| Black | 5448 |
| Asian | 566 |
| Native | 185 |
| Hispanic/Latino | 7559 |
| Bachelor's or higher | 15356 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 23](/us/states/tn/districts/senate/23.md) — 100% (state senate)
- [TN House District 66](/us/states/tn/districts/house/66.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
