---
type: Jurisdiction
title: "Madison County, GA"
classification: county
fips: "13195"
state: "GA"
demographics:
  population: 31528
  population_under_18: 7383
  population_18_64: 18351
  population_65_plus: 5794
  median_household_income: 61963
  poverty_rate: 17.24
  homeownership_rate: 76.93
  unemployment_rate: 3.92
  median_home_value: 219700
  gini_index: 0.416
  vacancy_rate: 10.3
  race_white: 24992
  race_black: 2972
  race_asian: 637
  race_native: 49
  hispanic: 2326
  bachelors_plus: 6786
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ga/districts/senate/47"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/123"
    rel: in-district
    area_weight: 0.5545
  - to: "us/states/ga/districts/house/33"
    rel: in-district
    area_weight: 0.4452
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Madison County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31528 |
| Under 18 | 7383 |
| 18–64 | 18351 |
| 65+ | 5794 |
| Median household income | 61963 |
| Poverty rate | 17.24 |
| Homeownership rate | 76.93 |
| Unemployment rate | 3.92 |
| Median home value | 219700 |
| Gini index | 0.416 |
| Vacancy rate | 10.3 |
| White | 24992 |
| Black | 2972 |
| Asian | 637 |
| Native | 49 |
| Hispanic/Latino | 2326 |
| Bachelor's or higher | 6786 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 47](/us/states/ga/districts/senate/47.md) — 100% (state senate)
- [GA House District 123](/us/states/ga/districts/house/123.md) — 55% (state house)
- [GA House District 33](/us/states/ga/districts/house/33.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
