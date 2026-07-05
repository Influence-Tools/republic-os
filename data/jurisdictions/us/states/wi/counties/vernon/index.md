---
type: Jurisdiction
title: "Vernon County, WI"
classification: county
fips: "55123"
state: "WI"
demographics:
  population: 31049
  population_under_18: 8081
  population_18_64: 16370
  population_65_plus: 6598
  median_household_income: 71893
  poverty_rate: 13.09
  homeownership_rate: 80.27
  unemployment_rate: 2.49
  median_home_value: 223800
  gini_index: 0.4247
  vacancy_rate: 11.67
  race_white: 29338
  race_black: 90
  race_asian: 65
  race_native: 19
  hispanic: 548
  bachelors_plus: 6973
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/32"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/wi/districts/house/96"
    rel: in-district
    area_weight: 0.998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Vernon County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31049 |
| Under 18 | 8081 |
| 18–64 | 16370 |
| 65+ | 6598 |
| Median household income | 71893 |
| Poverty rate | 13.09 |
| Homeownership rate | 80.27 |
| Unemployment rate | 2.49 |
| Median home value | 223800 |
| Gini index | 0.4247 |
| Vacancy rate | 11.67 |
| White | 29338 |
| Black | 90 |
| Asian | 65 |
| Native | 19 |
| Hispanic/Latino | 548 |
| Bachelor's or higher | 6973 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 32](/us/states/wi/districts/senate/32.md) — 100% (state senate)
- [WI House District 96](/us/states/wi/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
