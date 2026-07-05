---
type: Jurisdiction
title: "Logan County, KY"
classification: county
fips: "21141"
state: "KY"
demographics:
  population: 27986
  population_under_18: 6789
  population_18_64: 15858
  population_65_plus: 5339
  median_household_income: 60382
  poverty_rate: 16.75
  homeownership_rate: 74.28
  unemployment_rate: 5.68
  median_home_value: 164900
  gini_index: 0.4304
  vacancy_rate: 11.77
  race_white: 24901
  race_black: 1253
  race_asian: 92
  race_native: 57
  hispanic: 996
  bachelors_plus: 4103
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.927
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.0729
  - to: "us/states/ky/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/16"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Logan County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27986 |
| Under 18 | 6789 |
| 18–64 | 15858 |
| 65+ | 5339 |
| Median household income | 60382 |
| Poverty rate | 16.75 |
| Homeownership rate | 74.28 |
| Unemployment rate | 5.68 |
| Median home value | 164900 |
| Gini index | 0.4304 |
| Vacancy rate | 11.77 |
| White | 24901 |
| Black | 1253 |
| Asian | 92 |
| Native | 57 |
| Hispanic/Latino | 996 |
| Bachelor's or higher | 4103 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 93% (congressional)
- [KY-02](/us/states/ky/districts/02.md) — 7% (congressional)
- [KY Senate District 32](/us/states/ky/districts/senate/32.md) — 100% (state senate)
- [KY House District 16](/us/states/ky/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
