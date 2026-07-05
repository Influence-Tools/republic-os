---
type: Jurisdiction
title: "Allendale County, SC"
classification: county
fips: "45005"
state: "SC"
demographics:
  population: 7661
  population_under_18: 1396
  population_18_64: 4546
  population_65_plus: 1719
  median_household_income: 32328
  poverty_rate: 28.15
  homeownership_rate: 61.7
  unemployment_rate: 8.49
  median_home_value: 76200
  gini_index: 0.554
  vacancy_rate: 20.05
  race_white: 1877
  race_black: 5081
  race_asian: 313
  race_native: 72
  hispanic: 585
  bachelors_plus: 1250
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.9929
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.0064
  - to: "us/states/sc/districts/senate/40"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/sc/districts/house/91"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Allendale County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7661 |
| Under 18 | 1396 |
| 18–64 | 4546 |
| 65+ | 1719 |
| Median household income | 32328 |
| Poverty rate | 28.15 |
| Homeownership rate | 61.7 |
| Unemployment rate | 8.49 |
| Median home value | 76200 |
| Gini index | 0.554 |
| Vacancy rate | 20.05 |
| White | 1877 |
| Black | 5081 |
| Asian | 313 |
| Native | 72 |
| Hispanic/Latino | 585 |
| Bachelor's or higher | 1250 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 99% (congressional)
- [GA-12](/us/states/ga/districts/12.md) — 1% (congressional)
- [SC Senate District 40](/us/states/sc/districts/senate/40.md) — 100% (state senate)
- [SC House District 91](/us/states/sc/districts/house/91.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
