---
type: Jurisdiction
title: "Jackson County, KY"
classification: county
fips: "21109"
state: "KY"
demographics:
  population: 13086
  population_under_18: 3111
  population_18_64: 7597
  population_65_plus: 2378
  median_household_income: 40000
  poverty_rate: 19.46
  homeownership_rate: 77.39
  unemployment_rate: 3.97
  median_home_value: 111500
  gini_index: 0.438
  vacancy_rate: 14.72
  race_white: 12668
  race_black: 30
  race_asian: 6
  race_native: 19
  hispanic: 142
  bachelors_plus: 1095
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/89"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Jackson County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13086 |
| Under 18 | 3111 |
| 18–64 | 7597 |
| 65+ | 2378 |
| Median household income | 40000 |
| Poverty rate | 19.46 |
| Homeownership rate | 77.39 |
| Unemployment rate | 3.97 |
| Median home value | 111500 |
| Gini index | 0.438 |
| Vacancy rate | 14.72 |
| White | 12668 |
| Black | 30 |
| Asian | 6 |
| Native | 19 |
| Hispanic/Latino | 142 |
| Bachelor's or higher | 1095 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 25](/us/states/ky/districts/senate/25.md) — 100% (state senate)
- [KY House District 89](/us/states/ky/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
