---
type: Jurisdiction
title: "Morgan County, KY"
classification: county
fips: "21175"
state: "KY"
demographics:
  population: 14053
  population_under_18: 2824
  population_18_64: 8745
  population_65_plus: 2484
  median_household_income: 47913
  poverty_rate: 17.07
  homeownership_rate: 78.92
  unemployment_rate: 3.07
  median_home_value: 118200
  gini_index: 0.4943
  vacancy_rate: 14.12
  race_white: 12662
  race_black: 698
  race_asian: 73
  race_native: 8
  hispanic: 506
  bachelors_plus: 2863
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/99"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Morgan County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14053 |
| Under 18 | 2824 |
| 18–64 | 8745 |
| 65+ | 2484 |
| Median household income | 47913 |
| Poverty rate | 17.07 |
| Homeownership rate | 78.92 |
| Unemployment rate | 3.07 |
| Median home value | 118200 |
| Gini index | 0.4943 |
| Vacancy rate | 14.12 |
| White | 12662 |
| Black | 698 |
| Asian | 73 |
| Native | 8 |
| Hispanic/Latino | 506 |
| Bachelor's or higher | 2863 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 99](/us/states/ky/districts/house/99.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
