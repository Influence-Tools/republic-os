---
type: Jurisdiction
title: "Ford County, KS"
classification: county
fips: "20057"
state: "KS"
demographics:
  population: 34074
  population_under_18: 10197
  population_18_64: 19832
  population_65_plus: 4045
  median_household_income: 70781
  poverty_rate: 13.97
  homeownership_rate: 62.49
  unemployment_rate: 5.06
  median_home_value: 151100
  gini_index: 0.4006
  vacancy_rate: 7.43
  race_white: 15956
  race_black: 1184
  race_asian: 424
  race_native: 337
  hispanic: 20130
  bachelors_plus: 5626
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/115"
    rel: in-district
    area_weight: 0.9865
  - to: "us/states/ks/districts/house/119"
    rel: in-district
    area_weight: 0.0135
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Ford County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34074 |
| Under 18 | 10197 |
| 18–64 | 19832 |
| 65+ | 4045 |
| Median household income | 70781 |
| Poverty rate | 13.97 |
| Homeownership rate | 62.49 |
| Unemployment rate | 5.06 |
| Median home value | 151100 |
| Gini index | 0.4006 |
| Vacancy rate | 7.43 |
| White | 15956 |
| Black | 1184 |
| Asian | 424 |
| Native | 337 |
| Hispanic/Latino | 20130 |
| Bachelor's or higher | 5626 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 115](/us/states/ks/districts/house/115.md) — 99% (state house)
- [KS House District 119](/us/states/ks/districts/house/119.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
