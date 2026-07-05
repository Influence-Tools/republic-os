---
type: Jurisdiction
title: "Laurens County, GA"
classification: county
fips: "13175"
state: "GA"
demographics:
  population: 49798
  population_under_18: 12231
  population_18_64: 28423
  population_65_plus: 9144
  median_household_income: 55010
  poverty_rate: 22.61
  homeownership_rate: 64.27
  unemployment_rate: 5.17
  median_home_value: 154500
  gini_index: 0.5121
  vacancy_rate: 15.74
  race_white: 28331
  race_black: 18192
  race_asian: 573
  race_native: 56
  hispanic: 1646
  bachelors_plus: 9402
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/155"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Laurens County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49798 |
| Under 18 | 12231 |
| 18–64 | 28423 |
| 65+ | 9144 |
| Median household income | 55010 |
| Poverty rate | 22.61 |
| Homeownership rate | 64.27 |
| Unemployment rate | 5.17 |
| Median home value | 154500 |
| Gini index | 0.5121 |
| Vacancy rate | 15.74 |
| White | 28331 |
| Black | 18192 |
| Asian | 573 |
| Native | 56 |
| Hispanic/Latino | 1646 |
| Bachelor's or higher | 9402 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 155](/us/states/ga/districts/house/155.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
