---
type: Jurisdiction
title: "Lincoln County, WI"
classification: county
fips: "55069"
state: "WI"
demographics:
  population: 28426
  population_under_18: 5065
  population_18_64: 16640
  population_65_plus: 6721
  median_household_income: 68164
  poverty_rate: 10.57
  homeownership_rate: 79.53
  unemployment_rate: 3.16
  median_home_value: 192700
  gini_index: 0.4246
  vacancy_rate: 21.77
  race_white: 26638
  race_black: 136
  race_asian: 123
  race_native: 36
  hispanic: 647
  bachelors_plus: 5624
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/35"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Lincoln County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28426 |
| Under 18 | 5065 |
| 18–64 | 16640 |
| 65+ | 6721 |
| Median household income | 68164 |
| Poverty rate | 10.57 |
| Homeownership rate | 79.53 |
| Unemployment rate | 3.16 |
| Median home value | 192700 |
| Gini index | 0.4246 |
| Vacancy rate | 21.77 |
| White | 26638 |
| Black | 136 |
| Asian | 123 |
| Native | 36 |
| Hispanic/Latino | 647 |
| Bachelor's or higher | 5624 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 100% (state senate)
- [WI House District 35](/us/states/wi/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
