---
type: Jurisdiction
title: "Telfair County, GA"
classification: county
fips: "13271"
state: "GA"
demographics:
  population: 11831
  population_under_18: 1907
  population_18_64: 7682
  population_65_plus: 2242
  median_household_income: 50929
  poverty_rate: 24.11
  homeownership_rate: 64.94
  unemployment_rate: 5.25
  median_home_value: 113300
  gini_index: 0.5074
  vacancy_rate: 28.78
  race_white: 6075
  race_black: 4381
  race_asian: 17
  race_native: 4
  hispanic: 1776
  bachelors_plus: 1291
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/156"
    rel: in-district
    area_weight: 0.5343
  - to: "us/states/ga/districts/house/133"
    rel: in-district
    area_weight: 0.4654
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Telfair County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11831 |
| Under 18 | 1907 |
| 18–64 | 7682 |
| 65+ | 2242 |
| Median household income | 50929 |
| Poverty rate | 24.11 |
| Homeownership rate | 64.94 |
| Unemployment rate | 5.25 |
| Median home value | 113300 |
| Gini index | 0.5074 |
| Vacancy rate | 28.78 |
| White | 6075 |
| Black | 4381 |
| Asian | 17 |
| Native | 4 |
| Hispanic/Latino | 1776 |
| Bachelor's or higher | 1291 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 156](/us/states/ga/districts/house/156.md) — 53% (state house)
- [GA House District 133](/us/states/ga/districts/house/133.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
