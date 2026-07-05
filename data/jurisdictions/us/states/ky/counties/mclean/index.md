---
type: Jurisdiction
title: "McLean County, KY"
classification: county
fips: "21149"
state: "KY"
demographics:
  population: 9114
  population_under_18: 2053
  population_18_64: 5196
  population_65_plus: 1865
  median_household_income: 65596
  poverty_rate: 9.45
  homeownership_rate: 82.75
  unemployment_rate: 5.62
  median_home_value: 148500
  gini_index: 0.43
  vacancy_rate: 12.75
  race_white: 8730
  race_black: 48
  race_asian: 28
  race_native: 15
  hispanic: 203
  bachelors_plus: 1524
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/ky/districts/senate/8"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/12"
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

# McLean County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9114 |
| Under 18 | 2053 |
| 18–64 | 5196 |
| 65+ | 1865 |
| Median household income | 65596 |
| Poverty rate | 9.45 |
| Homeownership rate | 82.75 |
| Unemployment rate | 5.62 |
| Median home value | 148500 |
| Gini index | 0.43 |
| Vacancy rate | 12.75 |
| White | 8730 |
| Black | 48 |
| Asian | 28 |
| Native | 15 |
| Hispanic/Latino | 203 |
| Bachelor's or higher | 1524 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 8](/us/states/ky/districts/senate/8.md) — 100% (state senate)
- [KY House District 12](/us/states/ky/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
