---
type: Jurisdiction
title: "Caldwell County, KY"
classification: county
fips: "21033"
state: "KY"
demographics:
  population: 12618
  population_under_18: 2895
  population_18_64: 7019
  population_65_plus: 2704
  median_household_income: 59583
  poverty_rate: 15.15
  homeownership_rate: 70.21
  unemployment_rate: 4.38
  median_home_value: 118500
  gini_index: 0.4279
  vacancy_rate: 17.13
  race_white: 11326
  race_black: 755
  race_asian: 0
  race_native: 0
  hispanic: 186
  bachelors_plus: 2123
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/3"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/house/8"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Caldwell County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12618 |
| Under 18 | 2895 |
| 18–64 | 7019 |
| 65+ | 2704 |
| Median household income | 59583 |
| Poverty rate | 15.15 |
| Homeownership rate | 70.21 |
| Unemployment rate | 4.38 |
| Median home value | 118500 |
| Gini index | 0.4279 |
| Vacancy rate | 17.13 |
| White | 11326 |
| Black | 755 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 186 |
| Bachelor's or higher | 2123 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 3](/us/states/ky/districts/senate/3.md) — 100% (state senate)
- [KY House District 8](/us/states/ky/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
