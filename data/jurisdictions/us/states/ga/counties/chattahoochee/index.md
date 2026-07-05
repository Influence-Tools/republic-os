---
type: Jurisdiction
title: "Chattahoochee County, GA"
classification: county
fips: "13053"
state: "GA"
demographics:
  population: 8887
  population_under_18: 1311
  population_18_64: 7179
  population_65_plus: 397
  median_household_income: 61042
  poverty_rate: 13.95
  homeownership_rate: 39.28
  unemployment_rate: 9.05
  median_home_value: 102700
  gini_index: 0.3981
  vacancy_rate: 33.71
  race_white: 5169
  race_black: 1837
  race_asian: 311
  race_native: 128
  hispanic: 1594
  bachelors_plus: 1658
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.9989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Chattahoochee County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8887 |
| Under 18 | 1311 |
| 18–64 | 7179 |
| 65+ | 397 |
| Median household income | 61042 |
| Poverty rate | 13.95 |
| Homeownership rate | 39.28 |
| Unemployment rate | 9.05 |
| Median home value | 102700 |
| Gini index | 0.3981 |
| Vacancy rate | 33.71 |
| White | 5169 |
| Black | 1837 |
| Asian | 311 |
| Native | 128 |
| Hispanic/Latino | 1594 |
| Bachelor's or higher | 1658 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 100% (state senate)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
