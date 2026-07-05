---
type: Jurisdiction
title: "Whitfield County, GA"
classification: county
fips: "13313"
state: "GA"
demographics:
  population: 103598
  population_under_18: 25747
  population_18_64: 62368
  population_65_plus: 15483
  median_household_income: 67070
  poverty_rate: 14.84
  homeownership_rate: 67.0
  unemployment_rate: 5.19
  median_home_value: 218000
  gini_index: 0.4511
  vacancy_rate: 7.47
  race_white: 66961
  race_black: 3575
  race_asian: 1492
  race_native: 2145
  hispanic: 38573
  bachelors_plus: 19786
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/54"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/2"
    rel: in-district
    area_weight: 0.3814
  - to: "us/states/ga/districts/house/4"
    rel: in-district
    area_weight: 0.3173
  - to: "us/states/ga/districts/house/6"
    rel: in-district
    area_weight: 0.3011
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Whitfield County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103598 |
| Under 18 | 25747 |
| 18–64 | 62368 |
| 65+ | 15483 |
| Median household income | 67070 |
| Poverty rate | 14.84 |
| Homeownership rate | 67.0 |
| Unemployment rate | 5.19 |
| Median home value | 218000 |
| Gini index | 0.4511 |
| Vacancy rate | 7.47 |
| White | 66961 |
| Black | 3575 |
| Asian | 1492 |
| Native | 2145 |
| Hispanic/Latino | 38573 |
| Bachelor's or higher | 19786 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 54](/us/states/ga/districts/senate/54.md) — 100% (state senate)
- [GA House District 2](/us/states/ga/districts/house/2.md) — 38% (state house)
- [GA House District 4](/us/states/ga/districts/house/4.md) — 32% (state house)
- [GA House District 6](/us/states/ga/districts/house/6.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
