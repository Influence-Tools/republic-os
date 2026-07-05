---
type: Jurisdiction
title: "Mason County, MI"
classification: county
fips: "26105"
state: "MI"
demographics:
  population: 29207
  population_under_18: 5714
  population_18_64: 15804
  population_65_plus: 7689
  median_household_income: 64748
  poverty_rate: 14.13
  homeownership_rate: 78.31
  unemployment_rate: 4.54
  median_home_value: 219600
  gini_index: 0.4436
  vacancy_rate: 27.25
  race_white: 26749
  race_black: 279
  race_asian: 145
  race_native: 140
  hispanic: 1420
  bachelors_plus: 7971
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.4105
  - to: "us/states/mi/districts/senate/32"
    rel: in-district
    area_weight: 0.4107
  - to: "us/states/mi/districts/house/102"
    rel: in-district
    area_weight: 0.2935
  - to: "us/states/mi/districts/house/101"
    rel: in-district
    area_weight: 0.1172
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Mason County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29207 |
| Under 18 | 5714 |
| 18–64 | 15804 |
| 65+ | 7689 |
| Median household income | 64748 |
| Poverty rate | 14.13 |
| Homeownership rate | 78.31 |
| Unemployment rate | 4.54 |
| Median home value | 219600 |
| Gini index | 0.4436 |
| Vacancy rate | 27.25 |
| White | 26749 |
| Black | 279 |
| Asian | 145 |
| Native | 140 |
| Hispanic/Latino | 1420 |
| Bachelor's or higher | 7971 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 41% (congressional)
- [MI Senate District 32](/us/states/mi/districts/senate/32.md) — 41% (state senate)
- [MI House District 102](/us/states/mi/districts/house/102.md) — 29% (state house)
- [MI House District 101](/us/states/mi/districts/house/101.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
