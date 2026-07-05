---
type: Jurisdiction
title: "Meade County, KY"
classification: county
fips: "21163"
state: "KY"
demographics:
  population: 30158
  population_under_18: 6607
  population_18_64: 18843
  population_65_plus: 4708
  median_household_income: 74355
  poverty_rate: 12.23
  homeownership_rate: 74.09
  unemployment_rate: 4.83
  median_home_value: 207900
  gini_index: 0.4091
  vacancy_rate: 10.05
  race_white: 26810
  race_black: 1015
  race_asian: 204
  race_native: 88
  hispanic: 1280
  bachelors_plus: 5701
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ky/districts/senate/5"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/house/27"
    rel: in-district
    area_weight: 0.9982
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Meade County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30158 |
| Under 18 | 6607 |
| 18–64 | 18843 |
| 65+ | 4708 |
| Median household income | 74355 |
| Poverty rate | 12.23 |
| Homeownership rate | 74.09 |
| Unemployment rate | 4.83 |
| Median home value | 207900 |
| Gini index | 0.4091 |
| Vacancy rate | 10.05 |
| White | 26810 |
| Black | 1015 |
| Asian | 204 |
| Native | 88 |
| Hispanic/Latino | 1280 |
| Bachelor's or higher | 5701 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 5](/us/states/ky/districts/senate/5.md) — 100% (state senate)
- [KY House District 27](/us/states/ky/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
