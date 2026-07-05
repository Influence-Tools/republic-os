---
type: Jurisdiction
title: "Rio Blanco County, CO"
classification: county
fips: "08103"
state: "CO"
demographics:
  population: 6544
  population_under_18: 1589
  population_18_64: 3812
  population_65_plus: 1143
  median_household_income: 65473
  poverty_rate: 8.5
  homeownership_rate: 74.3
  unemployment_rate: 2.43
  median_home_value: 274400
  gini_index: 0.3543
  vacancy_rate: 14.9
  race_white: 5619
  race_black: 0
  race_asian: 44
  race_native: 41
  hispanic: 709
  bachelors_plus: 1434
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/26"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Rio Blanco County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6544 |
| Under 18 | 1589 |
| 18–64 | 3812 |
| 65+ | 1143 |
| Median household income | 65473 |
| Poverty rate | 8.5 |
| Homeownership rate | 74.3 |
| Unemployment rate | 2.43 |
| Median home value | 274400 |
| Gini index | 0.3543 |
| Vacancy rate | 14.9 |
| White | 5619 |
| Black | 0 |
| Asian | 44 |
| Native | 41 |
| Hispanic/Latino | 709 |
| Bachelor's or higher | 1434 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 26](/us/states/co/districts/house/26.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
