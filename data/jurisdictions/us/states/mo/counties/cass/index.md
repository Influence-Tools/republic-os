---
type: Jurisdiction
title: "Cass County, MO"
classification: county
fips: "29037"
state: "MO"
demographics:
  population: 110773
  population_under_18: 25988
  population_18_64: 64877
  population_65_plus: 19908
  median_household_income: 87535
  poverty_rate: 6.24
  homeownership_rate: 75.63
  unemployment_rate: 4.15
  median_home_value: 292400
  gini_index: 0.4068
  vacancy_rate: 5.73
  race_white: 93583
  race_black: 5124
  race_asian: 842
  race_native: 308
  hispanic: 6083
  bachelors_plus: 30718
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/62"
    rel: in-district
    area_weight: 0.6237
  - to: "us/states/mo/districts/house/55"
    rel: in-district
    area_weight: 0.3422
  - to: "us/states/mo/districts/house/56"
    rel: in-district
    area_weight: 0.0339
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Cass County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 110773 |
| Under 18 | 25988 |
| 18–64 | 64877 |
| 65+ | 19908 |
| Median household income | 87535 |
| Poverty rate | 6.24 |
| Homeownership rate | 75.63 |
| Unemployment rate | 4.15 |
| Median home value | 292400 |
| Gini index | 0.4068 |
| Vacancy rate | 5.73 |
| White | 93583 |
| Black | 5124 |
| Asian | 842 |
| Native | 308 |
| Hispanic/Latino | 6083 |
| Bachelor's or higher | 30718 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 31](/us/states/mo/districts/senate/31.md) — 100% (state senate)
- [MO House District 62](/us/states/mo/districts/house/62.md) — 62% (state house)
- [MO House District 55](/us/states/mo/districts/house/55.md) — 34% (state house)
- [MO House District 56](/us/states/mo/districts/house/56.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
