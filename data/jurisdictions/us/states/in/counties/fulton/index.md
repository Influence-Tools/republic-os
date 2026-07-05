---
type: Jurisdiction
title: "Fulton County, IN"
classification: county
fips: "18049"
state: "IN"
demographics:
  population: 20312
  population_under_18: 4744
  population_18_64: 11401
  population_65_plus: 4167
  median_household_income: 61360
  poverty_rate: 15.26
  homeownership_rate: 80.08
  unemployment_rate: 6.81
  median_home_value: 156500
  gini_index: 0.4305
  vacancy_rate: 16.0
  race_white: 18322
  race_black: 100
  race_asian: 22
  race_native: 19
  hispanic: 1108
  bachelors_plus: 3240
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/17"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Fulton County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20312 |
| Under 18 | 4744 |
| 18–64 | 11401 |
| 65+ | 4167 |
| Median household income | 61360 |
| Poverty rate | 15.26 |
| Homeownership rate | 80.08 |
| Unemployment rate | 6.81 |
| Median home value | 156500 |
| Gini index | 0.4305 |
| Vacancy rate | 16.0 |
| White | 18322 |
| Black | 100 |
| Asian | 22 |
| Native | 19 |
| Hispanic/Latino | 1108 |
| Bachelor's or higher | 3240 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 18](/us/states/in/districts/senate/18.md) — 100% (state senate)
- [IN House District 17](/us/states/in/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
