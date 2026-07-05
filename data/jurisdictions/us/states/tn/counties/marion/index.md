---
type: Jurisdiction
title: "Marion County, TN"
classification: county
fips: "47115"
state: "TN"
demographics:
  population: 29250
  population_under_18: 5931
  population_18_64: 17200
  population_65_plus: 6119
  median_household_income: 61824
  poverty_rate: 16.31
  homeownership_rate: 78.54
  unemployment_rate: 7.1
  median_home_value: 195200
  gini_index: 0.444
  vacancy_rate: 15.57
  race_white: 26546
  race_black: 871
  race_asian: 72
  race_native: 45
  hispanic: 728
  bachelors_plus: 4937
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/tn/districts/senate/10"
    rel: in-district
    area_weight: 0.9925
  - to: "us/states/tn/districts/senate/16"
    rel: in-district
    area_weight: 0.0074
  - to: "us/states/tn/districts/house/39"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Marion County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29250 |
| Under 18 | 5931 |
| 18–64 | 17200 |
| 65+ | 6119 |
| Median household income | 61824 |
| Poverty rate | 16.31 |
| Homeownership rate | 78.54 |
| Unemployment rate | 7.1 |
| Median home value | 195200 |
| Gini index | 0.444 |
| Vacancy rate | 15.57 |
| White | 26546 |
| Black | 871 |
| Asian | 72 |
| Native | 45 |
| Hispanic/Latino | 728 |
| Bachelor's or higher | 4937 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 10](/us/states/tn/districts/senate/10.md) — 99% (state senate)
- [TN Senate District 16](/us/states/tn/districts/senate/16.md) — 1% (state senate)
- [TN House District 39](/us/states/tn/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
