---
type: Jurisdiction
title: "Menard County, IL"
classification: county
fips: "17129"
state: "IL"
demographics:
  population: 12095
  population_under_18: 2643
  population_18_64: 6939
  population_65_plus: 2513
  median_household_income: 82176
  poverty_rate: 10.12
  homeownership_rate: 79.46
  unemployment_rate: 3.52
  median_home_value: 185500
  gini_index: 0.4058
  vacancy_rate: 6.64
  race_white: 11472
  race_black: 63
  race_asian: 31
  race_native: 0
  hispanic: 204
  bachelors_plus: 3377
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/il/districts/house/108"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Menard County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12095 |
| Under 18 | 2643 |
| 18–64 | 6939 |
| 65+ | 2513 |
| Median household income | 82176 |
| Poverty rate | 10.12 |
| Homeownership rate | 79.46 |
| Unemployment rate | 3.52 |
| Median home value | 185500 |
| Gini index | 0.4058 |
| Vacancy rate | 6.64 |
| White | 11472 |
| Black | 63 |
| Asian | 31 |
| Native | 0 |
| Hispanic/Latino | 204 |
| Bachelor's or higher | 3377 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 100% (state senate)
- [IL House District 108](/us/states/il/districts/house/108.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
