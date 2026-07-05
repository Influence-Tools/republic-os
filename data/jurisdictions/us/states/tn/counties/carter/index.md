---
type: Jurisdiction
title: "Carter County, TN"
classification: county
fips: "47019"
state: "TN"
demographics:
  population: 56712
  population_under_18: 11345
  population_18_64: 16411
  population_65_plus: 28956
  median_household_income: 50135
  poverty_rate: 17.08
  homeownership_rate: 75.19
  unemployment_rate: 6.24
  median_home_value: 168200
  gini_index: 0.4533
  vacancy_rate: 13.13
  race_white: 53094
  race_black: 1078
  race_asian: 63
  race_native: 80
  hispanic: 1422
  bachelors_plus: 11778
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/senate/3"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/tn/districts/house/4"
    rel: in-district
    area_weight: 0.6036
  - to: "us/states/tn/districts/house/3"
    rel: in-district
    area_weight: 0.3957
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Carter County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56712 |
| Under 18 | 11345 |
| 18–64 | 16411 |
| 65+ | 28956 |
| Median household income | 50135 |
| Poverty rate | 17.08 |
| Homeownership rate | 75.19 |
| Unemployment rate | 6.24 |
| Median home value | 168200 |
| Gini index | 0.4533 |
| Vacancy rate | 13.13 |
| White | 53094 |
| Black | 1078 |
| Asian | 63 |
| Native | 80 |
| Hispanic/Latino | 1422 |
| Bachelor's or higher | 11778 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 3](/us/states/tn/districts/senate/3.md) — 100% (state senate)
- [TN House District 4](/us/states/tn/districts/house/4.md) — 60% (state house)
- [TN House District 3](/us/states/tn/districts/house/3.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
