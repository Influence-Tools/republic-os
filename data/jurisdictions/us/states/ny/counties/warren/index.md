---
type: Jurisdiction
title: "Warren County, NY"
classification: county
fips: "36113"
state: "NY"
demographics:
  population: 65517
  population_under_18: 11464
  population_18_64: 38125
  population_65_plus: 15928
  median_household_income: 78442
  poverty_rate: 10.47
  homeownership_rate: 72.12
  unemployment_rate: 4.34
  median_home_value: 267400
  gini_index: 0.4576
  vacancy_rate: 25.31
  race_white: 60511
  race_black: 849
  race_asian: 621
  race_native: 22
  hispanic: 1944
  bachelors_plus: 26325
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/114"
    rel: in-district
    area_weight: 0.9957
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Warren County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65517 |
| Under 18 | 11464 |
| 18–64 | 38125 |
| 65+ | 15928 |
| Median household income | 78442 |
| Poverty rate | 10.47 |
| Homeownership rate | 72.12 |
| Unemployment rate | 4.34 |
| Median home value | 267400 |
| Gini index | 0.4576 |
| Vacancy rate | 25.31 |
| White | 60511 |
| Black | 849 |
| Asian | 621 |
| Native | 22 |
| Hispanic/Latino | 1944 |
| Bachelor's or higher | 26325 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 100% (state senate)
- [NY House District 114](/us/states/ny/districts/house/114.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
