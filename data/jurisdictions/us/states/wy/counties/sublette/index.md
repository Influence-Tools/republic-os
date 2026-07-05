---
type: Jurisdiction
title: "Sublette County, WY"
classification: county
fips: "56035"
state: "WY"
demographics:
  population: 8838
  population_under_18: 1866
  population_18_64: 4836
  population_65_plus: 2136
  median_household_income: 83597
  poverty_rate: 6.89
  homeownership_rate: 83.56
  unemployment_rate: 2.31
  median_home_value: 376200
  gini_index: 0.5444
  vacancy_rate: 30.06
  race_white: 7907
  race_black: 10
  race_asian: 0
  race_native: 22
  hispanic: 648
  bachelors_plus: 2946
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wy/districts/house/20"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Sublette County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8838 |
| Under 18 | 1866 |
| 18–64 | 4836 |
| 65+ | 2136 |
| Median household income | 83597 |
| Poverty rate | 6.89 |
| Homeownership rate | 83.56 |
| Unemployment rate | 2.31 |
| Median home value | 376200 |
| Gini index | 0.5444 |
| Vacancy rate | 30.06 |
| White | 7907 |
| Black | 10 |
| Asian | 0 |
| Native | 22 |
| Hispanic/Latino | 648 |
| Bachelor's or higher | 2946 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 14](/us/states/wy/districts/senate/14.md) — 100% (state senate)
- [WY House District 20](/us/states/wy/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
