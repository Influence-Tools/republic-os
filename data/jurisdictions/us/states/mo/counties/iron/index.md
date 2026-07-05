---
type: Jurisdiction
title: "Iron County, MO"
classification: county
fips: "29093"
state: "MO"
demographics:
  population: 9446
  population_under_18: 1983
  population_18_64: 5360
  population_65_plus: 2103
  median_household_income: 48850
  poverty_rate: 19.27
  homeownership_rate: 75.11
  unemployment_rate: 3.0
  median_home_value: 119300
  gini_index: 0.4383
  vacancy_rate: 17.54
  race_white: 8723
  race_black: 48
  race_asian: 126
  race_native: 26
  hispanic: 210
  bachelors_plus: 1794
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/144"
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

# Iron County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9446 |
| Under 18 | 1983 |
| 18–64 | 5360 |
| 65+ | 2103 |
| Median household income | 48850 |
| Poverty rate | 19.27 |
| Homeownership rate | 75.11 |
| Unemployment rate | 3.0 |
| Median home value | 119300 |
| Gini index | 0.4383 |
| Vacancy rate | 17.54 |
| White | 8723 |
| Black | 48 |
| Asian | 126 |
| Native | 26 |
| Hispanic/Latino | 210 |
| Bachelor's or higher | 1794 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
