---
type: Jurisdiction
title: "Henry County, TN"
classification: county
fips: "47079"
state: "TN"
demographics:
  population: 32412
  population_under_18: 6439
  population_18_64: 18207
  population_65_plus: 7766
  median_household_income: 50613
  poverty_rate: 18.27
  homeownership_rate: 73.53
  unemployment_rate: 4.83
  median_home_value: 160200
  gini_index: 0.4627
  vacancy_rate: 21.28
  race_white: 28116
  race_black: 2141
  race_asian: 180
  race_native: 129
  hispanic: 977
  bachelors_plus: 6024
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/76"
    rel: in-district
    area_weight: 0.7897
  - to: "us/states/tn/districts/house/74"
    rel: in-district
    area_weight: 0.2099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Henry County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32412 |
| Under 18 | 6439 |
| 18–64 | 18207 |
| 65+ | 7766 |
| Median household income | 50613 |
| Poverty rate | 18.27 |
| Homeownership rate | 73.53 |
| Unemployment rate | 4.83 |
| Median home value | 160200 |
| Gini index | 0.4627 |
| Vacancy rate | 21.28 |
| White | 28116 |
| Black | 2141 |
| Asian | 180 |
| Native | 129 |
| Hispanic/Latino | 977 |
| Bachelor's or higher | 6024 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 76](/us/states/tn/districts/house/76.md) — 79% (state house)
- [TN House District 74](/us/states/tn/districts/house/74.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
