---
type: Jurisdiction
title: "Hancock County, KY"
classification: county
fips: "21091"
state: "KY"
demographics:
  population: 9034
  population_under_18: 2157
  population_18_64: 5220
  population_65_plus: 1657
  median_household_income: 65464
  poverty_rate: 16.25
  homeownership_rate: 77.16
  unemployment_rate: 4.38
  median_home_value: 141200
  gini_index: 0.405
  vacancy_rate: 7.38
  race_white: 8513
  race_black: 114
  race_asian: 7
  race_native: 6
  hispanic: 74
  bachelors_plus: 1429
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/senate/8"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/house/14"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Hancock County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9034 |
| Under 18 | 2157 |
| 18–64 | 5220 |
| 65+ | 1657 |
| Median household income | 65464 |
| Poverty rate | 16.25 |
| Homeownership rate | 77.16 |
| Unemployment rate | 4.38 |
| Median home value | 141200 |
| Gini index | 0.405 |
| Vacancy rate | 7.38 |
| White | 8513 |
| Black | 114 |
| Asian | 7 |
| Native | 6 |
| Hispanic/Latino | 74 |
| Bachelor's or higher | 1429 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 8](/us/states/ky/districts/senate/8.md) — 100% (state senate)
- [KY House District 14](/us/states/ky/districts/house/14.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
