---
type: Jurisdiction
title: "Latah County, ID"
classification: county
fips: "16057"
state: "ID"
demographics:
  population: 41049
  population_under_18: 7748
  population_18_64: 27223
  population_65_plus: 6078
  median_household_income: 65424
  poverty_rate: 17.64
  homeownership_rate: 58.69
  unemployment_rate: 6.77
  median_home_value: 368600
  gini_index: 0.4759
  vacancy_rate: 7.51
  race_white: 35630
  race_black: 401
  race_asian: 870
  race_native: 206
  hispanic: 2120
  bachelors_plus: 14341
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/id/districts/senate/6"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Latah County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41049 |
| Under 18 | 7748 |
| 18–64 | 27223 |
| 65+ | 6078 |
| Median household income | 65424 |
| Poverty rate | 17.64 |
| Homeownership rate | 58.69 |
| Unemployment rate | 6.77 |
| Median home value | 368600 |
| Gini index | 0.4759 |
| Vacancy rate | 7.51 |
| White | 35630 |
| Black | 401 |
| Asian | 870 |
| Native | 206 |
| Hispanic/Latino | 2120 |
| Bachelor's or higher | 14341 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 6](/us/states/id/districts/senate/6.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
