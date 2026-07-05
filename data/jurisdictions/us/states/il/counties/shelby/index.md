---
type: Jurisdiction
title: "Shelby County, IL"
classification: county
fips: "17173"
state: "IL"
demographics:
  population: 20720
  population_under_18: 4412
  population_18_64: 11403
  population_65_plus: 4905
  median_household_income: 72095
  poverty_rate: 9.15
  homeownership_rate: 78.44
  unemployment_rate: 3.02
  median_home_value: 137100
  gini_index: 0.3806
  vacancy_rate: 11.35
  race_white: 20005
  race_black: 45
  race_asian: 38
  race_native: 65
  hispanic: 254
  bachelors_plus: 3419
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Shelby County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20720 |
| Under 18 | 4412 |
| 18–64 | 11403 |
| 65+ | 4905 |
| Median household income | 72095 |
| Poverty rate | 9.15 |
| Homeownership rate | 78.44 |
| Unemployment rate | 3.02 |
| Median home value | 137100 |
| Gini index | 0.3806 |
| Vacancy rate | 11.35 |
| White | 20005 |
| Black | 45 |
| Asian | 38 |
| Native | 65 |
| Hispanic/Latino | 254 |
| Bachelor's or higher | 3419 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 100% (state senate)
- [IL House District 107](/us/states/il/districts/house/107.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
