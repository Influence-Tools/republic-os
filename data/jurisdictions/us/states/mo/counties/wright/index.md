---
type: Jurisdiction
title: "Wright County, MO"
classification: county
fips: "29229"
state: "MO"
demographics:
  population: 18965
  population_under_18: 4900
  population_18_64: 10326
  population_65_plus: 3739
  median_household_income: 47909
  poverty_rate: 18.75
  homeownership_rate: 77.13
  unemployment_rate: 3.53
  median_home_value: 160100
  gini_index: 0.4552
  vacancy_rate: 14.1
  race_white: 17449
  race_black: 103
  race_asian: 65
  race_native: 14
  hispanic: 497
  bachelors_plus: 2755
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/141"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Wright County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18965 |
| Under 18 | 4900 |
| 18–64 | 10326 |
| 65+ | 3739 |
| Median household income | 47909 |
| Poverty rate | 18.75 |
| Homeownership rate | 77.13 |
| Unemployment rate | 3.53 |
| Median home value | 160100 |
| Gini index | 0.4552 |
| Vacancy rate | 14.1 |
| White | 17449 |
| Black | 103 |
| Asian | 65 |
| Native | 14 |
| Hispanic/Latino | 497 |
| Bachelor's or higher | 2755 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 141](/us/states/mo/districts/house/141.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
