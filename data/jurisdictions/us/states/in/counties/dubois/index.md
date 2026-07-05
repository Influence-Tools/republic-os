---
type: Jurisdiction
title: "Dubois County, IN"
classification: county
fips: "18037"
state: "IN"
demographics:
  population: 43614
  population_under_18: 10582
  population_18_64: 24848
  population_65_plus: 8184
  median_household_income: 75979
  poverty_rate: 11.02
  homeownership_rate: 74.72
  unemployment_rate: 2.28
  median_home_value: 230100
  gini_index: 0.41
  vacancy_rate: 6.7
  race_white: 38371
  race_black: 346
  race_asian: 211
  race_native: 33
  hispanic: 4372
  bachelors_plus: 9828
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/48"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/63"
    rel: in-district
    area_weight: 0.5108
  - to: "us/states/in/districts/house/74"
    rel: in-district
    area_weight: 0.4891
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Dubois County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43614 |
| Under 18 | 10582 |
| 18–64 | 24848 |
| 65+ | 8184 |
| Median household income | 75979 |
| Poverty rate | 11.02 |
| Homeownership rate | 74.72 |
| Unemployment rate | 2.28 |
| Median home value | 230100 |
| Gini index | 0.41 |
| Vacancy rate | 6.7 |
| White | 38371 |
| Black | 346 |
| Asian | 211 |
| Native | 33 |
| Hispanic/Latino | 4372 |
| Bachelor's or higher | 9828 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 48](/us/states/in/districts/senate/48.md) — 100% (state senate)
- [IN House District 63](/us/states/in/districts/house/63.md) — 51% (state house)
- [IN House District 74](/us/states/in/districts/house/74.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
