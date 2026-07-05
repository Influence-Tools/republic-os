---
type: Jurisdiction
title: "Centre County, PA"
classification: county
fips: "42027"
state: "PA"
demographics:
  population: 158576
  population_under_18: 23235
  population_18_64: 110069
  population_65_plus: 25272
  median_household_income: 74291
  poverty_rate: 16.32
  homeownership_rate: 61.79
  unemployment_rate: 4.25
  median_home_value: 323500
  gini_index: 0.4768
  vacancy_rate: 11.23
  race_white: 133022
  race_black: 5257
  race_asian: 9133
  race_native: 475
  hispanic: 5824
  bachelors_plus: 68231
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/25"
    rel: in-district
    area_weight: 0.709
  - to: "us/states/pa/districts/senate/35"
    rel: in-district
    area_weight: 0.291
  - to: "us/states/pa/districts/house/82"
    rel: in-district
    area_weight: 0.4168
  - to: "us/states/pa/districts/house/77"
    rel: in-district
    area_weight: 0.2921
  - to: "us/states/pa/districts/house/171"
    rel: in-district
    area_weight: 0.2908
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Centre County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 158576 |
| Under 18 | 23235 |
| 18–64 | 110069 |
| 65+ | 25272 |
| Median household income | 74291 |
| Poverty rate | 16.32 |
| Homeownership rate | 61.79 |
| Unemployment rate | 4.25 |
| Median home value | 323500 |
| Gini index | 0.4768 |
| Vacancy rate | 11.23 |
| White | 133022 |
| Black | 5257 |
| Asian | 9133 |
| Native | 475 |
| Hispanic/Latino | 5824 |
| Bachelor's or higher | 68231 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 25](/us/states/pa/districts/senate/25.md) — 71% (state senate)
- [PA Senate District 35](/us/states/pa/districts/senate/35.md) — 29% (state senate)
- [PA House District 82](/us/states/pa/districts/house/82.md) — 42% (state house)
- [PA House District 77](/us/states/pa/districts/house/77.md) — 29% (state house)
- [PA House District 171](/us/states/pa/districts/house/171.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
