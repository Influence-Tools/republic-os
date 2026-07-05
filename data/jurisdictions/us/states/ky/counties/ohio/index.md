---
type: Jurisdiction
title: "Ohio County, KY"
classification: county
fips: "21183"
state: "KY"
demographics:
  population: 23735
  population_under_18: 5663
  population_18_64: 13647
  population_65_plus: 4425
  median_household_income: 57798
  poverty_rate: 12.54
  homeownership_rate: 77.16
  unemployment_rate: 5.04
  median_home_value: 121400
  gini_index: 0.4268
  vacancy_rate: 11.07
  race_white: 21861
  race_black: 139
  race_asian: 39
  race_native: 93
  hispanic: 1131
  bachelors_plus: 3147
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/14"
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

# Ohio County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23735 |
| Under 18 | 5663 |
| 18–64 | 13647 |
| 65+ | 4425 |
| Median household income | 57798 |
| Poverty rate | 12.54 |
| Homeownership rate | 77.16 |
| Unemployment rate | 5.04 |
| Median home value | 121400 |
| Gini index | 0.4268 |
| Vacancy rate | 11.07 |
| White | 21861 |
| Black | 139 |
| Asian | 39 |
| Native | 93 |
| Hispanic/Latino | 1131 |
| Bachelor's or higher | 3147 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 5](/us/states/ky/districts/senate/5.md) — 100% (state senate)
- [KY House District 14](/us/states/ky/districts/house/14.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
