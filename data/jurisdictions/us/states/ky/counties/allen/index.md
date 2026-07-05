---
type: Jurisdiction
title: "Allen County, KY"
classification: county
fips: "21003"
state: "KY"
demographics:
  population: 21293
  population_under_18: 4914
  population_18_64: 12572
  population_65_plus: 3807
  median_household_income: 61403
  poverty_rate: 13.45
  homeownership_rate: 74.46
  unemployment_rate: 6.87
  median_home_value: 192300
  gini_index: 0.4349
  vacancy_rate: 13.37
  race_white: 20030
  race_black: 100
  race_asian: 3
  race_native: 32
  hispanic: 620
  bachelors_plus: 3755
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9924
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.0075
  - to: "us/states/ky/districts/senate/16"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/22"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Allen County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21293 |
| Under 18 | 4914 |
| 18–64 | 12572 |
| 65+ | 3807 |
| Median household income | 61403 |
| Poverty rate | 13.45 |
| Homeownership rate | 74.46 |
| Unemployment rate | 6.87 |
| Median home value | 192300 |
| Gini index | 0.4349 |
| Vacancy rate | 13.37 |
| White | 20030 |
| Black | 100 |
| Asian | 3 |
| Native | 32 |
| Hispanic/Latino | 620 |
| Bachelor's or higher | 3755 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 99% (congressional)
- [KY-02](/us/states/ky/districts/02.md) — 1% (congressional)
- [KY Senate District 16](/us/states/ky/districts/senate/16.md) — 100% (state senate)
- [KY House District 22](/us/states/ky/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
