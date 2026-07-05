---
type: Jurisdiction
title: "Stewart County, GA"
classification: county
fips: "13259"
state: "GA"
demographics:
  population: 4869
  population_under_18: 592
  population_18_64: 3490
  population_65_plus: 787
  median_household_income: 33250
  poverty_rate: 26.43
  homeownership_rate: 58.95
  unemployment_rate: 5.49
  median_home_value: 65100
  gini_index: 0.5488
  vacancy_rate: 15.87
  race_white: 1397
  race_black: 3303
  race_asian: 10
  race_native: 72
  hispanic: 206
  bachelors_plus: 670
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.0051
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Stewart County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4869 |
| Under 18 | 592 |
| 18–64 | 3490 |
| 65+ | 787 |
| Median household income | 33250 |
| Poverty rate | 26.43 |
| Homeownership rate | 58.95 |
| Unemployment rate | 5.49 |
| Median home value | 65100 |
| Gini index | 0.5488 |
| Vacancy rate | 15.87 |
| White | 1397 |
| Black | 3303 |
| Asian | 10 |
| Native | 72 |
| Hispanic/Latino | 206 |
| Bachelor's or higher | 670 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 99% (congressional)
- [AL-02](/us/states/al/districts/02.md) — 1% (congressional)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
