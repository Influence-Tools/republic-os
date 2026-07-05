---
type: Jurisdiction
title: "Lafayette County, WI"
classification: county
fips: "55065"
state: "WI"
demographics:
  population: 16942
  population_under_18: 4281
  population_18_64: 9211
  population_65_plus: 3450
  median_household_income: 76462
  poverty_rate: 11.89
  homeownership_rate: 80.16
  unemployment_rate: 2.9
  median_home_value: 194500
  gini_index: 0.4153
  vacancy_rate: 6.51
  race_white: 15422
  race_black: 62
  race_asian: 123
  race_native: 20
  hispanic: 1200
  bachelors_plus: 3346
districts:
  - to: "us/states/wi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/house/51"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Lafayette County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16942 |
| Under 18 | 4281 |
| 18–64 | 9211 |
| 65+ | 3450 |
| Median household income | 76462 |
| Poverty rate | 11.89 |
| Homeownership rate | 80.16 |
| Unemployment rate | 2.9 |
| Median home value | 194500 |
| Gini index | 0.4153 |
| Vacancy rate | 6.51 |
| White | 15422 |
| Black | 62 |
| Asian | 123 |
| Native | 20 |
| Hispanic/Latino | 1200 |
| Bachelor's or higher | 3346 |

## Districts

- [WI-02](/us/states/wi/districts/02.md) — 100% (congressional)
- [WI Senate District 17](/us/states/wi/districts/senate/17.md) — 100% (state senate)
- [WI House District 51](/us/states/wi/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
