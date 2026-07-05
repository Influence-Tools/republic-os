---
type: Jurisdiction
title: "Shelby County, KY"
classification: county
fips: "21211"
state: "KY"
demographics:
  population: 49096
  population_under_18: 10890
  population_18_64: 30022
  population_65_plus: 8184
  median_household_income: 82604
  poverty_rate: 9.69
  homeownership_rate: 73.85
  unemployment_rate: 4.17
  median_home_value: 304800
  gini_index: 0.4366
  vacancy_rate: 5.36
  race_white: 39480
  race_black: 1919
  race_asian: 477
  race_native: 209
  hispanic: 5399
  bachelors_plus: 15561
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/senate/7"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/58"
    rel: in-district
    area_weight: 0.9756
  - to: "us/states/ky/districts/house/33"
    rel: in-district
    area_weight: 0.0241
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Shelby County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49096 |
| Under 18 | 10890 |
| 18–64 | 30022 |
| 65+ | 8184 |
| Median household income | 82604 |
| Poverty rate | 9.69 |
| Homeownership rate | 73.85 |
| Unemployment rate | 4.17 |
| Median home value | 304800 |
| Gini index | 0.4366 |
| Vacancy rate | 5.36 |
| White | 39480 |
| Black | 1919 |
| Asian | 477 |
| Native | 209 |
| Hispanic/Latino | 5399 |
| Bachelor's or higher | 15561 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 7](/us/states/ky/districts/senate/7.md) — 100% (state senate)
- [KY House District 58](/us/states/ky/districts/house/58.md) — 98% (state house)
- [KY House District 33](/us/states/ky/districts/house/33.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
