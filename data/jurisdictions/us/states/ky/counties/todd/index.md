---
type: Jurisdiction
title: "Todd County, KY"
classification: county
fips: "21219"
state: "KY"
demographics:
  population: 12469
  population_under_18: 3370
  population_18_64: 6981
  population_65_plus: 2118
  median_household_income: 61103
  poverty_rate: 20.88
  homeownership_rate: 76.03
  unemployment_rate: 3.23
  median_home_value: 166700
  gini_index: 0.4966
  vacancy_rate: 12.11
  race_white: 10554
  race_black: 835
  race_asian: 23
  race_native: 4
  hispanic: 666
  bachelors_plus: 1873
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/senate/32"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/16"
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

# Todd County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12469 |
| Under 18 | 3370 |
| 18–64 | 6981 |
| 65+ | 2118 |
| Median household income | 61103 |
| Poverty rate | 20.88 |
| Homeownership rate | 76.03 |
| Unemployment rate | 3.23 |
| Median home value | 166700 |
| Gini index | 0.4966 |
| Vacancy rate | 12.11 |
| White | 10554 |
| Black | 835 |
| Asian | 23 |
| Native | 4 |
| Hispanic/Latino | 666 |
| Bachelor's or higher | 1873 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 32](/us/states/ky/districts/senate/32.md) — 100% (state senate)
- [KY House District 16](/us/states/ky/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
