---
type: Jurisdiction
title: "Washington County, ID"
classification: county
fips: "16087"
state: "ID"
demographics:
  population: 11142
  population_under_18: 2474
  population_18_64: 5704
  population_65_plus: 2964
  median_household_income: 54000
  poverty_rate: 15.28
  homeownership_rate: 74.58
  unemployment_rate: 5.24
  median_home_value: 278100
  gini_index: 0.481
  vacancy_rate: 9.22
  race_white: 8857
  race_black: 33
  race_asian: 86
  race_native: 189
  hispanic: 1843
  bachelors_plus: 2167
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/id/districts/senate/9"
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

# Washington County, ID

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11142 |
| Under 18 | 2474 |
| 18–64 | 5704 |
| 65+ | 2964 |
| Median household income | 54000 |
| Poverty rate | 15.28 |
| Homeownership rate | 74.58 |
| Unemployment rate | 5.24 |
| Median home value | 278100 |
| Gini index | 0.481 |
| Vacancy rate | 9.22 |
| White | 8857 |
| Black | 33 |
| Asian | 86 |
| Native | 189 |
| Hispanic/Latino | 1843 |
| Bachelor's or higher | 2167 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 9](/us/states/id/districts/senate/9.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
