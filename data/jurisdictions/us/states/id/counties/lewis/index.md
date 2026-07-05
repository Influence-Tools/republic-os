---
type: Jurisdiction
title: "Lewis County, ID"
classification: county
fips: "16061"
state: "ID"
demographics:
  population: 3682
  population_under_18: 808
  population_18_64: 1831
  population_65_plus: 1043
  median_household_income: 51615
  poverty_rate: 15.31
  homeownership_rate: 76.43
  unemployment_rate: 2.42
  median_home_value: 225300
  gini_index: 0.4706
  vacancy_rate: 13.8
  race_white: 3049
  race_black: 42
  race_asian: 37
  race_native: 48
  hispanic: 158
  bachelors_plus: 767
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/6"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Lewis County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3682 |
| Under 18 | 808 |
| 18–64 | 1831 |
| 65+ | 1043 |
| Median household income | 51615 |
| Poverty rate | 15.31 |
| Homeownership rate | 76.43 |
| Unemployment rate | 2.42 |
| Median home value | 225300 |
| Gini index | 0.4706 |
| Vacancy rate | 13.8 |
| White | 3049 |
| Black | 42 |
| Asian | 37 |
| Native | 48 |
| Hispanic/Latino | 158 |
| Bachelor's or higher | 767 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 6](/us/states/id/districts/senate/6.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
