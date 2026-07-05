---
type: Jurisdiction
title: "Elmore County, ID"
classification: county
fips: "16039"
state: "ID"
demographics:
  population: 29321
  population_under_18: 7101
  population_18_64: 17882
  population_65_plus: 4338
  median_household_income: 65359
  poverty_rate: 10.49
  homeownership_rate: 65.59
  unemployment_rate: 6.05
  median_home_value: 316500
  gini_index: 0.4031
  vacancy_rate: 9.81
  race_white: 21315
  race_black: 948
  race_asian: 800
  race_native: 274
  hispanic: 5334
  bachelors_plus: 5386
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/id/districts/senate/8"
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

# Elmore County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29321 |
| Under 18 | 7101 |
| 18–64 | 17882 |
| 65+ | 4338 |
| Median household income | 65359 |
| Poverty rate | 10.49 |
| Homeownership rate | 65.59 |
| Unemployment rate | 6.05 |
| Median home value | 316500 |
| Gini index | 0.4031 |
| Vacancy rate | 9.81 |
| White | 21315 |
| Black | 948 |
| Asian | 800 |
| Native | 274 |
| Hispanic/Latino | 5334 |
| Bachelor's or higher | 5386 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 8](/us/states/id/districts/senate/8.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
