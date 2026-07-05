---
type: Jurisdiction
title: "Lincoln County, ID"
classification: county
fips: "16063"
state: "ID"
demographics:
  population: 5358
  population_under_18: 1393
  population_18_64: 3140
  population_65_plus: 825
  median_household_income: 71453
  poverty_rate: 10.47
  homeownership_rate: 78.9
  unemployment_rate: 4.92
  median_home_value: 255600
  gini_index: 0.3712
  vacancy_rate: 7.09
  race_white: 3421
  race_black: 30
  race_asian: 17
  race_native: 192
  hispanic: 1735
  bachelors_plus: 540
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Lincoln County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5358 |
| Under 18 | 1393 |
| 18–64 | 3140 |
| 65+ | 825 |
| Median household income | 71453 |
| Poverty rate | 10.47 |
| Homeownership rate | 78.9 |
| Unemployment rate | 4.92 |
| Median home value | 255600 |
| Gini index | 0.3712 |
| Vacancy rate | 7.09 |
| White | 3421 |
| Black | 30 |
| Asian | 17 |
| Native | 192 |
| Hispanic/Latino | 1735 |
| Bachelor's or higher | 540 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 26](/us/states/id/districts/senate/26.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
