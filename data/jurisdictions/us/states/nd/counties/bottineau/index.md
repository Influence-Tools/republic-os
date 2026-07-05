---
type: Jurisdiction
title: "Bottineau County, ND"
classification: county
fips: "38009"
state: "ND"
demographics:
  population: 6378
  population_under_18: 1412
  population_18_64: 3328
  population_65_plus: 1638
  median_household_income: 85000
  poverty_rate: 7.59
  homeownership_rate: 79.17
  unemployment_rate: 1.65
  median_home_value: 193200
  gini_index: 0.4701
  vacancy_rate: 32.41
  race_white: 5738
  race_black: 0
  race_asian: 31
  race_native: 297
  hispanic: 164
  bachelors_plus: 1684
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nd/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/6"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Bottineau County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6378 |
| Under 18 | 1412 |
| 18–64 | 3328 |
| 65+ | 1638 |
| Median household income | 85000 |
| Poverty rate | 7.59 |
| Homeownership rate | 79.17 |
| Unemployment rate | 1.65 |
| Median home value | 193200 |
| Gini index | 0.4701 |
| Vacancy rate | 32.41 |
| White | 5738 |
| Black | 0 |
| Asian | 31 |
| Native | 297 |
| Hispanic/Latino | 164 |
| Bachelor's or higher | 1684 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 6](/us/states/nd/districts/senate/6.md) — 100% (state senate)
- [ND House District 6](/us/states/nd/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
