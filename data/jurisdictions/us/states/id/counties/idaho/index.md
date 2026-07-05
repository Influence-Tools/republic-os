---
type: Jurisdiction
title: "Idaho County, ID"
classification: county
fips: "16049"
state: "ID"
demographics:
  population: 17432
  population_under_18: 3456
  population_18_64: 8852
  population_65_plus: 5124
  median_household_income: 66325
  poverty_rate: 11.11
  homeownership_rate: 80.93
  unemployment_rate: 3.69
  median_home_value: 310200
  gini_index: 0.4225
  vacancy_rate: 23.89
  race_white: 15876
  race_black: 22
  race_asian: 95
  race_native: 319
  hispanic: 689
  bachelors_plus: 3765
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/id/districts/senate/7"
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

# Idaho County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17432 |
| Under 18 | 3456 |
| 18–64 | 8852 |
| 65+ | 5124 |
| Median household income | 66325 |
| Poverty rate | 11.11 |
| Homeownership rate | 80.93 |
| Unemployment rate | 3.69 |
| Median home value | 310200 |
| Gini index | 0.4225 |
| Vacancy rate | 23.89 |
| White | 15876 |
| Black | 22 |
| Asian | 95 |
| Native | 319 |
| Hispanic/Latino | 689 |
| Bachelor's or higher | 3765 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 7](/us/states/id/districts/senate/7.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
