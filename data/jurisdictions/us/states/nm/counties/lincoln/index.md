---
type: Jurisdiction
title: "Lincoln County, NM"
classification: county
fips: "35027"
state: "NM"
demographics:
  population: 20224
  population_under_18: 3369
  population_18_64: 10528
  population_65_plus: 6327
  median_household_income: 53303
  poverty_rate: 19.26
  homeownership_rate: 76.81
  unemployment_rate: 5.07
  median_home_value: 233200
  gini_index: 0.4894
  vacancy_rate: 44.04
  race_white: 14070
  race_black: 205
  race_asian: 106
  race_native: 755
  hispanic: 6664
  bachelors_plus: 7241
districts:
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nm/districts/senate/33"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nm/districts/house/56"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Lincoln County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20224 |
| Under 18 | 3369 |
| 18–64 | 10528 |
| 65+ | 6327 |
| Median household income | 53303 |
| Poverty rate | 19.26 |
| Homeownership rate | 76.81 |
| Unemployment rate | 5.07 |
| Median home value | 233200 |
| Gini index | 0.4894 |
| Vacancy rate | 44.04 |
| White | 14070 |
| Black | 205 |
| Asian | 106 |
| Native | 755 |
| Hispanic/Latino | 6664 |
| Bachelor's or higher | 7241 |

## Districts

- [NM-01](/us/states/nm/districts/01.md) — 100% (congressional)
- [NM Senate District 33](/us/states/nm/districts/senate/33.md) — 100% (state senate)
- [NM House District 56](/us/states/nm/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
